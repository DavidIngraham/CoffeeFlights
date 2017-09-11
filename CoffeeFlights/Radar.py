import requests, json
from CoffeeFlights.AirCraftList import AirCraftList
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
        self.radar_location = (33.4299930, -111.9348270, 1134)  # Lat/Lon/alt of virtual radar
        self.range = 50  # Max range filter, kilometers
        self.max_alt_agl = 1000
        response = self.get_radar_data()
        self.aircraft_list = AirCraftList(response['acList'])

    def get_radar_data(self):
        request_parameters = {
            'lat': str(self.radar_location[0]),
            'lng': str(self.radar_location[1]),
            'fDstL': 0,
            'fDstU': str(self.range),
            # 'fAirS': self.airport_string,  # Filter flights by airport code. Most flights don't seem to report this
            'fAltL': str(self.radar_location[2]),
            'fAltU': str(self.radar_location[2]+self.max_alt_agl)
        }
        response = requests.request('GET', RADAR_BASE_URL, params=request_parameters)
        return response.json()

    def update_aircraft_list(self):
        response = self.get_radar_data()
        self.aircraft_list.update(response['acList'])


