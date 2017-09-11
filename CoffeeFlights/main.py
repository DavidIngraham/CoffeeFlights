import time
from CoffeeFlights.Radar import Radar

radar = Radar()


if __name__ == '__main__':
    while True:
        radar.update_aircraft_list()
        print('Updating at', time.ctime())
        for plane in radar.aircraft_list:
            print(plane.tail_number)
        time.sleep(1)

