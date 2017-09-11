
class AirCraft:
    """
    Aircraft class - Object intended for each aircraft in the airspace.
    """
    def __init__(self, data):
        self.dict = None
        self.tail_number = None
        self.lat = None
        self.lng = None
        self.alt_msl = None
        self.speed = None
        self.track = None
        self.range_from_radar = None
        self.bearing_from_radar = None
        self.update(data)

    def update(self, data):
        try:
            self.dict = data
            self.tail_number = data['Reg']
            self.lat = data['Lat']
            self.lng = data['Long']
            self.alt_msl = data['Alt']
            self.speed = None
            self.track = None
            self.range_from_radar = None
            self.bearing_from_radar = None
        except KeyError as e:
            print(e)

