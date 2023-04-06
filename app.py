from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_session import Session
import script


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = 1200  # Set lifespan to 20 minutes
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def starting_page():
    return redirect(url_for('home_ukrainian'))


@app.route('/ua/', methods=['GET', 'POST'])
@app.route('/ua', methods=['GET', 'POST'])
def home_ukrainian():
    if request.method == 'GET':
        return render_template('main_ukr.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        return jsonify({'success': True})


@app.route('/ua/map', methods=['GET', 'POST'])
@app.route('/ua/map/', methods=['GET', 'POST'])
def introduce_ukrainian():
    if request.method == 'GET':
        lat = session.get('lat')
        lng = session.get('lng')
        script.create_map_ukrainian(lat, lng)
        return render_template('map_ukr.html')
    else:
        return 'yo'


@app.route('/en/')
@app.route('/en')
def home_english():
    if request.method == 'GET':
        return render_template('main_eng.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        return jsonify({'success': True})


@app.route('/en/map')
@app.route('/en/map/')
def introduce_english():
    if request.method == 'GET':
        lat = session.get('lat')
        lng = session.get('lng')
        script.create_map_english(lat, lng)
        return render_template('map_eng.html')
    else:
        return 'yo'


@app.route('/ua/about-us/', method=['GET'])
@app.route('/ua/about-us', method=['GET'])
def about_us_ukrainian():
    render_template('about_us_ukr.html')


@app.route('/en/about-us/', method=['GET'])
@app.route('/en/about-us', method=['GET'])
def about_us_english():
    render_template('about_us_eng.html')


@app.route('/ua/policies/', method=['GET'])
@app.route('/ua/policies', method=['GET'])
def policies_ukrainian():
    render_template('policies_ukr.html')


@app.route('/en/policies/', method=['GET'])
@app.route('/en/policies', method=['GET'])
def policies_english():
    render_template('policies_eng.html')


@app.route('/ua/error/', methods=['GET'])
@app.route('/ua/error', methods=['GET'])
def error_ukrainian():
    return render_template('error_ukr.html')


@app.route('/en/error/', methods=['GET'])
@app.route('/en/error', methods=['GET'])
def error_english():
    return render_template('error_eng.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=22505)
