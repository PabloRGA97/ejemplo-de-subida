import os
import random
import time
import sys
import pygame

pygame.init()
pygame.mixer.init()


#se preparan las variables de las cartas en mano, los puntos de cada jugador, el contador de rondas y música

cartasmanoP1 = [1,2,3,4,5,6,7]

cartasmanoP2 = [1,2,3,4,5,6,7]

puntosganadosP1 = 0

puntosganadosP2 = 0

contador_rondas = 0

musica_intro = "musica/yugioh.mp3"



# Se imprime en pantalla para solicitar información al usuario mientras suena musica de intro



pygame.mixer.music.load(musica_intro)
pygame.mixer.music.play(0)



print    ('''                                                                                                                                                                            ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████   ████   ███   ████████████     ████████   █████   █   ███  █████     █████   ████  ██       █    ██████ ████████████████████████████
█████████████████████████  ███ ██  ████  █████   █████  ███   ███  ███   ██  ███  ███ ██████  ███   ██   ████  ██  ████ ██  ███████  ███████████████████████████
████████████████████   ██   █████  ████  █████    ████  █████  █  █████  ███  ██  ██  ██████  ████   █   ████  ██  ███ ███  ███████  ███████████████████████████
██████████████████████████     ██        ████ ██  ████  █████  █  █████  ███       █ ███████  █████  █   ████  ██      ███  ███████ ████████████████████████████
█████████████████████ ███████   █  ████  ███  ███  ███  ████   █  █████  ████   █    ███████  ████   █   ████  ██  ███████  ████████████████████████████████████
█████████████████████  ██  ██  ██  ████  ██  ████   ██       ████   █   ██████ ███  ████████       ████   ██  ███       ██       ██  ███████████████████████████
████████████████████   █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████  █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
''')








print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                         Menu de Juego                                                                 ")
print("                                                                                                                                                       ")
print("                                                                    1.  Echar una partida                                                              ")
print("                                                                    2.  Salir del juego                                                                ")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")



while True:

    modojuego = int(input("¡Bienvenido al minijuego de cartas! Pulsa 1 para empezar una partida o 2 para salir del juego: "))



    if modojuego == 1:
     print("Está bien, ¡adelante!")
     time.sleep(3)
     break

    elif modojuego == 2:
        print("Saliendo del juego. ¡Hasta la próxima!")
        time.sleep(3)
        sys.exit()
    else:
        print("No es un modo válido, por favor introduce uno de entre las opciones...")
        time.sleep(2)






#se ha comenzado el juego y las rondas se suceden dentro del while




while contador_rondas < 7:
    os.system("cls")
    print(f"Tus cartas son las siguientes: {cartasmanoP1}, mientras que las de tu oponente son {cartasmanoP2}")
    jugadaplayer1_1 = int(input("Introduce una de las cartas para jugar de entre las disponibles (mediante números del 1 al 7): "))

    jugadaplayer2_1 = random.choice(cartasmanoP2)

    print(f"Jugador 1 juega la carta: {jugadaplayer1_1}")


    print("------------------------------------------------------------------------------------------------------------------------")

    if jugadaplayer1_1 not in cartasmanoP1 or jugadaplayer2_1 not in cartasmanoP2:
        print("Esa carta ya no está disponible, elije otra...") 
        time.sleep(3)

    elif jugadaplayer1_1 > jugadaplayer2_1:

        print("3")
        time.sleep(1) 
        print("2")
        time.sleep(1)
        print("1...")
        time.sleep(1) 

        print(f"Jugador 2 juega la carta: {jugadaplayer2_1}")

        print("--------------------------------------------------------------------------------------------------------------------")
        print("JUGADOR 1 GANA!")

        print("--------------------------------------------------------------------------------------------------------------------")
        cartasmanoP1.remove(jugadaplayer1_1)
        cartasmanoP2.remove(jugadaplayer2_1)
        contador_rondas = contador_rondas + 1

        puntosganadosP1 += 2
        print(f"Puntos Jugador 1 = {puntosganadosP1}")
        print(f"Puntos Jugador 2 = {puntosganadosP2}")
        input("Pulsa ENTER para comenzar la siguiente ronda")
        os.system("cls")

    elif jugadaplayer1_1 == jugadaplayer2_1:
        
        print("3")
        time.sleep(1) 
        print("2")
        time.sleep(1)
        print("1...")
        time.sleep(1) 

        print(f"Jugador 2 juega la carta: {jugadaplayer2_1}")

        print("--------------------------------------------------------------------------------------------------------------------")
        print("Ambos jugadores han jugado la misma carta! Por lo tanto se queda en mesa!")
        print("--------------------------------------------------------------------------------------------------------------------")
        cartasmanoP1.remove(jugadaplayer1_1)
        cartasmanoP2.remove(jugadaplayer2_1)
        contador_rondas = contador_rondas + 1
        print(f"Puntos Jugador 1 = {puntosganadosP1}")
        print(f"Puntos Jugador 2 = {puntosganadosP2}")
        input("Pulsa ENTER para comenzar la siguiente ronda")
        os.system("cls")
    else:
        print("3")
        time.sleep(1) 
        print("2")
        time.sleep(1)
        print("1...")
        time.sleep(1) 

        print(f"Jugador 2 juega la carta: {jugadaplayer2_1}")

        print("Has perdido la ronda...")
        cartasmanoP1.remove(jugadaplayer1_1)
        cartasmanoP2.remove(jugadaplayer2_1)
        contador_rondas = contador_rondas + 1

        puntosganadosP2 += 2
        print(f"Puntos Jugador 1 = {puntosganadosP1}")
        print(f"Puntos Jugador 2 = {puntosganadosP2}")
        input("Pulsa ENTER para comenzar la siguiente ronda")
        os.system("cls")
print("------------------------------------------------------------------------------------------------------------------------")


#Al terminar las rondas, se muestra los puntos de ambos jugadores y quien ha ganado o perdido

print(f"Puntos Jugador 1 = {puntosganadosP1}")
print(f"Puntos Jugador 2 = {puntosganadosP2}")

if puntosganadosP1 > puntosganadosP2:
    print("------------------------------------------------------------------------------------------------------------------------")
    print("El Jugador 1 ha ganado!")
    print("------------------------------------------------------------------------------------------------------------------------")
elif puntosganadosP1 == puntosganadosP2:
    print("------------------------------------------------------------------------------------------------------------------------")
    print("ha habido un EMPATE!!!")
    print("------------------------------------------------------------------------------------------------------------------------")
else:
    print("------------------------------------------------------------------------------------------------------------------------")
    print("El Jugador 2 ha ganado!")
    print("------------------------------------------------------------------------------------------------------------------------")


      