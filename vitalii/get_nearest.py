"""
Additional module to script.py
Calculates the nearest lcoation
"""


from haversine import haversine


def get_nearest(path: str, latitude: float, longitude: float) -> list:
    """
    The function do something
    """
    res = []
    with open(path, 'r') as file_:
        file_ = file_.read()
        file_ = file_.split('\n')[1:]
        for row in file_:
            data = row.split(',')
            try:
                distance = haversine((latitude, longitude), (float(data[2]), float(data[3])))
            except IndexError:
                continue
            res.append([row, distance])

    res = sorted(res, key=lambda distance: distance[1])
    return res[:5]
