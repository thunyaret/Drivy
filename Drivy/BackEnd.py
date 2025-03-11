# สถานที่รถ -----------------------------------------------------------------------
class Location:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
# รถ -----------------------------------------------------------------------
class Car:
    def __init__(self, id, model, licensecar, price, status, color, location:Location,pic):
        self.__id = id
        self.__model = model
        self.__licensecar = licensecar
        self.__price = price
        self.__status = status
        self.__color = color
        self.__location = location
        self.__pic = pic
        self.__reviews = []
        self.__ratings = []

    def get_pic(self):
        return self.__pic
    
    def get_review(self):
        for review in self.__reviews:
            return (review.get_comment(), review.get_date())
    
    def get_rating(self):
        for rating in self.__ratings:
            return rating

    def get_location(self):
        return self.__location

    def get_car_id(self):
        return self.__id

    def get_model(self):
        return self.__model
    
    def get_licensecar(self):
        return self.__licensecar
    
    def get_price(self):
        return self.__price
    
    def get_status(self):
        return self.__status
    
    def get_color(self):
        return self.__color

    def status_car(self, new_status):  # อัพเดตสถานะรถ
        self.__status = new_status
        return self.__status

    def add_review_car(self, review): 
        self.__reviews.append(review)
        return self.__reviews

    def add_rating_car(self, rating):
        self.__ratings.append(rating)
        return self.__ratings

    def cal_rating(self):
        if len(self.__ratings) == 0:
            return 0
        return (f" average : {sum(self.__ratings) / len(self.__ratings)}")

# account -----------------------------------------------------------------------
class Account:
    def __init__(self, id, username, password, role):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__role = role

    def get_id(self):
        return self.__id
    
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

class Driver(Account):
    def __init__(self, id, username, password, phone_number,role, licenseDrive):
        super().__init__(id, username, password, role)
        self.__licenseDrive = licenseDrive
        self.__phone_number = phone_number


    def get_licenseDrive(self):
        return self.__licenseDrive

    def accept_job(self):
        if True :
            job = (f"Driver {self.get_username()} accepted the job")
        else :
            job = (f"Driver {self.get_username()} reject the job")
        return job

class Admin(Account):
    def __init__(self, id, username, password, role):
        super().__init__(id, username, password, role)
    
    def accept_payment(self, payment):

        return f"Admin {self.get_username()} accepted payment with id {payment.get_id()}"

class User(Account):
    def __init__(self, id, username, password, role,phone_number, licensedrivUser):
        super().__init__(id, username, password, role)
        self.__licenseUser = licensedrivUser
        self.__phone_number = phone_number

    def get_id(self):
        return super().get_id()
    
    def get_username(self):
        return super().get_username()

    def get_phone_number(self):
        return self.__phone_number

    def get_licenseUser(self):
        return self.__licenseUser
        
    def search_car(self, company, model):
        matching_cars = [car for car in company.get_cars() if car.get_model() == model]
        return matching_cars

# จอง -----------------------------------------------------------------------
class Reservation:
    def __init__(self, id, renter: User, car: Car, start_date, end_date, price, driver=None, promotion=None, insurance=None):
        self.__id = id
        self.__renter = renter
        self.__car = car
        self.__driver = driver
        self.__start_date = start_date
        self.__end_date = end_date
        self.__promotion = promotion
        self.__insurance = insurance
        self.__price = price
        self.__location = car.get_location()

    def get_location(self):
        return self.__location

    def get_car(self):
        return self.__car

    def get_id(self):
        return self.__id
    
    def get_renter(self):
        return self.__renter
        
    def get_driver(self):
        return self.__driver
    
    def get_start_date(self):
        return self.__start_date
    
    def get_end_date(self):
        return self.__end_date
    
    def get_insurance(self):
        return self.__insurance
    
    def get_price(self):
        return self.__price

    def update_price(self):
        base_price = float(self.__car._Car__price)
        if self.__promotion:
            discount = base_price * (self.__promotion._Promotion__percent / 100)
            new_price = base_price - discount
        else:
            new_price = base_price
        self.__price = new_price
        return new_price

    def update_status_car(self, new_status="reserved"):
        self.__car.status_car(new_status)
        return self.__car.get_status()

# เก็บส่วนลด -----------------------------------------------------------------------
class Promotion:
    def __init__(self, id, code, percent):
        self.__id = id
        self.__code = code
        self.__percent = percent

    def get_id(self):
        return self.__id
    
    def get_percent(self):
        return self.__percent

    def check_promotion(self, code):
        return self.__code == code



# ราคาตามฤดูกาล -----------------------------------------------------------------------
class Priceseason:
    def __init__(self, id, high_season=1.2, low_season=0.9):
        self.__id = id
        self.__high_season = high_season
        self.__low_season = low_season

    def get_id(self):
        return self.__id

    def check_season(self, current_month):
        # สมมติว่าเดือน 6,7,8 คือฤดูร้อน (high season)
        if current_month in [6, 7, 8]:
            return self.__high_season
        else:
            return self.__low_season

# รีวิว -----------------------------------------------------------------------
class Review:
    def __init__(self, comment, date):
        self.__comment = comment
        self.__date = date

    def get_comment(self):
        return self.__comment

    def get_date(self):
        return self.__date

# จ่ายเงิน -----------------------------------------------------------------------
class Payment:
    def __init__(self, id, credit=None, qrcode=None):
        self.__id = id
        self.__credit = credit 
        self.__qrcode = qrcode

    def get_id(self):
        return self.__id

    def check_method_payment(self):
        if self.__credit:
            return "credit"
        elif self.__qrcode:
            return "qrcode"
        else:
            return "unknown"

# ประกัน --------------------------------------------------------------------------
class Insurance:
    def __init__(self, id, name, detail):
        self.__id = id
        self.__name = name
        self.__detail = detail

    def get_id(self):
        return self.__id    
    def get_name(self):
        return self.__name
    
    def get_detail(self):
        return self.__detail

# controller -----------------------------------------------------------------------
class Company:
    def __init__(self):
        self.__detailcars = []  # เก็บรายละเอียดรถพร้อมรีวิว+เรทติ้ง
        self.__users = []       # เก็บข้อมูลผู้ใช้งานทั้งหมด (admin, driver, user)
        self.__payments = []
        self.__reservations = []
        self.__historys = []
        self.__promotions = []
        self.__loactions = []
        self.__cars = []        # รวมรถทั้งหมด
        self.__insurances = []
        self.__jobs = []

    def get_reservations(self):
        return self.__reservations
    
    def get_cars(self):
        return self.__cars
    
    def get_loactions(self):
        return self.__loactions

    def add_reservation(self, reservation:Reservation):
        self.__reservations.append(reservation)
        return reservation

    def add_driver(self, driver: Driver):
        self.__users.append(driver)
        return driver

    def add_user(self, user: User):
        self.__users.append(user)
        return user
    
    def get_users(self):
        return self.__users

    def add_car(self, car: Car):
        self.__cars.append(car)
        return car

    def edit_car(self, car_id, **kwargs):
        for car in self.__cars:
            if car._Car__id == car_id:
                for key, value in kwargs.items():
                    if key == "model":
                        car._Car__model = value
                    elif key == "licensecar":
                        car._Car__licensecar = value
                    elif key == "price":
                        car._Car__price = value
                    elif key == "status":
                        car._Car__status = value
                    elif key == "color":
                        car._Car__color = value
                return True
        return False

    def del_car(self, car_id):
        for i, car in enumerate(self.__cars):
            if car._Car__id == car_id:
                del self.__cars[i]
                return True
        return False

    def add_location(self, location: Location):
        self.__loactions.append(location)
        return location

    def login(self, username, password):
        print(f"Attempting login: username={username}, password={password}")  # Debugging
        for user in self.__users:
            # print(f"Checking user: {user.get_username()}")  # Debugging
            if user.get_username() == username and user.get_password() == password:
                print(f"Login successful: {user.get_role()}")  # Debugging
                return user
        return False

    def register(self, username, password, phone_number, role,licensedrivUser):
        for user in self.__users:
            if user.get_username() == username:
                print("Username already exists")  # Debugging
                return False
        new_id = len(self.__users) + 1000
        if role in ["driver", "renter"]:
            if role == "driver":
                new_user = Driver(new_id, username, password, role, phone_number,licensedrivUser)  # เพิ่มเบอร์โทร
            else:
                new_user = User(new_id, username, password, role, phone_number,licensedrivUser)  # เพิ่มเบอร์โทร
        else:
            print("Invalid role selected")
            return False

        self.__users.append(new_user)
        print(f"Registration successful: {new_user.get_username()}")  # Debugging
        return True, "Registration successful"


company = Company()

admin1 = Admin(1001, "admin1", "pass1", "admin")
driver1 = Driver(2001, "driver1", "pass1", "driver","12346789","L-123")
user1 = User(3001, "user1", "pass1", "user", "U-111","12346555")
company.add_user(user1)
company.add_driver(driver1)
company.add_user(admin1)

# ฟังก์ชันสำหรับการเริ่มต้นข้อมูลตัวอย่าง (จะถูกเรียกใช้ทุกครั้งที่ module ถูก import)
    # ตรวจสอบว่าข้อมูลรถยังไม่มีอยู่ ให้เพิ่มข้อมูลตัวอย่าง
        # สร้าง instance สำหรับ Admin, Driver, และ User
# สร้าง instance ของรถ
car1 = Car("1", "Toyota", "D0-1125", 2000, "available", "black", Location(1, "Bangkok"),pic="/img/toyota_black.png")
company.add_car(car1)

# ทดสอบเพิ่มรีวิวและเรทติ้งให้รถ
review1 = Review("Excellent car", "2025-03-01")
car1.add_review_car(review1)
car1.add_rating_car(4.5)
car1.add_rating_car(5.0)

# สร้างรถเพิ่มอีกคัน
car2 = Car("2", "Honda", "D0-1126", 2500, "available", "white", Location(2, "Chiang Mai"),pic="/img/toyota_white.jpg")
company.add_car(car2)

# เรียกใช้งาน init_data() เมื่อ module ถูก import
reservation1 = Reservation(1, user1, car1, "2025-03-01", "2025-03-03", 2000)
company.add_reservation(reservation1)
# ทดสอบการรัน backend เมื่อรันไฟล์โดยตรง
if __name__ == "__main__":
    print("Registered Users:")
    for u in company.get_users():
        print(u.get_username(), u.get_role())
    print("Cars in Company:")
    for c in company.get_cars():
        print(c.get_id(), c.get_model(), c.get_licensecar(), c.get_price(), c.get_status(), c.get_color())