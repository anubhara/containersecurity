# src/app.py
import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from werkzeug.urls import quote as url_quote

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page of the application
    """
    app_name = os.getenv('APP_NAME', 'Docker Best Practices Demo')
    return render_template('index.html', app_name=app_name)

@app.route('/health')
def health_check():
    """
    Health check endpoint for Docker
    """
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running correctly'
    }), 200

if __name__ == '__main__':
    # Get port from environment or default to 5000
    port = int(os.getenv('PORT', 5000))
    
    # Run the application
    app.run(
        host='0.0.0.0', 
        port=port, 
        debug=os.getenv('FLASK_DEBUG', 'False') == 'True'
    )
