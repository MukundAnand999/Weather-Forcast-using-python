import requests
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good Aftenoon")
    else:
        speak("Good Evening")

wishMe()

speak("HI Master Mukund")
speak("welcome to your personal weather forecast application")
print("=" * 125)
print("jarvis: Hi Master Mukund")
print("\t\t\t\t\tWelcome to your Personal Weather Forecaster!\n\n")
print("Just Enter the City you want the weather report for and press Enter! Press 'q' to exit.\n\n")

while True:
    city_name = input("Enter the name of the City (or 'q' to quit): ")

    if city_name.lower() == 'q':
        speak("Exiting the weather forecast application. Goodbye!")
        break

    print("\n\n")

    def gen_report(c):
        url = f'https://wttr.in/{c}'
        try:
            data = requests.get(url)
            E = data.text
        except requests.exceptions.RequestException as e:
            E = "Error Occurred"
        print(E)

    gen_report(city_name)
    print("Thanks to @wttr.in\nall rights reserved to wttr.in\n")


#####################################
#this is using gui

# import sys
# import requests
# import pyttsx3
# import datetime
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
#                              QPushButton, QVBoxLayout, QTextEdit)
# from PyQt5.QtGui import QFont, QPalette, QColor

# class WeatherApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.engine = pyttsx3.init('sapi5')
#         self.engine.setProperty('rate', 150)
#         voices = self.engine.getProperty('voices')
#         self.engine.setProperty('voice', voices[0].id)
#         self.initUI()

#     def speak(self, audio):
#         self.engine.say(audio)
#         self.engine.runAndWait()

#     def initUI(self):
#         self.setWindowTitle('Weather Forecaster')
#         self.setGeometry(100, 100, 600, 400)

#         # Set background and text colors
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(0, 0, 0))  # Black background
#         palette.setColor(QPalette.WindowText, QColor(255, 255, 0)) # Yellow text
#         self.setPalette(palette)
#         self.setAutoFillBackground(True)

#         font = QFont()
#         font.setPointSize(12)

#         self.city_label = QLabel('Enter the name of the City:')
#         self.city_label.setFont(font)
#         self.city_entry = QLineEdit()
#         self.city_entry.setFont(font)
#         self.report_button = QPushButton('Get Weather Report')
#         self.report_button.setFont(font)
#         self.report_button.clicked.connect(self.get_weather_report)
#         self.weather_report_text = QTextEdit()
#         self.weather_report_text.setReadOnly(True)
#         self.weather_report_text.setFont(font)

#         #Style the text edit box
#         self.weather_report_text.setStyleSheet("background-color: #222; color: yellow;")

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.city_label)
#         vbox.addWidget(self.city_entry)
#         vbox.addWidget(self.report_button)
#         vbox.addWidget(self.weather_report_text)

#         self.setLayout(vbox)
#         self.wish_me()
#         self.speak("HI Master Mukund")
#         self.speak("welcome to your personal weather forcast")
#         self.weather_report_text.append("=" * 125)
#         self.weather_report_text.append("jarvis: Hi Master Mukund")
#         self.weather_report_text.append("\t\t\t\t\tWelcome to your Personal Weather Forecaster!\n\n")
#         self.weather_report_text.append("Just Enter the City you want the weather report for and click Enter! It's that simple!\n\n")

#     def wish_me(self):
#         hour = datetime.datetime.now().hour
#         if 0 <= hour < 12:
#             self.speak("Good morning!")
#         elif 12 <= hour < 18:
#             self.speak("Good Aftenoon")
#         else:
#             self.speak("Good Evening")

#     def get_weather_report(self):
#         city_name = self.city_entry.text()
#         self.weather_report_text.append(f"\n\nWeather report for {city_name}:\n")
#         url = f'https://wttr.in/{city_name}'
#         try:
#             data = requests.get(url)
#             report = data.text
#         except requests.exceptions.RequestException as e:
#             report = f"Error Occurred: {e}"
#         self.weather_report_text.append(report)
#         self.weather_report_text.append("\nThanks to @wttr.in\nall the rights reserved to wttr.in")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = WeatherApp()
#     window.show()
#     sys.exit(app.exec_())

