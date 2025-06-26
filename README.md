# 🌤️ Mini Weather App

A simple full-stack weather application built with FastAPI and a custom HTML/CSS/JavaScript frontend. Users can search for any city and instantly view live weather conditions powered by the OpenWeatherMap API.
![image](https://github.com/user-attachments/assets/1cef5f2d-8a0a-44f7-8a9e-83ac0742fbb4)

---

## 🚀 Features

- 🔍 Search weather by city name
- 📡 Real-time temperature, highs/lows, and description
- 💻 Built with FastAPI (backend) and vanilla HTML/CSS/JS (frontend)
- 🌐 Clean, responsive layout based on Canva design
- 🧠 Organized code with modular Python logic and environment variables

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python, Uvicorn
- **Frontend**: HTML, CSS, JavaScript
- **API**: OpenWeatherMap
- **Environment Management**: `python-dotenv`
- **Version Control**: Git + GitHub

---

## 📦 Installation

### 1. Clone the repo:

```bash
git clone https://github.com/brimmt/weather-app.git
cd weather-app
2. Set up and run the backend:
bash - run in VS terminal
pip install -r requirements.txt
Then create a .env file in the root folder:
env
WEATHER_API_KEY=your_openweathermap_api_key


Run the backend:
bash
uvicorn main:app --reload

3. Use the frontend:
Open frontend/index.html in your browser.

Make sure the backend is running locally at http://127.0.0.1:8000 for the frontend to fetch weather data!

🧪 Example API Call
bash
GET /weather?city_name=Atlanta&units=imperial
Returns a JSON response with city name, temperature, highs/lows, and description.

🎯 Future Improvements
Add weather icons using OpenWeatherMap icons

Let users choose Celsius or Fahrenheit

Deploy backend with Railway and frontend with Netlify

Add Tailwind or Figma-designed UI

👩🏽‍💻 Built By

Tatiana Brimm
🧠 Health Informatics + Software Dev
🌐 Coming soon: tatianabrimm.com (portfolio)



