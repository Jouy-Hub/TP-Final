#Importar lo necesariowd
# Escribir el menu en el mismo loop de pygame.
# Escribir primero game()
import pygame
from juego import *

def main():

    players,cpu=terminal_menu()
    game(players,cpu)

if __name__=="__main__":
    main()