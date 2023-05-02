# Weather Fetcber App
# Author: Bryan Yen Sheng Lee

# Weather Fetcher finds the current weather of any city using the OpenWeatherMap API in Python

import requests
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class FrontEnd(QWidget):
    """FrontEnd inherits functions from QWidget for access to setLayout, setGeometry, setWindowTitle"""

    def __init__(self):
        """Initialize superclass (QWidget)"""

        #Superclass constructor
        super().__init__()             

        # Elements of UI in V Box
        enter_city_label = QLabel("Enter City Name:")
        self.city_entry_textbox = QLineEdit("")
        self.city_entry_textbox.returnPressed.connect(self.enter_pressed_callback)
        self.search_button = QPushButton()
        self.search_button.setText("Search")
        self.search_button.clicked.connect(self.search_button_callback)

        # Elements of UI in H box 
        weather_label = QLabel("Weather:")
        self.weather_result_label = QLabel("--")
        temp_label = QLabel("Temperature(C):")
        self.temp_result_label = QLabel("--")

        # Layout for H Box 
        result_layout = QHBoxLayout()
        result_layout.addStretch()                      
        result_layout.addWidget(weather_label)
        result_layout.addWidget(self.weather_result_label)
        result_layout.addWidget(temp_label)
        result_layout.addWidget(self.temp_result_label)
        result_layout.addStretch()                     

        # Layout for V Box
        application_layout = QVBoxLayout()
        application_layout.addWidget(enter_city_label)
        application_layout.addWidget(self.city_entry_textbox)
        application_layout.addWidget(self.search_button)
        application_layout.addLayout(result_layout)

        # Using the V Box Layout as the main layout for application
        self.setLayout(application_layout)

        # Window Definition
        self.setGeometry(300, 300, 350, 250)            
        self.setWindowTitle('Weather Fetcher')
        self.show()


    def search_button_callback(self):
        """Function called whenever search button is pressed"""

        text_box_value = self.city_entry_textbox.text()
        print("Button pressed {}".format(text_box_value))
        self.api_handler(text_box_value)
    

    def enter_pressed_callback(self):
        """Function called whenever enter is pressed"""

        text_box_value = self.city_entry_textbox.text()
        print("Enter pressed {}".format(text_box_value))
        self.api_handler(text_box_value)


    def api_handler(self, input_city):
        """Function to call API to get results"""


        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
        request_url = f"{BASE_URL}?appid={API_KEY}&q={input_city}"
        response = requests.get(request_url)

        if not(response.status_code == 200):
            print("API Call Error: {}".format(response.status_code))
        else:
            data = response.json()

            weather = data['weather'][0]['main']
            self.weather_result_label.setText(weather)

            temperature = round(data["main"]["temp"] - 273.15, 2)
            self.temp_result_label.setText("{} C".format(temperature))

            print(weather, temperature)


app = QApplication([])              # Initialize QT library
frontend_handler = FrontEnd()       # Define & Initialize UI Elements

app.exec()                          # Execute app 