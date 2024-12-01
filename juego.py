from track.track import Track
from car.player_car import PlayerCar
from car.auto_car import AutoCar
import pygame
import random
import math

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((900, 820))
    clock = pygame.time.Clock()
    running = True
    menu=True
    sub_menu=False

    menu_BG= pygame.image.load("Menu_BG_2.jpg")
    menu_BG = pygame.transform.scale(menu_BG, (900, 820))

    track = Track(x_max=900,y_max=820,margin_x=200,margin_y=200)
    starting_position=track.get_starting_position()
    starting_direction=track.get_starting_direction()
    BG= pygame.image.load("Background_2.jpg")
    BG = pygame.transform.scale(BG, (900, 820))
    finish_line=pygame.image.load("finish_line.png")
    finish_line=pygame.transform.scale(finish_line,(30,10))

    pygame.mixer.music.load("EZ Rollers - Breakbeat Generation (Instrumental).mp3")
    win_sound_effect = pygame.mixer.Sound("Final Fantasy I ost - Victory.mp3")
    lap_sound_effect = pygame.mixer.Sound("Lap_audio.mp3")
    sound_played = False

    wood_plank= pygame.image.load("wood_plank.png")
    wood_plank = pygame.transform.scale(wood_plank, (320, 105))
    wood_plank_menu=pygame.image.load("small_wood_plank.png")
    wood_plank_menu = pygame.transform.scale(wood_plank_menu, (300, 100))
    win_BG= pygame.image.load("Winner.png")
    win_BG=pygame.transform.scale(win_BG, (900, 820))
    
    cars=[]
    teclas_1 = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    distance_1=track.get_distances_car(starting_position,starting_direction)
    car_1=PlayerCar('player 1', 1,teclas_1,starting_position,starting_direction,distance_1)
    vueltas_1=0
    cars.append(car_1)
    random_car1=random.randint(1,3)
    if random_car1==1: p1_sprite= pygame.image.load("P1_Sprite.png")
    elif random_car1==2: p1_sprite= pygame.image.load("P1_Sprite_2.png")
    else: p1_sprite= pygame.image.load("P1_Sprite_3.png")
    p1_sprite = pygame.transform.scale(p1_sprite, (30, 40))

    teclas_2 = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]
    distance_2=track.get_distances_car(starting_position,starting_direction)
    car_2=PlayerCar('player 2', 2, teclas_2, starting_position,starting_direction,distance_2)
    vueltas_2=0
    cars.append(car_2)
    random_car2=random.randint(1,3)
    if random_car2==1: p2_sprite= pygame.image.load("P2_Sprite.png")
    elif random_car2==2: p2_sprite= pygame.image.load("P2_Sprite_2.png")
    else: p2_sprite= pygame.image.load("P2_Sprite_3.png")
    p2_sprite = pygame.transform.scale(p2_sprite, (30, 40))

    distance_cpu=track.get_distances_car(starting_position,starting_direction)
    teclas_cpu=[]
    car_cpu = AutoCar("CPU", 95,teclas_cpu,starting_position,starting_direction,distance_cpu)
    vueltas_cpu=0
    cars.append(car_cpu)
    cpu_sprite= pygame.image.load("El_Rayo_Sprite.png")
    cpu_sprite = pygame.transform.scale(cpu_sprite, (45, 45))

    font_menu = pygame.font.Font(None, 36)
    options = ["1 Player", "2 Players"]
    options_2=['CPU: YES','CPU: NO']
    cpu = False
    players = []
    selected = 0
    selected_2=0
    enter_pressed=False
    win=False
    
    while running:
        keys = pygame.key.get_pressed()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #menu
        if menu and sub_menu==False and win == False:
            screen.blit(menu_BG, (0, 0))
            wood_plank_menu_rect = wood_plank_menu.get_rect(center=((900//2), 820//2+30-150))
            screen.blit(wood_plank_menu, wood_plank_menu_rect)
            for index, option in enumerate(options):
                color = (0, 0, 0) if index != selected else (251, 255, 163)
                text_surface = font_menu.render(option, False, color)
                tx_menu_rect = text_surface.get_rect(center=((900//2), 820//2-150 + index * 50))
            
                screen.blit(text_surface, (tx_menu_rect))
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = 0
                elif event.key == pygame.K_DOWN:
                    selected = 1
                elif event.key == pygame.K_RETURN:  # Detectar ENTER presionado
                    enter_pressed = True 
        
            if event.type == pygame.KEYUP:  # Detectar cuando ENTER es liberado
                if event.key == pygame.K_RETURN and enter_pressed:
                    enter_pressed = False  # Resetear el estado de ENTER
                    if selected == 0:
                        players = ['Player 1']
                        cpu = True
                        menu = False
                        sub_menu = False
                    elif selected == 1:
                        players = ['Player 1', 'Player 2']
                        sub_menu = True
                        menu=False
        #sub-menu
        if sub_menu and menu==False and win == False:
            screen.blit(menu_BG, (0, 0))
            wood_plank_menu_rect = wood_plank_menu.get_rect(center=((900//2), 820//2+30-150))
            screen.blit(wood_plank_menu, wood_plank_menu_rect)
            for index_2, option_2 in enumerate(options_2):
                color = (0, 0, 0) if index_2 != selected_2 else (251, 255, 163)
                text_surface_2 = font_menu.render(option_2, False, color)
                tx_sub_menu_rect = text_surface.get_rect(center=((900//2), 820//2-150 + index_2 * 50))
                screen.blit(text_surface_2, tx_sub_menu_rect)
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_2 = 0
                elif event.key == pygame.K_DOWN:
                    selected_2 = 1
                elif event.key == pygame.K_RETURN:  # Detectar ENTER en el submenú
                    enter_pressed = True
        
            if event.type == pygame.KEYUP:  # Detectar cuando ENTER es liberado (para evitar que tome el anterior)
                if event.key == pygame.K_RETURN and enter_pressed:
                    enter_pressed = False
                    if selected_2 == 0: 
                        cpu = True
                        sub_menu = False
                    elif selected_2 == 1:
                        cpu = False
                        sub_menu = False
        
        # gameplay
        elif menu==False and sub_menu==False and win==False:            
    
            screen.fill((0,102,51))

            exterior = list(track.track_polygon.exterior.coords)
            interior = list(track.track_polygon.interiors[0].coords)

            screen.blit(BG, (0,0))

            screen.blit(wood_plank, (10,10))

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(loops=-1)

            #Pintar pista
            pygame.draw.polygon(screen, (228,190,110), interior + exterior[::-1], 0)

            for tupla in range(len(exterior)-1):
                pygame.draw.line(screen, (0,0,0),exterior[tupla],exterior[tupla+1])
            for tupla in range(len(interior)-1):
                pygame.draw.line(screen, (0,0,0),interior[tupla],interior[tupla+1])

            #Printear linea de meta
            finish_line_coords = list(track.finish_line.coords)
    
            angle_fl=math.degrees(track.get_starting_direction())
            rotated_sprite_fl = pygame.transform.rotate(finish_line,-angle_fl -90)
            sprite_rect_fl = rotated_sprite_fl.get_rect(center=((finish_line_coords[1][0]+finish_line_coords[0][0])/2,(finish_line_coords[0][1]+ finish_line_coords[1][1])/2)) #resto
            screen.blit(rotated_sprite_fl, sprite_rect_fl)

            #imprimir Players
            angle_1 = math.degrees(car_1.direction) 
            rotated_sprite_1 = pygame.transform.rotate(p1_sprite, -angle_1+90) 
            sprite_rect_1 = rotated_sprite_1.get_rect(center=car_1.get_position())
            screen.blit(rotated_sprite_1, sprite_rect_1.topleft)

            if len(players)>1:
                angle_2 = math.degrees(car_2.direction)
                rotated_sprite_2 = pygame.transform.rotate(p2_sprite, -angle_2+90)
                sprite_rect_2 = rotated_sprite_2.get_rect(center=car_2.get_position())
                screen.blit(rotated_sprite_2, sprite_rect_2.topleft)

            if cpu:
                angle_cpu = math.degrees(car_cpu.direction) 
                rotated_sprite_cpu = pygame.transform.rotate(cpu_sprite, -angle_cpu-90) 
                sprite_rect_cpu = rotated_sprite_cpu.get_rect(center=car_cpu.get_position())
                screen.blit(rotated_sprite_cpu, sprite_rect_cpu.topleft)


            #mover jugadores
            p1_pressed_keys={"UP":False,"DOWN":False,"LEFT":False,"RIGHT":False}
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

            if len(players)>1:
                p2_pressed_keys={"UP":False,"DOWN":False,"LEFT":False,"RIGHT":False}
                if keys[pygame.K_w]:
                    p2_pressed_keys["UP"]=True
                if keys[pygame.K_s]:
                    p2_pressed_keys["DOWN"]=True
                if keys[pygame.K_a]:
                    p2_pressed_keys["LEFT"]=True
                if keys[pygame.K_d]:
                    p2_pressed_keys["RIGHT"]=True
                p2_inside_track= track.is_point_inside_track(car_2.get_position())
                acc_2,steer_2 = car_2.get_command(p2_pressed_keys, p2_inside_track)
                car_2.send_command(acc_2,steer_2)
                track.move_car(car_2)
                car_2.distances=track.get_distances_car(car_2.position,car_2.direction)

            if cpu:
                cpu_inside_track= track.is_point_inside_track(car_cpu.get_position())
                acc_cpu,steer_cpu = car_cpu.get_command(0, cpu_inside_track)
                car_cpu.send_command(acc_cpu,steer_cpu)
                track.move_car(car_cpu)
                car_cpu.distances=track.get_distances_car(car_cpu.position,car_cpu.direction)

            # Mostrar vueltas y velocidad en pantalla
            font_ls = pygame.font.Font(None, 28)
            laps_text = font_ls.render(f"{players[0]}: {vueltas_1} laps, Speed: {car_1.speed:.2f}", False, (0, 0, 0))
            screen.blit(laps_text, (25, 20))

            if len(players) > 1:
                laps_text_2 = font_ls.render(f"{players[1]}: {vueltas_2} laps, Speed: {car_2.speed:.2f}", False, (0, 0, 0))
                screen.blit(laps_text_2, (25, 50))

            if cpu:
                laps_text_cpu = font_ls.render(f"El Rayo : {vueltas_cpu} laps, Speed: {car_cpu.speed:.2f}", False, (0, 0, 0))
                screen.blit(laps_text_cpu, (25, 80))

            #Conteo de vueltas
            lap_1= track.check_lap([car_1.last_position,car_1.position])
            if len(players)>1:
                lap_2=track.check_lap([car_2.last_position,car_2.position])
            if cpu:
                lap_cpu=track.check_lap([car_cpu.last_position,car_cpu.position])

            if lap_1:
                vueltas_1+=1
                lap_sound_effect.play()

            if len(players)>1 and lap_2:
                vueltas_2+=1
                lap_sound_effect.play()

            if cpu and lap_cpu:
                vueltas_cpu+=1
                lap_sound_effect.play()

            if vueltas_1==3:
                win=True

            if len(players)>1 and vueltas_2==3:
                win=True

            if cpu and vueltas_cpu==3:
                win=True
        
        #pantalla de ganador
        elif win == True and menu == False and sub_menu == False:
            screen.blit(win_BG, (0,0))
            if not sound_played:
                win_sound_effect.play()
            sound_played = True
            if vueltas_1==3:
                pygame.mixer.music.stop()
                font_win = pygame.font.Font(None, 100)
                text_win=font_win.render(f'Player 1 wins!',False,(24, 21, 38))
                text_win_rect = text_win.get_rect(center=((900//2), 820//2+300))
                screen.blit(text_win,text_win_rect)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running=False
            elif vueltas_2==3:
                pygame.mixer.music.stop()
                font_win = pygame.font.Font(None, 100)
                text_win=font_win.render(f'Player 2 wins!',False,(63, 11, 57))
                text_win_rect = text_win.get_rect(center=((900//2), 820//2+300))
                screen.blit(text_win,text_win_rect)

                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RETURN:
                        running=False
            elif vueltas_cpu==3:
                pygame.mixer.music.stop()
                font_win = pygame.font.Font(None, 100)
                text_win=font_win.render(f'El Rayo wins!',False,(63, 11, 57))
                text_win_rect = text_win.get_rect(center=((900//2), 820//2+300))
                screen.blit(text_win,text_win_rect)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running=False            
 
        pygame.display.flip()

        clock.tick(100)
    
    pygame.quit()