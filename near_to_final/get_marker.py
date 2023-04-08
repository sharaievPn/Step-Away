"""
Module to create markers for map
"""
import re
import folium
from haversine import haversine


def parse_markers(marker_type, name: str, imagine: str, style, map_) -> None:
    """
    The func create markers for map
    :param map_: map for markers
    :param style: html
    :param marker_type: type of building
    :param name: name of type
    :param imagine: marker`s imagine
    :return: Nothing (add markers to map)
    """
    for elem in marker_type:
        elemS = elem[0].split(",")
        if 'пр.' in elem[0].split(',')[1]:
            pattern = r"вулиця|пр.\s+(\w+\s*\w*)\s*(\d+)"
        else:
            pattern = r"вулиця\s+(\w+\s*\w*)\s*(\d+)"
        try:
            address = re.search(pattern, elem[0].split(',')[1]).group(1) + \
                      '' + re.search(pattern, elem[0].split(',')[1]).group(2)
        except (AttributeError, TypeError):
            address = elem[0].split(',')[1][15:].replace('окільники', '').replace(")", '')
            if address.startswith('я'):
                address = address[1:]

        distance = f"{round(elem[-1] * 1000)}m"
        folium.Marker([elemS[2], elemS[3]], popup=folium.Popup(style.format(name=name, lt=elemS[2], ln=elemS[3],
                                                                            address=address, distance=distance)),
                      icon=folium.features.CustomIcon(imagine, icon_size=(42, 40)), id=name).add_to(map_)

    return None


def get_nearest_english(path: str, latitude: float, longitude: float) -> list:
    """
    The func get five nearest markers and get it to map
    :param longitude:
    :param latitude:
    :param path: path to file
    :return: Nothing
    >>> get_nearest_english('files/english_coord/pharmacy_enlish_coord', 49, 23)
    """
    res = []
    list_to_work = []
    with open(path, 'r', encoding='utf-8') as file:
        file = file.read().replace("\'", '').splitlines()
    for i in file:
        i = i.split(',')
        list_to_work.append(i)

    for row in list_to_work:
        data = row
        try:
            distance = haversine((latitude, longitude), (float(data[3]), float(data[4])))
        except IndexError:
            continue
        row += [distance]
        res += [row]

    return sorted(res, key=lambda x: x[5])[:5]


def parse_english_markers(marker_type, name: str, imagine: str, style, map_):
    """
    The func get five nearest markers and get it to map
    :param marker_type:
    :param name:
    :param imagine:
    :param style:
    :param map_:
    :return:
    # >>> pharmacy = get_nearest_english('files/english_coord/pharmacy_enlish_coord', 49, 23)
    # >>> parse_english_markers(pharmacy, '', '', '', '')
    """
    for i in marker_type:
        lt = i[3]
        lg = i[4]
        address_ = i[2].replace(')', '') + ' ' + i[1].replace('(', '').replace('" "', ' ')
        distance = f"{round(i[-1] * 1000)}m"

        folium.Marker([lt, lg], popup=folium.Popup(style.format(name=name, lt=lt, ln=lg,
                                                                address=address_, distance=distance)),
                      icon=folium.features.CustomIcon(imagine, icon_size=(42, 40)), id=name).add_to(map_)

    return None
