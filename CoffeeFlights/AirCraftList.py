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
        # Add any valid New AirCraft unless they have a stale position
        for aircraft_dict in new_aircraft_list_dict:
            # Read the tail number
            tail_number = aircraft_dict.get('Reg')
            # Check if the tail number is present
            if tail_number is not None:
                # Check if it's in the list already, continue to the next if so, else, add it to the list
                for i in self.aircraft_object_list:
                    if i.tail_number == tail_number:
                        break
                else:
                    if not aircraft_dict.get('PosStale'):
                        self.aircraft_object_list.append(AirCraft(aircraft_dict))

        # Update any aircraft already in list. Iterate backwards so we can delete planes that longer tracked
        for i in reversed(range(len(self.aircraft_object_list))):
            # Iterate through all new data to check if the Tail number is still there
            for aircraft_dict in new_aircraft_list_dict:
                new_aircraft_tail_number = aircraft_dict.get('Reg')
                if new_aircraft_tail_number is not None:
                    if self.aircraft_object_list[i].tail_number == new_aircraft_tail_number:
                        self.aircraft_object_list[i].update(aircraft_dict)
                        break
                else:
                    # Break here to ensure that an aircraft isn't deleted when a bad key comes in
                    break
            else:
                del(self.aircraft_object_list[i])

    def interpolate_all(self):
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




