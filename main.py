from models import ParkingLot, AGE_SLOT, AGE_VEHICLE, SLOT_CAR, Vehicle

if __name__ == "__main__":
    
    output_file="output.txt"
    read_input=open("input.txt", "r")
    writer = open(output_file, "w")
    
    lines = read_input.readlines()

    for i in lines:
        #print (i)
        i=i.replace("\n", "")
        steps = i.split(" ")
        print (steps)
        
        if len(steps)==2:
            if steps[0]=='Create_parking_lot':
                lot = ParkingLot(int(steps[1]))
                output_line= f"Creating parking of {steps[1]} slots \n"
                
            if steps[0]=='Leave':
                car, age=lot.clear_space(int(steps[1]))
                output_line= f"Slot number {steps[1]} vacated, the car with vehicle registration number {car} left the space, the driver of the car was of age {age} \n"

            if steps[0]=='Slot_numbers_for_driver_of_age':
                output_slots=AGE_SLOT[str(steps[1])]
                output_slots = list(map(int, output_slots)) 
                output_line=str(output_slots)[1:-1]   + "\n"
                
            if steps[0]=='Vehicle_registration_number_for_driver_of_age':
                print(AGE_VEHICLE)
                output_cars=AGE_VEHICLE[str(steps[1])] 
                output_line=str(output_cars) + "\n"
                print(AGE_VEHICLE[str(199)])
                
            if steps[0]=='Slot_number_for_car_with_number':
                for key, value in SLOT_CAR.items():
                    if value==steps[1]:    
                        #output_slots=AGE_SLOT[str(steps[1])]
                        output_line=str(key)  + "\n"
                
                                
                
            
        
        elif len(steps)==4:
            task=steps[0]
            car_number=steps[1]
            driver_age=steps[3]
            
            if task =="Park":
                vehicle=Vehicle(car_number, int(driver_age))
                slot_assigned=vehicle.park(lot)
                output_line= f"Car with vehicle registration number {car_number} has been parked at slot number {slot_assigned} \n"
                
            
        print(output_line)
        writer.write(output_line)
            