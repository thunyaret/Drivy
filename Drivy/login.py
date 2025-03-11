from fasthtml.common import *
from routing import app, rt, serve
import BackEnd
from BackEnd import Admin, User, Driver

# ใช้งาน instance ของ Company จาก BackEnd.py
company = BackEnd.company

# ฟังก์ชัน RedirectResponse แบบง่าย (ใช้ JavaScript redirect)
def RedirectResponse(url):
    return Container(
        Script("window.location.href='{}'".format(url))
    )

@rt('/')
def get(success_message=None, error_message=None):
    # สร้างหน้า HTML สำหรับแสดงฟอร์ม Login และ Register
    return Title("DRIVY"), Container(
        Style(""" 
            .tab-btn { 
                color: #1C1C3B; 
                font-size: 18px; 
                font-weight: bold; 
                background: transparent; 
                border: none;
                outline: none; 
                padding: 10px 20px; 
                cursor: pointer; 
                transition: background 0.3s;
            }
            .tab-btn:hover { background: #D3D3D3; }
            .tab-btn.active { border-bottom: 2px solid #1C1C3B; }
            .form-section { 
                display: none; 
                background: #fff; 
                padding: 20px; 
                border-radius: 10px; 
                border: 1px solid #1C1C3B; 
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2); 
                margin-top: 20px;
                transition: opacity 0.5s ease;
            }
            .form-section.active { display: block; opacity: 1; }
            .success-message {
                color: green;
                font-size: 20px;
                text-align: center;
                margin-top: 20px;
            }
            .error-message {
                color: red;
                font-size: 20px;
                text-align: center;
                margin-top: 20px;
            }
        """),
        Div(
            Div(H2("DRIVY", style="color: #B0E0E6; margin: 0;")),
            style="width: 100%; background: #4682B4; padding: 25px; border-bottom: 2px solid #502314; position: fixed; top: 0; left: 0; z-index: 1000;"
        ),
        Body(
            Div(
                H3("LOGIN / REGISTER", style="font-size: 36px; text-align: center; color: #1C1C3B;"),
                Div(
                    Button("Login", type="button", id="loginBtn", _class="tab-btn active"),
                    Button("Register", type="button", id="registerBtn", _class="tab-btn"),
                    style="text-align: center; margin-bottom: 10px;"
                ),
                # แสดงข้อความแจ้งเตือนถ้ามี
                (Div(H3(success_message, _class="success-message")) if success_message else None),
                (Div(H3(error_message, _class="error-message")) if error_message else None),
                # แบบฟอร์มสำหรับ Login
                Form(
                    Div(
                        Div(Label("Username"), Input(type="text", id="login_username", name="login_username", required=True)),
                        Div(Label("Password"), Input(type="password", id="login_password", name="login_password", required=True))
                    ),
                    Button("LOG IN", type="submit"),
                    method="POST",
                    action="/login",
                    style="background: #AEEEEE; padding: 20px; min-height: 100vh; margin-top: 80px;",
                    id="login-section",
                    _class="form-section active"
                ),
                # แบบฟอร์มสำหรับ Register
                Form(
                    Div(
                        Div(Label("Username"), Input(type="text", id="register_username", name="register_username", required=True)),
                        Div(Label("Password"), Input(type="password", id="register_password", name="register_password", required=True)),
                        Div(Label("Phone Number"), Input(type="text", id="register_number", name="register_number", required=True)),
                         Div(Label("license Number"), Input(type="text", id="license_number", name="license_number", required=True)),
                        Div(
                            Label(Input(type="radio", name="role", value="driver", required=True), "driver"),
                            Label(Input(type="radio", name="role", value="renter", required=True), "renter")
                        )
                    ),
                    Button("REGISTER", type="submit"),
                    method="POST",  # ใช้ POST สำหรับส่งข้อมูลลงทะเบียน
                    action="/register",
                    style="background: #AEEEEE; padding: 20px; min-height: 100vh; margin-top: 80px;",
                    id="register-section",
                    _class="form-section"
                ),
                Script(""" 
                    // สลับการแสดงฟอร์ม Login และ Register ด้วย JavaScript
                    document.getElementById('loginBtn').addEventListener('click', function() {
                        document.getElementById('loginBtn').classList.add('active');
                        document.getElementById('registerBtn').classList.remove('active');
                        document.getElementById('login-section').classList.add('active');
                        document.getElementById('register-section').classList.remove('active');
                    });
                    document.getElementById('registerBtn').addEventListener('click', function() {
                        document.getElementById('registerBtn').classList.add('active');
                        document.getElementById('loginBtn').classList.remove('active');
                        document.getElementById('register-section').classList.add('active');
                        document.getElementById('login-section').classList.remove('active');
                    });
                """)
            )
        )
    )

@rt('/register', methods=["GET", "POST"])
def register(register_username:str, register_password:str, register_number:int, role:str,license_number:str):
    # ตรวจสอบว่าข้อมูลถูกส่งมาครบหรือไม่
    if not (register_username and register_password and register_number and role and license_number):
        return get(error_message="กรุณากรอกข้อมูลให้ครบถ้วนสำหรับการสมัครสมาชิก")
    
    # เรียกใช้งานฟังก์ชัน register จาก BackEnd
    success, msg = company.register(
        register_username.strip(),
        register_password.strip(),
        register_number,
        role.strip(),
        license_number.strip()
    )
    
    if success:
        return get(success_message="การสมัครสมาชิกสำเร็จ กรุณาเข้าสู่ระบบ")
    else:
        return get(error_message=f"การสมัครสมาชิกล้มเหลว: {msg}")

@rt('/login', methods=["GET", "POST"])
def login(login_username:str, login_password:str):
    # ตรวจสอบว่าข้อมูล Login ถูกส่งมาครบหรือไม่
    if not (login_username and login_password):
        return get(error_message="กรุณากรอกข้อมูลให้ครบถ้วนในการเข้าสู่ระบบ")
    
    # username = login_username.strip()
    # password = login_password.strip()
    
    user = company.login(login_username, login_password)
    
    # เปลี่ยนเส้นทาง (redirect) ตามบทบาทของผู้ใช้
    if isinstance(user, User):
        return RedirectResponse("/search")
    elif isinstance(user, Driver):
        return RedirectResponse("/driver")
    elif isinstance(user, Admin):
        return RedirectResponse("/admin")
    else:
        return get(error_message="ข้อมูลเข้าสู่ระบบผิดพลาด กรุณาลองใหม่อีกครั้ง")

# เริ่มต้นเซิร์ฟเวอร์
serve()
