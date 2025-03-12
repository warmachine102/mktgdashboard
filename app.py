# app.py
from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# --- Configuration ---
# Define the path to the data directory relative to app.py
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Set the template and static folder for Flask (optional as Flask defaults to 'templates' and 'static' in the same directory as app.py)
app.template_folder = TEMPLATE_FOLDER
app.static_folder = STATIC_FOLDER

# --- Routes ---
@app.route("/")
def dashboard():
    """
    Route for the main dashboard page.
    Renders the index.html template located in the /templates folder.
    """
    return render_template('index.html')

@app.route("/api/marketShare")
def get_market_share():
    """
    API endpoint to serve market share data.
    Reads data from marketShare.json and returns it as JSON.
    """
    try:
        filepath = os.path.join(DATA_DIR, 'marketShare.json')
        with open(filepath, 'r') as f:
            market_share_data = json.load(f)
        return jsonify(market_share_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

@app.route("/api/revenueTrends")
def get_revenue_trends():
    """
    API endpoint to serve revenue trends data.
    Reads data from revenueTrends.json and returns it as JSON.
    """
    try:
        filepath = os.path.join(DATA_DIR, 'revenueTrends.json')
        with open(filepath, 'r') as f:
            revenue_trends_data = json.load(f)
        return jsonify(revenue_trends_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

@app.route("/api/marketSegmentation")
def get_market_segmentation():
    """
    API endpoint to serve market segmentation data.
    Reads data from marketSegmentation.json and returns it as JSON.
    """
    try:
        filepath = os.path.join(DATA_DIR, 'marketSegmentation.json')
        with open(filepath, 'r') as f:
            market_segmentation_data = json.load(f)
        return jsonify(market_segmentation_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

# --- Static Files Serving (Optional - Flask automatically serves from 'static' folder) ---
# If you have files in the /static folder (e.g., CSS, additional JS, images),
# Flask will serve them automatically.
# You can access them in your HTML like: <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">

# --- Run the Flask App ---
if __name__ == '__main__':
    app.run(debug=True) # Set debug=False in production


# --- Recommended Repository Structure ---
"""
Recommended GitHub Repository Structure for the Market Analysis Dashboard Project:

Project Root (e.g., market-analysis-dashboard/)
├── app.py                # Flask application file
├── templates/            # HTML templates
│   └── index.html        # Main dashboard HTML file
├── data/               # JSON data files
│   ├── marketShare.json
│   ├── revenueTrends.json
│   └── marketSegmentation.json
├── static/             # Static assets (optional, e.g., CSS, images, additional JS)
│   └── ( ... your static files here ... )
├── README.md             # Project README file (optional but recommended)
└── requirements.txt      # Project dependencies (if you use external libraries beyond Flask and standard Python libraries)

Explanation:
- Project Root:  The main directory of your project, named appropriately (e.g., market-analysis-dashboard).
- app.py: Contains the Flask application code to run the dashboard.
- templates/:  Holds the HTML template files for your web application. 'index.html' is the main dashboard page.
- data/: Stores the JSON data files that your Flask app will serve to the dashboard. Keeping data separate makes the project organized.
- static/:  For any static files like CSS stylesheets, JavaScript files (other than D3.js which is loaded from CDN), images, etc. This is where you would put files that are served directly to the browser without server-side processing.
- README.md: (Optional) A good practice to include a README file in your repository to describe your project, how to set it up, run it, etc.
- requirements.txt: (Optional) If your Flask app depends on any Python packages not in the standard library (although in this case it mostly relies on Flask itself), list them in this file so others can easily install them using 'pip install -r requirements.txt'.

This structure clearly separates the different components of your web application: backend logic (app.py), frontend templates (templates/), data (data/), and static assets (static/), making the project easier to manage, understand, and maintain.
"""
