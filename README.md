# 🌤️ Python Weather App (GUI)

A simple, user-friendly desktop weather application built with Python. This app allows users to search for a city and instantly view current weather conditions, including temperature, humidity, and a dynamically loaded weather icon.

## ✨ Features
- **Real-time Data:** Fetches live weather data using the OpenWeatherMap API.
- **Dynamic Icons:** Automatically downloads and displays the correct weather icon based on current conditions.
- **Graphical User Interface (GUI):** Clean and modern interface built with `tkinter`.
- **Keyboard Shortcuts:** 
  - Press `Enter` to search.
  - Press `Esc` to close the application.
- **Error Handling:** Gracefully handles invalid city names, typos, and network connection issues.

## 🛠️ Technologies Used
- **Python 3.x**
- **Tkinter** (Built-in GUI library)
- **Requests** (For handling HTTP/API requests)
- **Pillow (PIL)** (For image processing and displaying icons)
- **OpenWeatherMap API** (Direct Geocoding & Current Weather Data)

## 🚀 Installation & Setup

1. **Install required packages:**
Make sure you have Python installed. Then, install the required external libraries using pip:
```pip install requests Pillow```

2. **Get your API Key:**
- Go to OpenWeatherMap and create a free account.
- Generate a free API Key.
- Open the python file and replace "YOUR_API_KEY_HERE" with your actual API key:
``` api_key = "YOUR_API_KEY_HERE"```
   
3. **Run the app:**
```python main.py```

<img width="398" height="491" alt="image" src="https://github.com/user-attachments/assets/6618c7fe-c9c4-4e7f-b023-f2fc44b34818" />
