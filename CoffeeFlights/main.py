import time
from CoffeeFlights.Radar import Radar

radar = Radar()


if __name__ == '__main__':
    while True:
        radar.update_aircraft_list()
        print('Updating:', time.ctime())

        for plane in radar.aircraft_list:
            print(plane.call_sign, plane.lat, plane.lng, plane.alt_msl, plane.model)

        time.sleep(1)

