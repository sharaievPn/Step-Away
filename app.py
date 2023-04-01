from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from script import create_map


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = 1200  # Set lifespan to 20 minutes
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        return jsonify({'success': True})


@app.route('/map', methods=['GET', 'POST'])
def introduce():
    if request.method == 'GET':
        lat = session.get('lat')
        lng = session.get('lng')
        create_map(lat, lng)
        return render_template('map.html')
    else:
        return 'yo'

#
#
# @app.route('/no_perm')
# def introduce2():
#     return render_template('main_no_perm.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=22505)
