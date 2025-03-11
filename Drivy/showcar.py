from fasthtml.common import *
from routing import app, rt
import BackEnd
import search
car = BackEnd.Car
company = BackEnd.company
@rt('/showcar', methods=["GET"])
def showcar():
    print("Cars to show:", search.show_car)
    return Container(
        Style("""
            /* กำหนด style สำหรับทั้งหน้า */
            body {
                font-family: Arial, sans-serif;
                background: #AEEEEE;
                padding: 20px;
            }
            .header {
                width: 100%;
                background: #4682B4;
                padding: 25px;
                border-bottom: 2px solid #502314;
                position: fixed;
                top: 0;
                left: 0;
                z-index: 1000;
            }
            .header h2 {
                color: #B0E0E6;
                margin: 0;
            }
            .content {
                margin-top: 80px;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 2px 4px rgba(0,0,0,0.2);
            }
            h3 {
                text-align: center;
                color: #1C1C3B;
                font-size: 36px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                padding: 8px;
                border: 1px solid #ddd;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #f9f9f9;
            }
            button {
                background: #4CAF50;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background: #45a049;
            }
            img {
                width: 100px;
                height: auto;
                border-radius: 5px;
            }
        """),

        # Header Bar
        Div(
            Div(
                Div(
                    H2("DRIVY", style="color: #fff; margin: 0;"),
                    style="display: flex; align-items: center; gap: 0px;"
                ),
                style="display: flex; justify-content: space-between; align-items: center; width: 100%;"
            ),
            _class="header"
        ),
        # Body Content

        Body(
            Div(
                H3("Car Details"),
                Table(
                    # Header ของตาราง
                    Tr(
                        Th("Image"),
                        Th("ID"),
                        Th("Model"),
                        Th("License"),
                        Th("Price"),
                        Th("Color"),
                        Th("Select")
                    ),
                     # สร้างแถวข้อมูลรถจาก backend
                    *[Tr(
                            Td(Img(src = car.get_pic())),
                            Td(car.get_car_id()),
                            Td(car.get_model()),
                            Td(car.get_licensecar()),
                            Td(car.get_price()),
                            Td(car.get_color()),
                            Td(Button("Select", type="submit"),action = "/reservation", method = "GET")
                        ) for car in search.show_car],
                    style= "width: 100%;"
                ),
                _class="content"
            ),
            style="background: #AEEEEE; padding: 20px; min-height: 100vh;"
        )
    )