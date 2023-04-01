import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", 'Flask-session'])
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = 1200  # Set lifespan to 20 minutes
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('main_trying.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        return jsonify({'success': True})


@app.route('/location', methods=['GET', 'POST'])
def save_location():
    if request.method == 'GET':
        lat = session.get('lat')
        lng = session.get('lng')
        return f"""<h1>Latitude is {lat}</h1>
                   <h1>Longitude is {lng}</h1>
                """
    else:
        return 'yo'
      
      
 if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=22505)
