import requests, json
RADAR_BASE_URL = 'https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json'
# Example Query String: ?lat=33.433638&lng=-112.008113&fDstL=0&fDstU=100


class Radar:
    """
    Virtual Radar Class:

    Provides an interface for requesting flight data from a Virtual Radar Server (http://www.virtualradarserver.co.uk/)
    We use ADSBExchange.com
    """

    def __init__(self):
        self.airport_string = 'KPHX'
        self.radar_location = (33.4299930, -111.9348270)  # Lat/Lon of virtual radar
        self.range = 100  # Max range filter, kilometers

    def get_radar_data(self):


        request_parameters = {
            'lat': str(self.radar_location[0]),
            'lng': str(self.radar_location[1]),
            'fDstL': 0,
            'fDstU': str(self.range),
            'fAirS': self.airport_string
        }

        response = requests.request('GET', RADAR_BASE_URL, params=request_parameters)
        radar_data = response.json()
        print(radar_data)

