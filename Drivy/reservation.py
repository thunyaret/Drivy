from fasthtml.common import *
from routing import app, rt
import BackEnd
import search
date = 0
reservation = BackEnd.Reservation
company = BackEnd.company
car = BackEnd.Car
total = 0
# Endpoint สำหรับแสดงฟอร์มจองรถ
@rt('/reservation/form', methods=["GET", "POST"])
def reservation_form():
    return Container(
        Style("""
            body { font-family: Arial; background: #F5F5F5; padding: 20px; }
            .form-container { max-width: 500px; margin: 40px auto; background: #FFF; padding: 20px; 
                               border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }
            label { display: block; margin-top: 10px; font-weight: bold; }
            input { width: 100%; padding: 8px; margin-top: 5px; }
            button { margin-top: 20px; background: #4CAF50; color: white; border: none; 
                     padding: 10px 20px; border-radius: 5px; cursor: pointer; }
            button:hover { background: #45a049; }
        """),
        Div(
            H2("จองรถ"),
            Form(
                # ส่งข้อมูลแบบ POST ไปที่ /reservation
                *[Div(
                    Label(car.get_name()),
                    Img(car.get_pic()),
                    Label("PRICE : " + str(car.get_price()) + " บาท/วัน"),
                    Label("STATUS : " + car.get_status()),
                    Label("START :" + search.start_date),
                    Label("END :" + search.end_date),
                    Label("DATE OF RENT : " + str(date)),
                    Label("REVIEW : " + car.get_review()),
                    Label("RATING : " + car.get_rating()),
                
                    Label("CODE PROMOTION :"),
                    Input(name="promotion_code", type="text", placeholder="CODE PROMOTION"),
                    Label("Have insurance?", type="text", name="insurance_checkbox"),
                    *[Input(insu.get_detail(), type="checkbox",id="insurance",name="insurance")for insu in company.get_insurance()],

                    Label("TOTAL PRICE : " + total ,id="total_price",name="total_price"),

                    Button("payment", type="submit")
                )for car in search.show_car],
                action="/pay", method="POST"
            ),
            _class="form-container"
        )
    )

@rt('/pay', methods=["POST"])
def build_reservation(car_id: str,start_date,end_date,promotion_code=None, insurance=None):

    global date
    date += reservation.count_date(start_date, end_date)

    global total
    for pro in company.get_promotions() :
        if promotion_code == pro and insurance == None:
            total = ((car.get_price() * date)-company.get_percent())
        elif promotion_code == pro and insurance != None:
            total = ((car.get_price() * date)-company.get_percent())+company.get_insurance().get_price()
        elif promotion_code != pro and insurance == None:
            total = (car.get_price() * date)
        elif promotion_code != pro and insurance != None:
            total = (car.get_price() * date)+company.get_insurance().get_price()
    return RedirectResponse("/payment")


serve()
