import tkinter as tk
import requests
from datetime import datetime

apiKey = 'a393a1d9db732e99ca504204603d38e8'

def displayWeatherInfo():
	city = cityInput.get()
	if not city:
		resultLabel.config(text="Please Enter a City name!")
		return

	url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
 
	try:
		response = requests.get(url)
		data = response.json()

		if data["cod"] != 200:
			resultLabel.config(text=f"Error: {data['message']}")
			return

		main = data["weather"][0]["main"]
		desc = data["weather"][0]["description"]
		temp = data["main"]["temp"]
		feels_like = data["main"]["feels_like"]
		sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I %M %p")
		sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I %M %p")
  

		weather_info = (
			f"Weather: {main} ({desc}) \n"
			f"Temparature: {temp} \n"
			f"feels like:{feels_like} \n"
			f"sunrise: {sunrise}"
			f"sunset:{sunset}"
		)
  
		resultLabel.config(text=weather_info)

  
  
	except Exception as e:
		resultLabel.config(text="Unable to fetch Weather data")
 

def on_enter(event):
    event.widget.config(bg="#45a049")
    
def on_leave(event):
    event.widget.config(bg="#4CAF50")

root = tk.Tk()
root.geometry('500x600')
root.title("PyAtmos")
root.configure(bg="#87CEEB")

titleLabel = tk.Label(
    root,
    text="Weather Forcast 🌤",
	font=("Helvatic", 20, "bold"),
	bg="#87CEEB",
	fg="white"
)
titleLabel.pack(pady=20)

cityInput = tk.Entry(root, font=("Helvatica", 14), justify="center", relief="flat")
cityInput.pack(pady=10, ipadx=10, ipady=5)

submitBtn = tk.Button(
	root,
 text="Check Weather 🌦",
 bg="#4CAF50",
 fg="white",
 relief="flat",
 padx = 20, 
 pady=20,
 command=displayWeatherInfo
)
submitBtn.pack(pady=10)
submitBtn.bind("<Enter>", on_enter)
submitBtn.bind("<Leave>", on_leave)

resultFrame = tk.Frame(root, bg="white", bd=2)
resultFrame.pack(pady=20, padx=20, fill="both", expand=True)

resultLabel = tk.Label(
	resultFrame,
	text="",
	font=("Helvatica", 14),
	bg="white",
	fg="black",
	justify="left",
	anchor="nw",
	padx=10,
	pady=10
)

resultLabel.pack(fill="both", expand=True)

root.mainloop()
