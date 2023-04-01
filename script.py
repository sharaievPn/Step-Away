"""
Module to create map with the nearest location
"""


import folium
from get_nearest import get_nearest


def create_map(latitude, longitude):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mark</title>
        <link rel="stylesheet" href="mark.css">
        <style>
        * {
    margin: 0;
    padding: 0;
    font-family: 'Times New Roman', Times, serif;
}

.mark {
    width: 130px;
    height: 75px;
    background-color: rgb(4, 70, 36);
    border-radius: 10px;
    opacity: 85%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap; 
}

.mark1 {
    width: 120px;
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
    align-items: center; /* вирівнюємо по вертикалі */
}

.mark2 {
    width: 120px;
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
    align-items: center; /* вирівнюємо по вертикалі */
}

.mark3 {
    width: 120px;
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
    text-decoration: underline;
}
 
    </style>
    </head>
    <body>
        <div class="mark">
            <div class="mark1">
                <a href="#" class="mark1">Адреса</a>
            </div>
            <div class="mark2 d-flex justify-content-center">
                <a href="#" class="mark2 d-flex justify-content-center">{{ name }}</a>
            </div>
            <div class="mark3">
                <a href="https://www.google.com.ua/maps/place/{{ latitude }}%20{{ longitude }}" class="mark3">Google maps</a>
            </div>
        </div>
    </body>
    </html>
    """
    m = folium.Map(location=[latitude, longitude], tiles="Stamen Terrain", zoom_start=15)
    fg = folium.FeatureGroup(name="SA creators map")
    fg.add_child(folium.Marker(location=[latitude, longitude],
                               popup="во хата",
                               icon=folium.Icon()))
    # marker_cluster = MarkerCluster().add_to(m)

    shelter = get_nearest('files/shelters_cor.csv', latitude, longitude)

    punkts = get_nearest('files/invicibility_coordinates.csv', latitude, longitude)

    police = get_nearest('files/police_coordinates.csv', latitude, longitude)

    hospitals = get_nearest('files/hospitals_coordinates.csv', latitude, longitude)

    pharmacy = get_nearest('files/apotheke_coor.csv', latitude, longitude)

    for elem in shelter:
        elemS = elem[0].split(",")
        lt = elemS[2]
        ln = elemS[3]
        folium.Marker([lt, ln], popup=folium.Popup(html, name='shelter', latitude=lt, longitude=ln),
                      icon=folium.features.CustomIcon('images/shelters.png'), id='shelter').add_to(fg)

    for elem in punkts:
        elemS = elem[0].split(",")
        lt = elemS[2]
        ln = elemS[3]
        folium.Marker([lt, ln], popup=folium.Popup(html), icon=folium.features.CustomIcon('images/punkts.png'),
                      id='punkts').add_to(fg)

    for elem in police:
        elemS = elem[0].split(",")
        lt = elemS[2]
        ln = elemS[3]
        folium.Marker([lt, ln], popup=folium.Popup(html), icon=folium.features.CustomIcon('images/police.png'),
                      id='police').add_to(fg)

    for elem in hospitals:
        elemS = elem[0].split(",")
        lt = elemS[2]
        ln = elemS[3]
        folium.Marker([lt, ln], popup=folium.Popup(html), icon=folium.features.CustomIcon('images/hospitals.png'),
                      id='hospitals').add_to(fg)

    for elem in pharmacy:
        elemS = elem[0].split(",")
        lt = elemS[2]
        ln = elemS[3]
        folium.Marker([lt, ln], popup=folium.Popup(html), icon=folium.features.CustomIcon('images/pharmacy.png'),
                      id='pharmacy').add_to(fg)
    m.get_root().html.add_child(folium.Element("""
    <div id='menu' style="
          position: fixed;
          top: 10px; left: 70px; width: 150px; height: 10px;
          width: 200px;
          z-index: 900;
          height: 200px;
          border: 1px solid black;
          background-color: #006e48;
          border-radius: 20px;
          opacity: 90%;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          align-items: center;
          padding: 10px;">
        <label style="display: flex;
          justify-content: space-between;
          align-items: center;
          border-radius: 10px;
          width: 100%;
          margin-right: 10px;
          padding: 5px;
          background-color: #f6f2f2;
          margin: 2px 0;">
          <span>Укриття</span>
          <input type="checkbox" id="checkbox1" name = shelter>
        </label>

        <label style="display: flex;
          justify-content: space-between;
          align-items: center;
          border-radius: 10px;
          width: 100%;
          margin-right: 10px;
          padding: 5px;
          background-color: #f6f2f2;
          margin: 2px 0;">
          <span>Пункти незламності</span>
          <input type="checkbox" id="checkbox2" name = unbreakpoint>
        </label>

        <label style="display: flex;
          justify-content: space-between;
          align-items: center;
          border-radius: 10px;
          width: 100%;
          margin-right: 10px;
          padding: 5px;
          background-color: #f6f2f2;
          margin: 2px 0;">
          <span>Аптеки</span>
          <input type="checkbox" id="checkbox3" name = drugstore>
        </label>

        <label style="display: flex;
          justify-content: space-between;
          align-items: center;
          border-radius: 10px;
          width: 100%;
          margin-right: 10px;
          padding: 5px;
          background-color: #f6f2f2;
          margin: 2px 0;">
          <span>Лікарні</span>
          <input style="margin-left: 10px;
          border: 1px solid gray;
          padding: 5px;" type="checkbox" id="checkbox4" name = hospital>
        </label>
        <button type="submit">Подати</button>
    </div>
    """))
    m.add_child(fg)
    m.save('templates/map.html')
