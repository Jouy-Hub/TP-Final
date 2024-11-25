from car.car import Car

class AutoCar(Car):
    def __init__(self, driver_name: str, car_number: int, position:list, direction:float,distances:list):#Agregue position y directtion para que se las pase a Car
        super().init(driver_name, car_number, position, direction,distances)

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
        
        pass
