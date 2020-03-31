import numpy as np


def lla_to_ecef_1(lat, lon, alt):
    # see http://www.mathworks.de/help/toolbox/aeroblks/llatoecefposition.html
    rad = np.float64(6378137.0)  # Radius of the Earth (in meters)
    f = np.float64(1.0 / 298.257223563)  # Flattening factor WGS84 Model
    cosLat = np.cos(lat)
    sinLat = np.sin(lat)
    FF = (1.0 - f) ** 2
    C = 1 / np.sqrt(cosLat ** 2 + FF * sinLat ** 2)
    S = C * FF

    x = (rad * C + alt) * cosLat * np.cos(lon)
    y = (rad * C + alt) * cosLat * np.sin(lon)
    z = (rad * S + alt) * sinLat
    return x, y, z


def lla_to_ecef_2(lat, lon, alt):
    import pyproj

    ecef = pyproj.Proj(proj="geocent", ellps="WGS84", datum="WGS84")
    lla = pyproj.Proj(proj="latlong", ellps="WGS84", datum="WGS84")
    x, y, z = pyproj.transform(lla, ecef, lon, lat, alt, radians=False)
    return x, y, z


coords = [
    (37.4001100556, -79.1539111111, 208.38),
    (37.3996955278, -79.153841, 208.48),
    (37.3992233889, -79.15425175, 208.18),
    (37.3989114167, -79.1532775833, 208.48),
    (37.3993285556, -79.1533773333, 208.28),
    (37.3992801667, -79.1537883611, 208.38),
    (37.3992441111, -79.1540981944, 208.48),
    (37.3992616389, -79.1539428889, 208.58),
    (37.3993530278, -79.1531711944, 208.28),
    (37.4001223889, -79.1538085556, 208.38),
    (37.3992922222, -79.15368575, 208.28),
    (37.3998074167, -79.1529132222, 208.18),
    (37.400068, -79.1542711389, 208.48),
    (37.3997516389, -79.1533794444, 208.38),
    (37.3988933333, -79.1534320556, 208.38),
    (37.3996279444, -79.154401, 208.58),
]

for lat, lon, alt in coords:
    print(lla_to_ecef_1(lat, lon, alt))
    print(lla_to_ecef_2(lat, lon, alt))
