import collections
import heapq

# Since database is not used in this activity, I have used these dictionary to emulate a DB
AGE_VEHICLE=collections.defaultdict(list)
SLOT_CAR={}
AGE_SLOT=collections.defaultdict(list)


class ParkingLot:
    def __init__(self, size):
        self.size=size
        self.slots={}
        self.available_slots=[i for i in range(1, size+1)]
        heapq.heapify(self.available_slots)
        
    def clear_space(self, slot_num):
        heapq.heappush(self.available_slots,slot_num)
        car_number=SLOT_CAR[str(slot_num)]
        
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



class Vehicle:
    def __init__(self, vehicle_number, driver_age):
        self.vehicle_number=vehicle_number
        self.driver_age=driver_age
        
    def park(self, ParkingLotObj):
        if len(ParkingLotObj.available_slots)==0:
            print("No spaces available in our parking lot")
        
        slot_assigned=heapq.heappop(ParkingLotObj.available_slots)
        SLOT_CAR[str(slot_assigned)]=self.vehicle_number
        AGE_VEHICLE[str(self.driver_age)].append(self.vehicle_number)
        AGE_SLOT[str(self.driver_age)].append(str(slot_assigned))
        
        return slot_assigned
'''       
lot = ParkingLot(4)

vehicle1=Vehicle("jkfdsd", 23)
vehicle1.park(lot)
vehicle2=Vehicle("jkfdsfsd", 21)
vehicle2.park(lot)

print(AGE_VEHICLE)
print(SLOT_CAR)
print(AGE_SLOT)

lot.clear_space(1)

print(AGE_VEHICLE)
print(SLOT_CAR)
print(AGE_SLOT)

'''