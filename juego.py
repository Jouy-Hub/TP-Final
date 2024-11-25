from track.track import Track
from car.car import Car
from car.player_car import PlayerCar
from car.auto_car import AutoCar
import pygame

#Hay que arreglar el menu
def get_player_name(num):
    """
    Pide al usuario ingresar un nombre, capturando la entrada de texto mediante pygame.
    Parametro:
    - num: numero que indica qué jugador es.
    Retorna:
    - input_text: El texto ingresado por el usuario.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 720))
    font = pygame.font.Font(None, 36)
    input_text = ""
    active = True
    clock = pygame.time.Clock()

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False  # Salir del bucle si se cierra la ventana
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Elimina el último carácter
                elif event.key == pygame.K_RETURN:
                    active = False  # Confirma el texto ingresado
                else:
                    input_text += event.unicode  # Añade el carácter presionado

        # Renderizado de la pantalla
        screen.fill((255, 255, 255))  # Fondo blanco

        # Imprimir "Ingrese nombre del jugador [num]:"
        instruction_text = font.render(f"Ingrese nombre del jugador {num}:", True, (150, 0, 150))
        screen.blit(instruction_text, (200, 250))  # Posición del texto de instrucción

        text_surface = font.render(input_text, True, (0, 0, 0))  # Texto ingresado en negro
        screen.blit(text_surface, (200, 300))  # Dibuja el texto ingresado en pantalla

        pygame.display.flip()  # Actualiza la pantalla
        clock.tick(30)

    pygame.quit()
    return input_text

def menu():
    """
    Muestra el menú del juego con tres opciones:
    - 1 Player: Solicita el nombre del jugador e inicia el juego contra la CPU.
    - 2 Players: Solicita los nombres de los jugadores y permite configurar un juego entre ambos o contra la CPU.
    - Quit: Cierra el juego.

    Retorna:
    - players: Lista con los nombres de los jugadores.
    - cpu: Booleano que indica si se juega contra la CPU.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 720))
    font = pygame.font.Font(None, 36)
    options = ["1 Player", "2 Players", "Quit"]
    selected = 0  # Índice de la opción seleccionada
    cpu = False
    players = []

    while True:
        screen.fill((255, 255, 255))  # Fondo blanco
        for index, option in enumerate(options):
            color = (0, 0, 0) if index != selected else (150, 0, 150)  # Resalta la opción seleccionada
            text_surface = font.render(option, True, color)
            screen.blit(text_surface, (340, 300 + index * 50))  # Dibuja las opciones en pantalla

        pygame.display.flip()  # Actualiza la pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None, None  # Termina el juego
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Mover flecha hacia arriba
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:  # Mover flecha hacia abajo
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:  # Enter
                    if selected == 0:  # 1 Player
                        name = get_player_name(1)
                        players = [name]
                        cpu = True
                        return players, cpu
                    elif selected == 1:  # 2 Players
                        name1 = get_player_name(1)
                        name2 = get_player_name(2)
                        players = [name1, name2]

                        # Preguntar si jugar contra la CPU
                        cpu_options = ["Yes", "No"]
                        cpu_selected = 0
                        while True:
                            screen.fill(255, 255, 255)  # Fondo blanco
                            question_text = font.render("¿Jugar contra la CPU?", True, (0, 0, 255))
                            screen.blit(question_text, (300, 250))
                            for idx, cpu_option in enumerate(cpu_options):
                                color = (0, 0, 0) if idx != cpu_selected else (150, 0, 150)
                                cpu_text = font.render(cpu_option, True, color)
                                screen.blit(cpu_text, (350, 300 + idx * 50))

                            pygame.display.flip()

                            for cpu_event in pygame.event.get():
                                if cpu_event.type == pygame.QUIT:
                                    pygame.quit()
                                    return None, None
                                if cpu_event.type == pygame.KEYDOWN:
                                    if cpu_event.key == pygame.K_UP:
                                        cpu_selected = (cpu_selected - 1) % len(cpu_options)
                                    elif cpu_event.key == pygame.K_DOWN:
                                        cpu_selected = (cpu_selected + 1) % len(cpu_options)
                                    elif cpu_event.key == pygame.K_RETURN:
                                        cpu = cpu_selected == 0  # "Yes" es CPU=True, "No" es CPU=False
                                        return players, cpu
                    elif selected == 2:  # Quit
                        pygame.quit()
                        return None, None

def terminal_menu()->tuple:
    """
    Muestra el menú del juego con tres opciones:
    - 1 Player: Solicita el nombre del jugador e inicia el juego contra la CPU.
    - 2 Players: Solicita los nombres de los jugadores y permite configurar un juego entre ambos o contra la CPU.
    - Quit: Cierra el juego.

    Retorna:
    - players: Lista con los nombres de los jugadores.
    - cpu: Booleano que indica si se juega contra la CPU.
    """
    jugadores=[]
    while len(jugadores) not in [1,2]:
        respuesta=input("Ingrese la cantidad de jugadores: ")
        if respuesta=="1":
            nombre=input("Ingrese el nombre del jugador: ")
            jugadores.append(nombre)

        elif respuesta == "2":
            nombre_1=input("Ingrese el nombre del jugador 1: ")
            jugadores.append(nombre_1)
            nombre_2=input("Ingrese el nombre del jugador 2: ")
            jugadores.append(nombre_2)

        else:
            print("Cantidad de jugadores invalida.")

    cpu_bool=True   
    if len(jugadores) == 2:
        cpu=input("Cpu si/no: ").lower()
        cpu_bool = False if cpu == "no" else True

    return jugadores,cpu_bool
    
# cpu decide teclas (retorna teclas)

def game(players:list,cpu:bool):
    pygame.init()
    screen = pygame.display.set_mode((800, 720))
    clock = pygame.time.Clock()
    dt=0
    running = True

    track = Track()
    starting_position=track.get_starting_position()
    starting_direction=track.get_starting_direction()
    
    cars=[]
    teclas_1 = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    distance_1=track.get_distances_car(starting_position,starting_direction)
    car_1=PlayerCar(players[0], 1,starting_position,starting_direction,distance_1)
    cars.append(car_1)

    if len(players)>1:
        teclas_2 = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
        distance_2=track.get_distances_car(starting_position,starting_direction)
        car_2=PlayerCar(players[1], 2, starting_position,starting_direction,distance_2)
        cars.append(car_2)
    
    if cpu:
        distance_cpu=track.get_distances_car(starting_position,starting_direction)
        car_cpu = AutoCar("CPU", 95,starting_position,starting_direction,distance_cpu)
        cars.append(car_cpu)

    
    while running:
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("green")

        # RENDER YOUR GAME HERE (Aca va el codigo de juego a actualizar en cada tick)
        exterior = list(track.track_polygon.exterior.coords)
        interior = list(track.track_polygon.interiors[0].coords)
        for tupla in range(len(exterior)-1):
            pygame.draw.line(screen, (0,0,0),exterior[tupla],exterior[tupla+1])
        for tupla in range(len(interior)-1):
            pygame.draw.line(screen, (0,0,0),interior[tupla],interior[tupla+1])
        
        #Printear linea de partida
        finish_line_coords = list(track.finish_line.coords)  # Convierte LineString a lista de puntos
        pygame.draw.line(screen, (255, 0, 0), (finish_line_coords[0][0], finish_line_coords[0][1]), (finish_line_coords[1][0], finish_line_coords[1][1]),3)

        #imprimir a Player 1
        pygame.draw.circle(screen,(50,50,50), car_1.get_position(), 5)

        #mover a player 1
        keys = pygame.key.get_pressed()
        p1_pressed_keys={"UP":False,"DOWN":False,"LEFT":False,"RIGHT":False}#las inicializo como no presionadas
        if keys[pygame.K_UP]:
            p1_pressed_keys["UP"]=True
        if keys[pygame.K_DOWN]:
            p1_pressed_keys["DOWN"]=True
        if keys[pygame.K_LEFT]:
            p1_pressed_keys["LEFT"]=True
        if keys[pygame.K_RIGHT]:
            p1_pressed_keys["RIGHT"]=True
        p1_inside_track= track.is_point_inside_track(car_1.get_position())
        acc_1,steer_1 = car_1.get_command(p1_pressed_keys, p1_inside_track)
        car_1.send_command(acc_1,steer_1)
        track.move_car(car_1)
        car_1.distances=track.get_distances_car(car_1.position,car_1.direction)




    # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(100)
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(100) / 1000
    pygame.quit()