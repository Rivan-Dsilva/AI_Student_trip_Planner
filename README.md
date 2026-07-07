# ✈️ AI Student Travel Planner 

A dynamic, budget-conscious travel itinerary generator built with **Python Streamlit** and powered by the **Google Gemini API (`gemini-2.5-flash`)**. This app creates optimized schedules tailored specifically for student budgets.

---

## 🌟 Features

- **Round-Trip Transit Math:** Automatically calculates separate departure and return fares based on your transit mode.
- **Geographically Clustered Timelines:** Curates exactly 4 local landmarks per day and calculates realistic transit costs between them.
- **Local Culinary Guides:** Recommends 3 regional meals a day (Breakfast, Lunch, Dinner) at iconic, pocket-friendly eateries.
- **Adaptive UI Dashboard:** Beautifully transitions between Dark and Light modes without breaking text readability.
- **Interactive Packing Checklist:** Generates a custom packing list tailored to your destination's weather and terrain.
- **Group Expense Splitter:** Dynamically splits lodging and local travel costs among friends.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/student_trip_planner.git
cd student_trip_planner
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser to start using the application.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit & Custom CSS
* **AI Core:** Google GenAI SDK (Gemini 2.5 Flash)
* **Data Format:** JSON

---

## 🔑 API Key

This repository **does not include a valid API key**.

To run the project:

1. Create a free account on **Google AI Studio**.
2. Generate your own API key.
3. Replace the placeholder in the code with your API key.

> **⚠️ Never commit your personal API key to a public GitHub repository.**
