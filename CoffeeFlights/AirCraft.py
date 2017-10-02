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
        self.tail_number = data.get('Reg')
        self.call_sign = data.get('Call')
        if self.call_sign is None:
            self.call_sign = self.tail_number
        self.lat_raw = float(data.get('Lat'))
        self.lng_raw = float(data.get('Long'))
        self.alt_msl = int(data.get('GAlt'))
        self.speed = data.get('Spd')
        self.track = int(data.get('Trak'))
        self.range_from_radar = float(data.get('Dst'))
        self.bearing_from_radar = float(data.get('Brng'))
        self.model = data.get('Mdl')
        self.timestamp = data.get('PosTime')/1000
        self.interpolated = self.interpolate_position()

    def interpolate_position(self):

        if None in [self.speed, self.track, self.timestamp, self.lat_raw, self.lng_raw] :
            self.lat, self.lng = self.lat_raw, self.lng_raw
            return False
        delta_t = (time.time() - self.timestamp)/3600  # hours
        delta_x = max(self.speed * delta_t, 0) # offset distance in nm

        # Get updated location using geopy lib
        reported_location = geopy.Point(latitude=self.lat_raw, longitude=self.lng_raw)
        offset_km = distance(nautical=delta_x)

        if offset_km.kilometers > 10:
            # If it's too unreasonable don't interpolate
            self.lat, self.lng = self.lat_raw, self.lng_raw
            return False

        updated_location = offset_km.destination(reported_location, self.track)
        self.lat = updated_location.latitude
        self.lng = updated_location.longitude
        return True

    def __repr__(self):
        return self.call_sign





