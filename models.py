import collections
import heapq

# Since database is not used in this activity, I have used these dictionary to emulate a DB
AGE_VEHICLE=collections.defaultdict(list) # age-> car_num (list) map
SLOT_CAR={} # slot_num-> car_num mapr
AGE_SLOT=collections.defaultdict(list) # age-> slot_num (list) map


class ParkingLot:
    # constructor for parking lot
    def __init__(self, size):
        self.size=size
        self.slots={}
        self.available_slots=[i for i in range(1, size+1)]
        heapq.heapify(self.available_slots) # use of heap/priority queue instead of normal list as it is more intuitive and offers better time complexity

    # free the parking slot
    def clear_space(self, slot_num):
        '''
        Frees the parking space and returns car_number and age of the driver.

        Parameters:
                slot_num (int): number of slot to be freed.
                self (ParkingLot): parking lot from where slot is being freed.

        Returns:
                car_number (str): vehicle registration number of the removed vehicle.
                age_key (str): age of the driver who is leaving the lot.
        '''
        try:
            # add the slot back to the heap
            heapq.heappush(self.available_slots,slot_num)
            car_number=SLOT_CAR[str(slot_num)]
            
            # remove slot_num from SLOT_CAR map
            del SLOT_CAR[str(slot_num)]
            
            # remove car_number from AGE_VEHICLE
            for key, values in AGE_VEHICLE.items():
                if str(car_number) in values:
                    age_key=key
                    vehicle_list=AGE_VEHICLE[str(age_key)]
                    vehicle_list=vehicle_list.remove(car_number)
                    AGE_VEHICLE[str(age_key)]=vehicle_list
            
            # remove slot_num from AGE_SLOT
            for key, values in AGE_SLOT.items():
                if str(slot_num) in values:
                    age_key=key
                    slot_list=AGE_SLOT[str(age_key)]
                    slot_list=slot_list.remove(str(slot_num))
                    AGE_SLOT[str(age_key)]=slot_list
                    
            return car_number,age_key
        
        except:
            # TODO make sure duplicates can't be pushed in the heap
            print("Space already not occupied")



class Vehicle:
    def __init__(self, vehicle_number, driver_age):
        self.vehicle_number=vehicle_number
        self.driver_age=driver_age

    # park the vehicle
    def park(self, ParkingLotObj):
        '''
        Parks the car in the parking lot and returns the slot assigned.

        Parameters:
                ParkingLotObj (ParkingLot): ParkingLot object where car is to be parked.
                self (Vehicle): Vehicle object to be parked.

        Returns:
                slot_assigned (int): slot number assigned to the vehicle.
        '''
        if len(ParkingLotObj.available_slots)==0:
            print("No spaces available in our parking lot")
            return -1
        
        else:
            slot_assigned=heapq.heappop(ParkingLotObj.available_slots)
            SLOT_CAR[str(slot_assigned)]=self.vehicle_number
            AGE_VEHICLE[str(self.driver_age)].append(self.vehicle_number)
            AGE_SLOT[str(self.driver_age)].append(str(slot_assigned))
            
            return slot_assigned
