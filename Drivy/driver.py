from fasthtml.common import *
from routing import app,rt
import BackEnd
company = BackEnd.company
reservation = company.get_reservations()

@rt('/driver',methods=["GET","POST"])
def driver():
    global reservation
    return Container(
        Style("""
            body {
                font-family: Arial, sans-serif;
                background: #AEEEEE; /* พื้นหลังสีฟ้าเหมือนหน้า login */
                padding: 20px;
            }
            .header {
                width: 100%;
                background: #4682B4; /* สีฟ้าเข้ม */
                padding: 25px;
                border-bottom: 2px solid #000; /* เส้นขอบด้านล่างเป็นสีดำ */
                text-align: center;
            }
            .content {
                max-width: 600px;
                margin: 80px auto;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            }
            h2, h3, p {
                margin: 0 0 15px 0;
            }
            .info {
                font-size: 18px;
                color: #333;
            }
            button {
                background: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background: #45a049;
            }
        """),
        # Header Bar
        Div(
            H2("DRIVY", style="color: #fff; margin: 0;"),
            _class="header"
        ),
        Div(
            Table(
                Tr(
                    Th("ID:"),
                    Th("renter:"),
                    Th("car id:"),
                    Th("car:"),
                    Th("start date:"),
                    Th("end date:"),
                    Th("location:"),
                    Th("jobs:")  
                ),
                *[Tr(
                    Td(p.get_id()),
                    Td(p.get_renter().get_username()),
                    Td(p.get_car().get_car_id()),
                    Td(p.get_car().get_model()),
                    Td(p.get_start_date()),
                    Td(p.get_end_date()),
                    Td(p.get_location().get_name()),
                    Td(Button("accept" ,type="button"),
                       Button("reject",type="button")) 
                )for p in reservation],
                _class="info"
            )
        )
    )

serve()