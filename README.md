# 📊 Google Play Analysis

An interactive web application for analyzing app data from the Google Play Store using Python, Dash, and Flask. It provides visual insights into trends, price comparisons, and other key metrics from the dataset.

## 📌 Features

- Interactive Dashboards and Charts
- Filtering by Category, Rating, Content Type, etc.
- Visual Comparison of App Trends
- Price and Popularity Analysis
- Responsive UI built with Dash

## 🧰 Tech Stack

- **Python**
- **Dash** for interactive web interfaces
- **Flask** as the backend server
- **Pandas & Plotly** for data manipulation and visualization

## 📁 Project Structure

├── app.py # Main entry point for the Dash/Flask app
├── assets/ # CSS and other static files
├── data/ # Dataset files (CSV, etc.)
├── components/ # Dash layout components (optional structure)
├── requirements.txt # Python dependencies
├── Procfile # For Render deployment
└── README.md # Project documentation


## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/katkaramruta64/google-play-analysis.git
cd google-play-analysis

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app locally
python app.py


