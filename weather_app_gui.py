import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


def get_weather(event = None):
    city = city_entry.get()
    api_key = "YOUR_API_KEY_HERE"

    if not city:
        result_label.config(text="⚠️ Please enter a city name!", fg="orange")
        return

    try:
        # ======================
        # Direct geocoding
        # ======================
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # ======================
        # Get current weather data
        # ======================
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        # ======================
        # Get icon
        # ======================
        icon_code = weather_data["weather"][0]["icon"]

        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        image_data = icon_response.content

        photo = ImageTk.PhotoImage(Image.open(BytesIO(image_data)))

        icon_label.config(image=photo, bg="#708090", bd=4, relief="ridge")
        icon_label.image = photo

        final_text = f"🌍 City: {city.capitalize()}\n🌡️ Temp: {temperature}°C\n💧 Humidity: {humidity}%\n☁️ Condition: {description.capitalize()}"

        result_label.config(text=final_text, fg="green")

    except IndexError:
        result_label.config(text=f"❌ Error: City '{city}' not found.\nPlease check the spelling.", fg="red")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"❌ Connection Error:\nCould not connect to the\n weather server.", fg="red")
    except Exception as ex:
        result_label.config(text=f"Unexpected error!!! : {ex}", fg="red")


# ======================
# GUI
# ======================
window = tk.Tk()
window.title("Weather App")
window.geometry("400x500")

window.config(bg="#F0F8FF")

instruction_label = tk.Label(window, text="Enter City Name:", font=("Helvetica", 14, "bold"), bg="#F0F8FF", fg="#333333")
instruction_label.pack(pady=20)

city_entry = tk.Entry(window, font=("Helvetica", 14), justify="center", bd=2, relief="groove")
city_entry.pack(pady=10)

search_button = tk.Button(window, text="Get Weather", font=("Helvetica", 12, "bold"), bg="#007BFF", fg="white", activebackground="#0056b3", activeforeground="white", bd=0, padx=10, pady=5 ,command=get_weather)
search_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 14), fg="blue", bg="#F0F8FF")
result_label.pack(pady=30)

icon_label = tk.Label(window, bg="#F0F8FF")
icon_label.pack(pady=10)

window.bind("<Return>", get_weather)
window.bind("<Escape>", lambda event : window.destroy())

window.mainloop()