
class AirCraft:
    """
    Aircraft class - Object intended for each aircraft in the airspace.

    API Documentation for JSON being parsed:
    http://www.virtualradarserver.co.uk/Documentation/Formats/AircraftList.aspx
    """
    def __init__(self, data):
        self.dict = None
        self.tail_number = None
        self.call_sign = None
        self.lat = None
        self.lng = None
        self.alt_msl = None
        self.speed = None
        self.track = None
        self.range_from_radar = None
        self.bearing_from_radar = None
        self.model = None
        self.update(data)

    def update(self, data):
        try:
            self.dict = data
            self.tail_number = data['Reg']
            self.call_sign = data['Call']
            self.lat = float(data['Lat'])
            self.lng = float(data['Long'])
            self.alt_msl = int(data['GAlt'])
            self.speed = int(data['Spd'])
            self.track = int(data['Trak'])
            self.range_from_radar = float(data['Dst'])
            self.bearing_from_radar = int(data['Brng'])
            self.model = data['Mdl']
        except KeyError as e:
            print(e)

