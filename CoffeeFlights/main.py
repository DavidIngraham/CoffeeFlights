import time
import matplotlib.pyplot as plt
from CoffeeFlights.Radar import Radar

radar = Radar()

bounds = (33.465673, 33.4074764, -111.848405, -112.030175)  # NSEW Bounds

if __name__ == '__main__':

    while True:
        print('Updating:', time.ctime())
        radar.update_aircraft_list()
        plt.ion()

        for foo in range(0, 20):
            axes = plt.gca()
            axes.set_xlim([bounds[3], bounds[2]])
            axes.set_ylim([bounds[1], bounds[0]])
            radar.aircraft_list.interpolate_all()
            for plane in radar.aircraft_list:
                print(plane.call_sign, plane.lat, plane.lng, plane.alt_msl, plane.model)
                plt.scatter(plane.lng, plane.lat)
                plt.pause(0.001)

            plt.draw()
            plt.pause(.2)
            plt.clf()



