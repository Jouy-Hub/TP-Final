from car.car import Car
import math

class AutoCar(Car):
    def __init__(self, driver_name: str, car_number: int,movement_keys:list, position:list, direction:float,distances:list):#Agregue position y directtion para que se las pase a Car
        super().init(driver_name, car_number,movement_keys, position, direction,distances)

    def get_command(self, pygame_keys: dict, is_inside_track: bool) -> list[float]:#no uso pygame 
        """
        Returns the command for the car

        Args:
            pygame_keys (dict): The pygame keys
            is_inside_track (bool): Whether the car is inside the track

        Returns:
            list[float]: The command [acceleration, steering]
        """
        
        #el auto piensa aca, uso get_distance y decide que hacer
        left,right=self.distances

        if type(left) == float and type(right) == float and left<right and is_inside_track==True:
            steering= -math.radians(0.5)
        elif type(left) == float and type(right) == float and right<left and is_inside_track==True:
            steering=math.radians(0.5)

        elif type(left) == float and type(right) == float and is_inside_track==False and left<50 and right <50:
            steering=0
            acceleration=0

        elif type(left) == float and type(right) == float and is_inside_track==False and left>50 and right >50:
            steering=math.radians(0.5)

        elif type(left) == float and type(right) == float and is_inside_track==False and left>50 and right <50:
            steering= -math.radians(0.5)  

        elif type(left) == float and type(right) == float and is_inside_track==False and left<50 and right >50:
            steering= math.radians(0.5)     
        
        elif left == None and type(right)==float:
            steering= -math.radians(0.5)
        elif right== None and type(left)==float:
            steering=math.radians(0.5)


        
        elif left ==None and right == None:
            steering=-math.radians(0.5)
            acceleration=-0.0025
        
        else:
            steering=0


        if self.speed<0.025 and is_inside_track==True or (type(left) == float and type(right) == float and abs(right-left)<=0.3 and is_inside_track==True):
            acceleration=0.0025
        elif type(left) == float and type(right) == float and abs(right-left)>0.7 and is_inside_track==True:
            acceleration=-0.0025
        else:
            acceleration=0             

        #que hago con la bool (la posicion modifica la velocidad o la aceleracion?)

        return [acceleration, steering]
