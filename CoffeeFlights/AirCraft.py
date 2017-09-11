
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
        def try_update(key):
            try:
                new_value = data[key]
            except KeyError as e:
                #print('This Stupid Plane Doesn\'t Tell Us About', e)
                new_value = None
            return new_value

        def try_update_int(key):
            try:
                new_value = int(data[key])
            except KeyError as e:
                #print('This Stupid Plane Doesn\'t Tell Us About', e)
                new_value = None
            return new_value

        def try_update_float(key):
            try:
                new_value = float(data[key])
            except KeyError as e:
                #print('This Stupid Plane Doesn\'t Tell Us About', e)
                new_value = None
            return new_value

        self.dict = data
        self.tail_number = try_update('Reg')
        self.call_sign = try_update('Call')
        self.lat = try_update_float('Lat')
        self.lng = try_update_float('Long')
        self.alt_msl = try_update_int('GAlt')
        self.speed = try_update_int('Spd')
        self.track = try_update_int('Trak')
        self.range_from_radar = try_update_float('Dst')
        self.bearing_from_radar = try_update_int('Brng')
        self.model = try_update('Mdl')



