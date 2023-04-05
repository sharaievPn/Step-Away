from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import script


app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = 1200  # Set lifespan to 20 minutes
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/uk/', methods=['GET', 'POST'])
@app.route('/uk', methods=['GET', 'POST'])
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


@app.route('/uk/map', methods=['GET', 'POST'])
@app.route('/uk/map/', methods=['GET', 'POST'])
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


# @app.route('/uk/about-us/', method=['GET'])
# @app.route('/uk/about-us', method=['GET'])
# def about_us_ukrainian():
#     pass
#
#
# @app.route('/en/about-us/', method=['GET'])
# @app.route('/en/about-us', method=['GET'])
# def about_us_english():
#     pass
#
#
# @app.route('/uk/policies/', method=['GET'])
# @app.route('/uk/policies', method=['GET'])
# def policies_ukrainian():
#     pass
#
#
# @app.route('/en/policies/', method=['GET'])
# @app.route('/en/policies', method=['GET'])
# def policies_english():
#     pass
#
#
# @app.route('/uk/error/', method=['GET'])
# @app.route('/uk/error', method=['GET'])
# def error_ukrainian():
#     pass
#
#
# @app.route('/en/error/', method=['GET'])
# @app.route('/en/error', method=['GET'])
# def error_english():
#     pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=22505)
