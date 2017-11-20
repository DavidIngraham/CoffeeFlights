import requests
from json import JSONDecodeError
from CoffeeFlights.AirCraftList import AirCraftList
RADAR_BASE_URL = 'https://public-api.adsbexchange.com/VirtualRadar/AircraftList.json'
#RADAR_BASE_URL = 'http://n7uv.dyndns.org:9080/VirtualRadar/AircraftList.json'
#RADAR_BASE_URL = 'http://10.0.1.2:8080/VirtualRadar/AircraftList.json'



class Radar:
    """
    Virtual Radar Class:

    Provides an interface for requesting flight data from a Virtual Radar Server (http://www.virtualradarserver.co.uk/)
    We use ADSBExchange.com

    Docs: http://www.virtualradarserver.co.uk/Documentation/Formats/AircraftList.aspx
    """

    def __init__(self):
        self.airport_string = 'KPHX'
        self.radar_location = (33.4299930, -111.9348270, 1100)  # Lat/Lon/alt of virtual radar
        self.range = 50  # Max range filter, kilometers
        self.max_alt_agl = 3000
        self.bounds = (33.465673, 33.4074764, -111.848405, -112.030175)  # NSEW Bounds
        response = self.get_radar_data()
        self.aircraft_list = AirCraftList(response['acList'])

    def get_radar_data(self):
        request_parameters = {
            'lat': str(self.radar_location[0]),
            'lng': str(self.radar_location[1]),
            # 'fDstL': 0,
            # 'fDstU': str(self.range),
            # 'fAirS': self.airport_string,  # Filter flights by airport code. Most flights don't seem to report this
            'fAltL': str(self.radar_location[2]),
            'fAltU': str(self.radar_location[2] + self.max_alt_agl),
            'fNBnd': str(self.bounds[0]),
            'fSBnd': str(self.bounds[1]),
            'fEBnd': str(self.bounds[2]),
            'fWBnd': str(self.bounds[3])
        }
        response = requests.request('GET', RADAR_BASE_URL, params=request_parameters)
        try:
            return response.json()
        except JSONDecodeError:
            return None

    def update_aircraft_list(self):
        response = self.get_radar_data()
        #print response prints entire json message from server
        #print(response)
        if response is not None:
            self.aircraft_list.update(response['acList'])



