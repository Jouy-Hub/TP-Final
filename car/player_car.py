from car.car import Car
import math

class PlayerCar(Car):
    def __init__(self, driver_name: str, car_number: int, movement_keys: list, position:list, direction:float,distances:list):
        """
        Initializes the player car

        Args:
            driver_name (str): The name of the driver
            car_number (int): The number of the car
            movement_keys (list): The keys for the movement [up, down, left, right]. 
                                  Probably something like [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        """
        super().init(driver_name, car_number,movement_keys,position, direction,distances)
        self.movement_keys = movement_keys

    def get_command(self, pygame_keys, is_inside_track):#no hace falta inside track
        """
        Returns the command for the car

        Args:
            pygame_keys (dict): The pygame keys with bools (True for pressed, False for not pressed)
            is_inside_track (bool): Whether the car is inside the track

        Returns:
            list[float]: The command [acceleration, steering]
        """
        # baja la aceleracion si esta fuera de la pista
        if pygame_keys["UP"]==True and pygame_keys["DOWN"]==False:#para que no haya errores al apretar los dos
            acceleration=0.0025
        elif pygame_keys["DOWN"]==True and pygame_keys["UP"]==False:
            acceleration=-0.0025
        else: acceleration=0

        if pygame_keys["RIGHT"]==True and pygame_keys["LEFT"]==False:
            steering= math.radians(0.5)
        elif pygame_keys["LEFT"]==True and pygame_keys["RIGHT"]==False:
            steering=-math.radians(0.5)
        else:
            steering=0

        #que hago con la bool (la posicion modifica la velocidad o la aceleracion?)

        return [acceleration, steering]