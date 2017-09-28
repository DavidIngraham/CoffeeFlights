from CoffeeFlights.AirCraft import AirCraft


class AirCraftList:
    """
    AirCraftList:

    Updates a list of aircraft objects from a python dictionary of VirtualRadarServer Responses

    Implements an iterator output so you can easily loop over all of the aircraft
    """
    def __init__(self, aircraft_list_dict):
        self.index = 0 # used for iterator
        self.aircraft_object_list = []
        for aircraft_dict in aircraft_list_dict:
            self.aircraft_object_list.append(AirCraft(aircraft_dict))

    def update(self, new_aircraft_list_dict):
        # Add any New AirCraft
        for new_aircraft_dict in new_aircraft_list_dict:
            new = True
            try:
                tail_number = new_aircraft_dict['Reg']
            except KeyError as e:
                # print(e)
                new = False
            else:
                for i in self.aircraft_object_list:
                    if i.tail_number == tail_number:
                        new = False
                        break
            if new:
                self.aircraft_object_list.append(AirCraft(new_aircraft_dict))
        # Update any aircraft already in list. Iterate backwards so we can delete planes that longer tracked
        for i in reversed(range(len(self.aircraft_object_list))):
            current = False
            # Iterate through all new data to check if the Tail number is still there
            for new_aircraft in new_aircraft_list_dict:
                try:
                    new_aircraft_tail_number = new_aircraft['Reg']
                except KeyError as e:
                    # print(e)
                    pass
                else:
                    if self.aircraft_object_list[i].tail_number == new_aircraft_tail_number:
                        current = True
                        self.aircraft_object_list[i].update(new_aircraft)
                        break
            if not current:
                del(self.aircraft_object_list[i])

    def interpolate_all(self):
        print(self.aircraft_object_list)
        for i in range(0, len(self.aircraft_object_list)):
            self.aircraft_object_list[i].interpolate_position()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.aircraft_object_list[self.index]
        except IndexError:
            self.index = 0
            raise StopIteration
        self.index += 1
        return result




