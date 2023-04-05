"""
Module to create markers for map
"""
import re
import folium


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

        except AttributeError:
            address = elem[0].split(',')[1][16:]

        distance = f"{round(elem[-1] * 1000)}m"
        folium.Marker([elemS[2], elemS[3]],
                      popup=folium.Popup(style.format(name=name, lt=elemS[2], ln=elemS[3],
                                                      address=address, distance=distance)),
                      icon=folium.features.CustomIcon(imagine, icon_size=(42, 40)), id=name).add_to(map_)
