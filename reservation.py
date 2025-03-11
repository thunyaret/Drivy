from fasthtml.common import *
from routing import app, rt, serve
import BackEnd
company = BackEnd.company

@rt('/reservation')
def reservation_page():
    # ดึงรายการ reservation จาก backend
    reservations = company._Company__reservations
    if reservations:
        reservation_info = Table(
            Tr(
                Th("Reservation ID"),
                Th("Renter Username"),
                Th("Car Model"),
                Th("Start Date"),
                Th("End Date"),
                Th("Price"),
                Th("Car Status"),
                Th("Driver")
            ),
            *[
                Tr(
                    Td(res.get_id()),
                    Td(res.get_renter().get_username()),
                    Td(res._Reservation__car.get_model()),
                    Td(res.get_start_date()),
                    Td(res.get_end_date()),
                    Td(str(res.get_price())),
                    Td(res._Reservation__car.get_status()),
                    Td(res.get_driver().get_username() if res.get_driver() else "Not assigned")
                ) for res in reservations
            ],
            {"style": "width: 100%;"}
        )
    else:
        reservation_info = P("No reservation found.")

    # ส่วนเลือกวันที่เช่า
    date_selection = Div(
        Label("Select Rental Start Date: "),
        Input("", {"type": "date", "id": "start_date", "style": "padding:8px; margin:5px;"}),
        Label("Select Rental End Date: "),
        Input("", {"type": "date", "id": "end_date", "style": "padding:8px; margin:5px;"}),
        {"style": "text-align: center; margin-top: 20px;"}
    )

    return Container(
        Style("""
            body {
                font-family: Arial, sans-serif;
                background: #F5F5F5;
                padding: 20px;
            }
            .header {
                width: 100%;
                background: #4682B4;
                padding: 20px;
                color: #FFF;
                text-align: center;
                margin-bottom: 20px;
            }
            .content {
                max-width: 800px;
                margin: auto;
                background: #FFF;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                text-align: center;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                padding: 10px;
                border: 1px solid #ddd;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
            button {
                background: #4CAF50;
                color: #FFF;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                margin: 10px;
            }
            button:hover {
                background: #45a049;
            }
        """),
        Div(
            H2("Reservation Details", style="color: #fff; margin: 0;"),
            {"class": "header"}
        ),
        Body(
            Div(
                H3("Reservation Information", {"style": "color: #1C1C3B;"}),
                reservation_info,
                date_selection,
              
                Button("Proceed to Payment", {"type": "button", "onclick": "window.location.href='/payment'"})
                , {"class": "content"}
            ),
            {"style": "background: #F5F5F5; padding: 20px; min-height: 100vh;"}
        )
    )

serve()