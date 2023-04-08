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
        return render_template('main_ukrainian.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        print(lat, lng)
        return jsonify({'success': True})


@app.route('/ua/map', methods=['GET', 'POST'])
@app.route('/ua/map/', methods=['GET', 'POST'])
def introduce_ukrainian():
    if request.method == 'GET':
        lat = session.get('lat')
        lng = session.get('lng')
        script.create_map_ukrainian(lat, lng)
        return render_template('mapa_ukrainian.html')
    else:
        return 'yo'


@app.route('/en/')
@app.route('/en')
def home_english():
    if request.method == 'GET':
        return render_template('main_english.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        print(lat, lng)
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


@app.route('/ua/about-us/', methods=['GET'])
@app.route('/ua/about-us', methods=['GET'])
def about_us_ukrainian():
    return render_template('about_us_ukrainian.html')


@app.route('/en/about-us/', methods=['GET'])
@app.route('/en/about-us', methods=['GET'])
def about_us_english():
    return render_template('about_us_english.html')


@app.route('/ua/policies/', methods=['GET'])
@app.route('/ua/policies', methods=['GET'])
def policies_ukrainian():
    return render_template('policies_ukrainian.html')


@app.route('/en/policies/', methods=['GET'])
@app.route('/en/policies', methods=['GET'])
def policies_english():
    return render_template('policies_english.html')


@app.route('/ua/error/', methods=['GET'])
@app.route('/ua/error', methods=['GET'])
def error_ukrainian():
    return render_template('error_ukrainian.html')


@app.route('/en/error/', methods=['GET'])
@app.route('/en/error', methods=['GET'])
def error_english():
    return render_template('error_english.html')


if __name__ == '__main__':
    app.run(debug=True)
