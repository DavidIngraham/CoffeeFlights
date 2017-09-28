import time
import geopy
from geopy.distance import distance


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
        self.lat_raw = None
        self.lng_raw = None
        self.lat = None
        self.lng = None
        self.alt_msl = None
        self.speed = None
        self.track = None
        self.range_from_radar = None
        self.bearing_from_radar = None
        self.model = None
        self.timestamp = None
        self.interpolated = False
        self.update(data)

    def update(self, data):
        self.dict = data
        self.tail_number = self.try_update('Reg')
        self.call_sign = self.try_update('Call')
        if self.call_sign is None:
            self.call_sign = self.tail_number
        self.lat_raw = self.try_update_float('Lat')
        self.lng_raw = self.try_update_float('Long')
        self.alt_msl = self.try_update_int('GAlt')
        self.speed = self.try_update_int('Spd')
        self.track = self.try_update_int('Trak')
        self.range_from_radar = self.try_update_float('Dst')
        self.bearing_from_radar = self.try_update_int('Brng')
        self.model = self.try_update('Mdl')
        self.timestamp = self.try_update_float('PosTime')/1000
        self.interpolated = self.interpolate_position()

    def try_update(self, key):
        try:
            new_value = self.dict[key]
        except KeyError as e:
            new_value = None
        return new_value

    def try_update_int(self, key):
        try:
            new_value = int(self.dict[key])
        except KeyError as e:
            new_value = None
        return new_value

    def try_update_float(self, key):
        try:
            new_value = float(self.dict[key])
        except KeyError as e:
            new_value = None
        return new_value

    def interpolate_position(self):

        if None in [self.speed, self.track, self.timestamp, self.lat_raw, self.lng_raw] :
            self.lat, self.lng = self.lat_raw, self.lng_raw
            print("Can't Interpolate", self.call_sign)
            return False

        delta_t = (time.time() - self.timestamp)/3600  # hours
        delta_x = abs(self.speed * delta_t) # offset distance in nm

        # Get updated location using geopy lib
        reported_location = geopy.Point(latitude=self.lat_raw, longitude=self.lng_raw)
        offset_km = distance(nautical=delta_x)
        updated_location = offset_km.destination(reported_location, self.track)
        self.lat = updated_location.latitude
        self.lng = updated_location.longitude
        print("Interpolated", self.call_sign)

        return True

    def __repr__(self):
        return self.call_sign





