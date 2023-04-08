"""
Module to generate map with the nearest objects
"""


import folium
from get_nearest import get_nearest
from get_marker import parse_markers, get_nearest_english, parse_english_markers


def create_map_ukrainian(latitude, longitude):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mark</title>
    <link rel="stylesheet" href="mark.css">
</head>
<body>
    <div class="mark" style= "width: 130px;
height: 75px;
background-color: rgb(4, 70, 36);
border-radius: 10px;
opacity: 85%;
display: flex;
flex-direction: column;
justify-content: space-between;
align-items: center;
flex-wrap: wrap;">
        <div class="mark1" style="width: 120px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark1" style="width: 120px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{address}</a>
        </div>
        <div class="mark2 d-flex justify-content-center" style = "width: 120px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark2 d-flex justify-content-center" style="width: 120px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{distance}</a>
        </div>
        <div class="mark3" style ="width: 120px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">
            <a href="https://www.google.com.ua/maps/place/{lt}%20{ln}" class="mark3" style ="width: 120px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">Знайти</a>
        </div>
    </div>
</body>
</html>"""
    m = folium.Map(location=[latitude, longitude], tiles="CartoDB Positron", zoom_start=15)
    fg = folium.FeatureGroup(name="SA creators map")
    fg.add_child(folium.Marker(location=[latitude, longitude],
                               icon=folium.features.CustomIcon('images/my_loc.png', icon_size=(52, 50)),
                               id='location', popup="Your location").add_to(fg))
    # marker_cluster = MarkerCluster().add_to(m)

    shelter = get_nearest('files/shelters_coor_ukrainian.csv', latitude, longitude)
    punkts = get_nearest('files/invicibility_coor_ukrainian.csv', latitude, longitude)
    police = get_nearest('files/police_coor_ukrainian.csv', latitude, longitude)
    hospitals = get_nearest('files/hospitals_coor_ukrainian.csv', latitude, longitude)
    pharmacy = get_nearest('files/apotheke_coor_ukrainian.csv', latitude, longitude)

    parse_markers(shelter, 'shelter', 'images/shelters.png', html, fg)
    parse_markers(punkts, 'punkts', 'images/punkts.png', html, fg)
    parse_markers(police, 'police', 'images/police.png', html, fg)
    parse_markers(hospitals, 'hospitals', 'images/hospitals.png', html, fg)
    parse_markers(pharmacy, 'pharmacy', 'images/pharmacy.png', html, fg)


    m.get_root().html.add_child(folium.Element("""
<style>
  .leaflet-top.leaflet-left{
    display: none;
  }
  #menu-box{
    position: absolute;
    z-index: 900;
    /*left: 40vw;
    top: 60vh;*/
    height: auto;
    width: auto;
  }
  #menu-box-information{
    position: fixed;
    width: 20vw;
    /*height: 25vh;*/
    height: auto;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  .menu-box-revealed{
    transform: translate3d(39.5vw, 60.5vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
  }
  .menu-box-hidden{
    transform: translate3d(39.5vw, 100vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    color: black;
    height: auto;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  .btn {
    display: flex;
    justify-content: center;
    align-items: center;
    --color: #ffff;
    --color2: rgb(10, 25, 30);
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    padding: 0.8em 1.75em;
    background-color: transparent;
    border-radius: 6px;
    border: .3px solid var(--color);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    margin: 1vh auto;
    z-index: 900;
    font-family: 'Roboto', 'Segoe UI', sans-serif;
    text-transform: uppercase;
    color: var(--color);
  }

  .btn::after, .btn::before {
    content: '';
    display: block;
    height: 100%;
    width: 100%;
    transform: skew(90deg) translate(-50%, -50%);
    position: absolute;
    inset: 50%;
    left: 25%;
    z-index: -1;
    transition: .5s ease-out;
    background-color: var(--color);
  }

  .btn::before {
    top: -50%;
    left: -25%;
    transform: skew(90deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::before {
    transform: skew(45deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::after {
    transform: skew(45deg) translate(-50%, -50%);
  }

  .btn:hover {
    color: var(--color2);
  }

  .btn:active {
    filter: brightness(.7);
    transform: scale(.98);
  }
  #arrow-up{
    position: absolute;
    z-index: 900;
    top: 80vh;
    left: 48vw;
  }

</style>
<script>
    function showCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-hidden');
    document.getElementById('menu-box').classList.add('menu-box-revealed');
    document.getElementById('arrow-up').style.display = 'none';
  }

  function hideCheckBoxesMenu(){
    document.getElementById('menu-box').classList.remove('menu-box-revealed');
    document.getElementById('menu-box').classList.add('menu-box-hidden');
    document.getElementById('arrow-up').style.display = 'block';
  }
</script>
    <div class="arrow-button-up">
      <svg onclick="showCheckBoxesMenu()" id="arrow-up" color="green" xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-arrow-up-circle" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M1 8a7 7 0 1 0 14 0A7 7 0 0 0 1 8zm15 0A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707V11.5z"/>
      </svg>
    </div>
    <div class="menu-box-hidden" id="menu-box">
      <div id="menu-scroller">
        <div id="menu-box-information">
          <label class="label">
            <span>Укриття</span>
            <input type="checkbox" id="checkbox1" class="check" name="shelter">
          </label>

          <label class="label">
            <span>Пункти незламності</span>
            <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
          </label>

          <label class="label">
            <span>Аптеки</span>
            <input type="checkbox" id="checkbox3" class="check" name="drugstore">
          </label>

          <label class="label">
            <span>Лікарні</span>
            <input type="checkbox" id="checkbox4" class="check" name="hospital">
          </label>
          <label class="label">
            <span>Поліція</span>
            <input type="checkbox" id="checkbox4" class="check" name="police_departments">
          </label>
          <div>
            <button onclick="hideCheckBoxesMenu() " type="submit" class ='btn'>Подати</button>
          </div>
        </div>
      </div>
    </div>
    """))
    m.add_child(fg)
    m.save('templates/mapa_ukrainian.html')


def create_map_english(latitude, longitude):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mark</title>
    <link rel="stylesheet" href="mark.css">
</head>
<body>
    <div class="mark" style= "width: 130px;
height: 75px;
background-color: rgb(4, 70, 36);
border-radius: 10px;
opacity: 85%;
display: flex;
flex-direction: column;
justify-content: space-between;
align-items: center;
flex-wrap: wrap;">
        <div class="mark1" style="width: 120px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark1" style="width: 120px;
    height: 12px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 25px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{address}</a>
        </div>
        <div class="mark2 d-flex justify-content-center" style = "width: 120px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">
            <a href="#" class="mark2 d-flex justify-content-center" style="width: 120px;
    height: 13px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-bottom: 15px;
    font-family: 'Times New Roman';
    text-decoration: none;
    padding: 2px;
    color: black;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 3px 0;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center;">{distance}</a>
        </div>
        <div class="mark3" style ="width: 120px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">
            <a href="https://www.google.com.ua/maps/place/{lt}%20{ln}" class="mark3" style ="width: 120px;
    height: 14px;
    background-color: white;
    border-radius: 10px;
    opacity: 80%;
    margin-top: 30px;
    font-family: 'Times New Roman';
    text-decoration: none;
    color: black;
    margin: 3px 0;
    padding: 1px;
    font-size: medium;
    display: flex; /* встановлюємо flex-контейнер */
    justify-content: center; /* вирівнюємо по горизонталі */
    align-items: center; /* вирівнюємо по вертикалі */
    text-decoration: underline;">Знайти</a>
        </div>
    </div>
</body>
</html>"""
    m = folium.Map(location=[latitude, longitude], tiles="CartoDB Positron", zoom_start=15)
    fg = folium.FeatureGroup(name="SA creators map")
    fg.add_child(folium.Marker(location=[latitude, longitude],
                               icon=folium.features.CustomIcon('images/my_loc.png', icon_size=(52, 50)),
                               id='location', popup="Your location").add_to(fg))

    shelter = get_nearest_english('files/english_coord/shelters_english_coord', latitude, longitude)
    punkts = get_nearest_english('files/english_coord/invisibly_english_coord', latitude, longitude)
    police = get_nearest_english('files/english_coord/police_english_coord', latitude, longitude)
    hospitals = get_nearest_english('files/english_coord/hospitals_english_coord', latitude, longitude)
    pharmacy = get_nearest_english('files/english_coord/pharmacy_enlish_coord', latitude, longitude)
    #
    parse_english_markers(shelter, 'shelter', 'images/shelters.png', html, fg)
    parse_english_markers(punkts, 'punkts', 'images/punkts.png', html, fg)
    parse_english_markers(police, 'police', 'images/police.png', html, fg)
    parse_english_markers(hospitals, 'hospitals', 'images/hospitals.png', html, fg)
    parse_english_markers(pharmacy, 'pharmacy', 'images/pharmacy.png', html, fg)

    m.get_root().html.add_child(folium.Element("""
    <style>
  #menu-box{
    position: absolute;
    z-index: 900;
  }
  #menu-box-information{
    position: fixed;
    width: 20vw;
    height: 25vh;
    z-index: 900;
    border: 1px solid black;
    background-color: #006e48;
    border-radius: 20px;
    opacity: 80%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 2vh;
    overflow-y: auto;
    overflow-x: hidden;
  }
  .menu-box-revealed{
    transform: translate3d(33vw, -30vh, 0);
    transition: transform 1.0s cubic-bezier(0, .52, 0, 1);
    overflow: auto;
    margin: center;
  }
  .menu-box-hidden{
    overflow: hidden;
    transform: translate3d(33vw, 100vh, 0);
    transition: transform 2.0s cubic-bezier(0, .52, 0, 1);
  }
  .label{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    min-width: 0;
    padding: 5px;
    background-color: #f8f8f8;
    margin: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
  }
  .check {
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 2px;
    appearance: none;
    background-color: #bbb;
    transition: all .3s;
  }

  .check::before {
    content: '';
    position: absolute;
    border: solid #fff;
    display: block;
    width: .3em;
    height: .6em;
    border-width: 0 .2em .2em 0;
    z-index: 1;
    opacity: 0;
    right: calc(50% - .3em);
    top: calc(50% - .6em);
    transform: rotate(0deg);
    transition: all .3s;
    transform-origin: center center;
  }

  .check:checked {
    animation: a .3s ease-in forwards;
    background-color: #00a97e;
  }

  .check:checked::before {
    opacity: 1;
    transform: rotate(405deg);
  }

  @keyframes a {
    0% {
      opacity: 1;
      transform: scale(1) rotateY(0deg);
    }

    50% {
      opacity: 0;
      transform: scale(.8) rotateY(180deg);
    }

    100% {
      opacity: 1;
      transform: scale(1) rotateY(360deg);
    }
  }
  .btn {
    display: flex;
    justify-content: center;
    align-items: center;
    --color: #ffff;
    --color2: rgb(10, 25, 30);
    font-size: 2vmin;
    transition: 1s;
    flex-grow: 1;
    padding: 0.8em 1.75em;
    background-color: transparent;
    border-radius: 6px;
    border: .3px solid var(--color);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    margin: 1vh auto;
    z-index: 900;
    font-family: 'Roboto', 'Segoe UI', sans-serif;
    text-transform: uppercase;
    color: var(--color);
  }

  .btn::after, .btn::before {
    content: '';
    display: block;
    height: 100%;
    width: 100%;
    transform: skew(90deg) translate(-50%, -50%);
    position: absolute;
    inset: 50%;
    left: 25%;
    z-index: -1;
    transition: .5s ease-out;
    background-color: var(--color);
  }

  .btn::before {
    top: -50%;
    left: -25%;
    transform: skew(90deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::before {
    transform: skew(45deg) rotate(180deg) translate(-50%, -50%);
  }

  .btn:hover::after {
    transform: skew(45deg) translate(-50%, -50%);
  }

  .btn:hover {
    color: var(--color2);
  }

  .btn:active {
    filter: brightness(.7);
    transform: scale(.98);
  }

</style>
    <div id="menu-box">
      <div id="menu-scroller">
        <div id="menu-box-information">
          <label class="label">
            <span>Укриття</span>
            <input type="checkbox" id="checkbox1" class="check" name="shelter">
          </label>

          <label class="label">
            <span>Пункти незламності</span>
            <input type="checkbox" id="checkbox2" class="check" name="unbreakpoint">
          </label>

          <label class="label">
            <span>Аптеки</span>
            <input type="checkbox" id="checkbox3" class="check" name="drugstore">
          </label>

          <label class="label">
            <span>Лікарні</span>
            <input type="checkbox" id="checkbox4" class="check" name="hospital">
          </label>
          <label class="label">
            <span>Поліція</span>
            <input type="checkbox" id="checkbox4" class="check" name="police_departments">
          </label>
          <div>
            <button type="submit" class ='btn'>Подати</button>
          </div>
        </div>
      </div>
    </div>
    """))
    m.add_child(fg)
    m.save('templates/map_eng.html')


create_map_ukrainian(50.2, 26.5)
