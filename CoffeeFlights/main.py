import time, threading
import matplotlib.pyplot as plt
from CoffeeFlights.Radar import Radar


radar = Radar()


bounds = (33.465673, 33.4074764, -111.848405, -112.030175)  # NSEW Bounds


def request_thread():
    while True:
        print('Updating:', time.ctime())
        radar.update_aircraft_list()
        for plane in radar.aircraft_list:
            print(plane.call_sign, plane.lat, plane.lng, plane.alt_msl, plane.model)
        time.sleep(1)


if __name__ == '__main__':
    updater = threading.Thread(target=request_thread)
    updater.start()
    plt.ion()

    while True:
        radar.aircraft_list.interpolate_all()
        plt.clf()
        axes = plt.gca()
        axes.set_xlim([bounds[3], bounds[2]])
        axes.set_ylim([bounds[1], bounds[0]])

        for plane in radar.aircraft_list:
            plt.scatter(plane.lng, plane.lat)
            plt.pause(0.0001)

        plt.draw()
        plt.pause(.5)




