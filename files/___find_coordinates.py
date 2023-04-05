# from geopy.geocoders import Nominatim
# from geopy.extra.rate_limiter import RateLimiter
import googlemaps
import csv
import googlemaps.geocoding as geo
def read_file(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        csvreader = file.readlines()
        res = []
        for row in csvreader[1:]:
            elem = row.strip().split(",")
            row = elem[0] + ", " + "" + "м. Львів" + "" + elem[1]
            # print(row.split(","))
            res.append(row.split(","))
        return res
# print(read_file("координати/she.csv"))

def find_coor(res):
    lat = []
    lon = []
    # alls = []
    API_key = 'AIzaSyBg53v69eujkVTxN2nWrsQ-iLIsCH4NZcU'

    gmaps = googlemaps.Client(key=API_key)
    for el in res:
        location = geo.geocode(client=gmaps, address=el[1])
        try:
            location = location[0]['geometry']['location']
            lat.append(location['lat'])
            lon.append(location['lng'])
        except IndexError:
            continue

    with open('shelters_coor_ukrainian.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Address', 'Latitude', 'Longitude'])

        for i in range(len(res)):
            writer.writerow([res[i][0], res[i][1], lat[i], lon[i]])

res = read_file("координати/she.csv")
find_coor(res)
