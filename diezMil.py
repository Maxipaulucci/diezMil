#--------------------------------------------------------------------------------------------------------------
#MODULOS IMPORTADOS
#--------------------------------------------------------------------------------------------------------------
import random
from time import sleep

#--------------------------------------------------------------------------------------------------------------
#FUNCIONES
#--------------------------------------------------------------------------------------------------------------

def reglas():
    decision = pedirEntero("Ingrese si quiere saber las reglas del 10.000 con 5 dados o con 6 dados (5 o 6): ", "Valor incorrecto!")

    while decision != 5 and decision != 6:
        print("Valor incorrecto!")
        decision = pedirEntero("Quieres saber las reglas del 10.000 con 5 dados o con 6 dados: ", "Valor incorrecto!")

    if decision == 5:
        print()
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· El 10.000 es un juego de dados en el cual el objetivo es conseguir 10.000 puntos.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· ¿COMO SUMAR PUNTOS? Hay 5 opciones posibles para sumar puntos:")
        print("   - Los dados con un valor igual a 1 suman 100 puntos cada uno.")
        print("   - Los dados con valor un valor igual a 5 suman 50 puntos cada uno.")
        print("   - Si obtengo tres dados con igual valor se multiplica su valor por 100, exceptuando el 1 que su valor se multiplica por 1000.")
        print("   - Si obtengo cinco dados con igual valor se multiplica su valor por 1000, exceptuando el 1 que su valor se multiplica por 10.000.")
        print("   - Escalera de dados en orden ascendente (1, 2, 3, 4, 5 o 2, 3, 4, 5, 6) suma 500 puntos.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Para comenzar a sumar puntos, debes obtener un total de 750 puntos en un solo turno.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Si en algún lanzamiento no sumas puntos, perderás el turno y se restarán los puntos conseguidos en ese turno.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Después de anotar puntos en un turno, los dados que contribuyeron a esa puntuación serán retirados. Por ejemplo, si en mi primer lanzamiento con 5 dados obtengo 2, 1, 6, 4 y 5, en el próximo lanzamiento solo tendré disponibles los dados que no fueron parte de la puntuación obtenida, es decir, 3 dados en este caso.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("Si en diversas rondas todos los dados muestran combinaciones que suman puntos, tendrás la opción de decidir entre volver a lanzar los seis dados o mantener tu puntaje en ese momento. Por ejemplo, si en una tirada obtuviste 3, 3, 3, en la siguiente 1, 5 y en la ultima obtuviste un 5, en la cuarta ronda podrás elegir entre arriesgarte a lanzar nuevamente los seis dados o conservar tu puntaje actual.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Ten cuidado, si te pasas de 10.000 puntos, no ganarás y tu puntaje se reiniciará al valor anterior al turno en que superaste los 10.000 puntos. Es decir para ganar debes obtener un puntaje total de exactamente 10.000 puntos")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Cabe aclarar que este es un juego infinito por lo tanto es imposible de programar asi que tendras como máximo 10 tiradas que ya es muy dificil de llegar hasta alli")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Hay un pequeño easter egg (secreto oculto) escondido y deberas encontrarlo!")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("Sumérgete en el emocionante mundo del juego, desafía el azar y disfruta cada tirada mientras compartes risas con tu oponente. ¡Que los dados estén a tu favor en este emocionante viaje hacia la victoria! ¡Buena suerte y que comience el juego!")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    elif decision == 6:
        print()
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· El 10.000 es un juego de dados en el cual el objetivo es conseguir 10.000 puntos.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Para empezar a sumar puntos deberas utilizar la estrategia y elegir tus propias combinaciones ganadoras de puntos.")
        
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("Hay 6 opciones posibles para sumar puntos:")
        print("   -Dados con valor 1 suman 100 puntos cada uno.")
        print("   -Dados con valor 5 suman 50 puntos cada uno.")
        print("   -Tres dados iguales multiplican su valor por 100, exceptuando el 1 que su valor se multiplica por 1000.")
        print("   -Si logras sacar escalera de dados en orden ascendente (1, 2, 3, 4, 5, 6) suma 1500 puntos.")
        print("   -Tres pares simultáneos suman 1500 puntos, por ejemplo si en la tirada los valores de los dados son: 6, 6, 4, 4, 1, 1")
        print("   -Cuatro iguales y un par en un lanzamiento suman 1.500 puntos, por ejemplo si en la tirada los valores de los dados son: 6, 6, 6, 6, 2, 2")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Tienes la libertad de elegir estratégicamente tus combinaciones de dados. Por ejemplo, si en un lanzamiento obtengo tres pares simultáneos, no estoy obligado a sumar automáticamente 1500 puntos. Puedo optar por seleccionar dados específicos y descartar los demás. Por ejemplo, si obtengo 5, 5, 3, 3, 1, 1, tengo la opción de sumar 1500 puntos o elegir los dados con valor 5, 5, 1 y 1, descartando los otros 2 y lanzandolos en el proximo lanzamiento.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· ¿SE PUEDE GANAR EN UN SOLO LANZAMIENTO?")
        print("   -Si, hay una unica manera de ganar la partida en un solo lanzamiento, esa manera es obteniendo los 6 dados con el mismo valor.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Para comenzar a sumar puntos, debes obtener un total de 750 puntos en un solo turno.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Si en algún lanzamiento no sumas puntos, perderás el turno y se restarán los puntos conseguidos en ese turno.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Después de anotar puntos en un turno, los dados que contribuyeron a esa puntuación serán retirados. Por ejemplo, si en mi primer lanzamiento con 5 dados obtengo 2, 1, 6, 4 y 5, en el próximo lanzamiento solo tendré disponibles los dados que no fueron parte de la puntuación obtenida, es decir, 3 dados en este caso.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("Si en diversas rondas todos los dados muestran combinaciones que suman puntos, tendrás la opción de decidir entre volver a lanzar los seis dados o mantener tu puntaje en ese momento. Por ejemplo, si en una tirada obtuviste 3, 3, 3, en la siguiente 1, 5 y en la ultima obtuviste un 5, en la cuarta ronda podrás elegir entre arriesgarte a lanzar nuevamente los seis dados o conservar tu puntaje actual.")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Ten cuidado, si te pasas de 10.000 puntos, no ganarás y tu puntaje se reiniciará al valor anterior al turno en que superaste los 10.000 puntos. Es decir para ganar debes obtener un puntaje total de exactamente 10.000 puntos")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Cabe aclarar que este es un juego infinito por lo tanto es imposible de programar asi que tendras como máximo 10 tiradas que ya es muy dificil de llegar hasta alli")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("· Hay un pequeño easter egg (secreto oculto) escondido y deberas encontrarlo!")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        print("Sumérgete en el emocionante mundo del juego, desafía el azar y disfruta cada tirada mientras compartes risas con tu oponente. ¡Que los dados estén a tu favor en este emocionante viaje hacia la victoria! ¡Buena suerte y que comience el juego!")

        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def pedirEntero(mensajeInput, mensajeError):
#Esta función sirve para pedir un valor y validar si es un número entero utilizando excepciones, si no se ingresa nada o si se ingresa un valor que no se pueda convertir a un entero entonces se debe mostrar el mensaje de error y volver a pedir el valor
    try:
        num = int(input(mensajeInput))
    except ValueError:
        print(mensajeError)
        num = pedirEntero(mensajeInput, mensajeError)
    return num

def pedirCadena(mensajeInput, mensajeError):
#Esta función sirve para pedir una cadena y validar si es una cadena utilizando excepciones, si no se ingresa nada o si se ingresa un entero entonces se debe mostrar el mensaje de error y volver a pedir el valor
    cadena = input(mensajeInput).upper()
    while cadena.strip().isdigit() or cadena.strip() == "":
        print(mensajeError)
        cadena = pedirCadena(mensajeInput, mensajeError).upper()
    return cadena

def funcionJugarConCincoDados(posicionDado, numsDeDados, sumaTotalDeDadosPrimerJugador, sumaTotalDeDadosSegundoJugador, unoContador, dosContador, tresContador, cuatroContador, cincoContador, seisContador):

    jugador1 = pedirCadena("Ingrese el nombre del primer jugador: ", "Nombre no valido!")
    jugador2 = pedirCadena("Ingrese el nombre del segundo jugador: ", "Nombre no valido!")

    while sumaTotalDeDadosPrimerJugador != 10000 or sumaTotalDeDadosSegundoJugador != 10000:

        cantidadDePuntosQueLeFaltanAlPrimerJugadorParaLlegarA10000 = 10000 - sumaTotalDeDadosPrimerJugador
        cantidadDePuntosQueLeFaltanAlSegundoJugadorParaLlegarA10000 = 10000 - sumaTotalDeDadosSegundoJugador

        print(f"TURNO DE: {jugador1}!!!!")
        sleep(2)

        while True:
            if sumaTotalDeDadosPrimerJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje inicial es {sumaTotalDeDadosPrimerJugador}, necesitas 750 puntos como minimo para seguir sumando!")
                print("-------------------------------------------")
            else:
                print("-------------------------------------------")
                print(f"Tu puntaje es {sumaTotalDeDadosPrimerJugador} y faltan {cantidadDePuntosQueLeFaltanAlPrimerJugadorParaLlegarA10000} puntos para llegar a 10.000!")
                print("-------------------------------------------")

            print(f"PRIMERA TIRADA DE {jugador1}!")
            sleep(1)
            sumaDeDadosPrimerJugador = 0
            variableParaSaberSiNoSumoNada = 0
            sumaDePuntosDelJugadorHastaEstaRonda = 0
            unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0
            dadosDisponibles = 5
            dadosDisponiblesPrimerTirada = dadosDisponibles

            for i in range(dadosDisponiblesPrimerTirada):
                dado = random.randint(1,6)
                if dado == 1:
                    unoContador += 1
                    sumaDeDadosPrimerJugador += 100
                    dadosDisponibles -= 1
                elif dado == 2:
                    dosContador += 1
                elif dado == 3:
                    tresContador += 1
                elif dado == 4:
                    cuatroContador += 1
                elif dado == 5:
                    cincoContador += 1
                    sumaDeDadosPrimerJugador += 50
                    dadosDisponibles -= 1
                elif dado == 6:
                    seisContador += 1

                numsDeDados[i] = dado

            if unoContador >= 3 and unoContador < 5:
                sumaDeDadosPrimerJugador += 700
            elif dosContador >= 3 and dosContador < 5:
                sumaDeDadosPrimerJugador += 200
                dadosDisponibles -= 3
            elif tresContador >= 3 and tresContador < 5:
                sumaDeDadosPrimerJugador += 300
                dadosDisponibles -= 3
            elif cuatroContador >= 3 and cuatroContador < 5:
                sumaDeDadosPrimerJugador += 400
                dadosDisponibles -= 3
            elif cincoContador >= 3 and cincoContador < 5:
                sumaDeDadosPrimerJugador += 350
            elif seisContador >= 3 and seisContador < 5:
                sumaDeDadosPrimerJugador += 600
                dadosDisponibles -= 3

            for i in range(dadosDisponiblesPrimerTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            sumaTotalDeDadosPrimerJugador += sumaDeDadosPrimerJugador

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")

            if sumaTotalDeDadosPrimerJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total hasta el momento es: {sumaTotalDeDadosPrimerJugador}")
                print("-------------------------------------------")

            elif sumaTotalDeDadosPrimerJugador > 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
                print("-------------------------------------------")
            break
        
        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            
            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponibles == 0:
                    dadosDisponibles += 5
                dadosDisponiblesPrimerTirada = dadosDisponibles

                print(f"SEGUNDA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponibles):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesPrimerTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesPrimerTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesPrimerTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesPrimerTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesSegundaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break                      
            elif decision == "SI":
                if dadosDisponiblesPrimerTirada == 0:
                    dadosDisponiblesPrimerTirada += 5
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada

                print(f"TERCERA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesPrimerTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 6:
                        seisContador += 1

                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesSegundaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesSegundaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesSegundaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesSegundaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesTerceraTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break
        
        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada

                print(f"CUARTA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSegundaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesTerceraTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesTerceraTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesTerceraTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesTerceraTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesCuartaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada

                print(f"QUINTA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesTerceraTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesCuartaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesCuartaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesCuartaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesCuartaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesQuintaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")
            
            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesTerceraTirada == 0:
                    dadosDisponiblesTerceraTirada += 5
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada

                print(f"SEXTA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesCuartaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesQuintaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesQuintaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesQuintaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesQuintaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesSextaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesCuartaTirada == 0:
                    dadosDisponiblesCuartaTirada += 5
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada

                print(f"SEPTIMA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesSextaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesSextaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesSextaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesSextaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesSeptimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesQuintaTirada == 0:
                    dadosDisponiblesQuintaTirada += 5
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada

                print(f"OCTAVA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesSeptimaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesSeptimaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesSeptimaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesSeptimaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesOctavaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSextaTirada == 0:
                    dadosDisponiblesSextaTirada += 5
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada

                print(f"NOVENA TIRADA DE {jugador1}! (Tanta suerte tendras {jugador1}, me pregunto si alguien más vera esto siquiera)")
                sleep(1)
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSextaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesOctavaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesOctavaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesOctavaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesOctavaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesNovenaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSeptimaTirada == 0:
                    dadosDisponiblesSeptimaTirada += 5
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada

                print(f"DECIMA Y ULTIMA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesDecimaTirada = dadosDisponiblesNovenaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSeptimaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesNovenaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesNovenaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesNovenaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesNovenaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesDecimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosPrimerJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        sumaTotalDeDadosPrimerJugador += sumaDeDadosPrimerJugador

        if sumaTotalDeDadosPrimerJugador < 750:
            sumaTotalDeDadosPrimerJugador -= sumaTotalDeDadosPrimerJugador
            print(f"Lamentablemente {jugador1} tu puntaje es menor a 750 por lo tanto se te reinician los puntos a 0, mejor suerte en la proxima tirada!")
 
        elif sumaTotalDeDadosPrimerJugador > 10000:
            sumaTotalDeDadosPrimerJugador -= sumaDePuntosDelJugadorHastaEstaRonda
            print(f"Lamentablemente {jugador1} tu puntaje es de mas de 10.000 por lo tanto se te restaran los puntos conseguidos en este turno!")

        elif sumaTotalDeDadosSegundoJugador == 10000:
            print(f"¡Enhorabuena, {jugador1}! Has alcanzado la victoria sobre {jugador2} en este emocionante duelo. Espero que les haya gustado el codigo y lo mas importante que se hayan divertido. Hasta la proxima!")

#--------------------------------------------------------------------------------------------------------------
# SIGUIENTE JUGADOR
#--------------------------------------------------------------------------------------------------------------
        print(f"TURNO DE: {jugador2}!!!!")
        sleep(2)

        while True:
            if sumaTotalDeDadosSegundoJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje inicial es {sumaTotalDeDadosSegundoJugador}, necesitas 750 puntos para seguir sumando!")
                print("-------------------------------------------")
            else:
                print("-------------------------------------------")
                print(f"Tu puntaje es {sumaTotalDeDadosSegundoJugador} y faltan {cantidadDePuntosQueLeFaltanAlSegundoJugadorParaLlegarA10000} puntos para llegar a 10.000!")
                print("-------------------------------------------")

            print(f"PRIMERA TIRADA DE {jugador2}!")
            sleep(1)
            sumaDeDadosSegundoJugador = 0
            variableParaSaberSiNoSumoNada = 0
            sumaDePuntosDelJugadorHastaEstaRonda = 0
            unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0
            dadosDisponibles = 5
            dadosDisponiblesPrimerTirada = dadosDisponibles

            for i in range(dadosDisponiblesPrimerTirada):
                dado = random.randint(1,6)
                if dado == 1:
                    unoContador += 1
                    sumaDeDadosSegundoJugador += 100
                    dadosDisponibles -= 1
                elif dado == 2:
                    dosContador += 1
                elif dado == 3:
                    tresContador += 1
                elif dado == 4:
                    cuatroContador += 1
                elif dado == 5:
                    cincoContador += 1
                    sumaDeDadosSegundoJugador += 50
                    dadosDisponibles -= 1
                elif dado == 6:
                    seisContador += 1

                numsDeDados[i] = dado

            if unoContador >= 3:
                sumaDeDadosSegundoJugador += 700
            elif dosContador >= 3:
                sumaDeDadosSegundoJugador += 200
                dadosDisponibles -= 3
            elif tresContador >= 3:
                sumaDeDadosSegundoJugador += 300
                dadosDisponibles -= 3
            elif cuatroContador >= 3:
                sumaDeDadosSegundoJugador += 400
                dadosDisponibles -= 3
            elif cincoContador >= 3:
                sumaDeDadosSegundoJugador += 350
            elif seisContador >= 3:
                sumaDeDadosSegundoJugador += 600
                dadosDisponibles -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesPrimerTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450
            
            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")

            if sumaTotalDeDadosSegundoJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total hasta el momento es: {sumaTotalDeDadosSegundoJugador}")
                print("-------------------------------------------")

            elif sumaTotalDeDadosSegundoJugador > 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
                print("-------------------------------------------")
            break
        
        while True:
            if sumaDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador 

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            
            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponibles == 0:
                    dadosDisponibles += 5
                dadosDisponiblesPrimerTirada = dadosDisponibles

                print(f"SEGUNDA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSegundaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesPrimerTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesPrimerTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesPrimerTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesPrimerTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesSegundaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450
            
            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break                      
            elif decision == "SI":
                if dadosDisponiblesPrimerTirada == 0:
                    dadosDisponiblesPrimerTirada += 5
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada

                print(f"TERCERA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesTerceraTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 6:
                        seisContador += 1

                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesSegundaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesSegundaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesSegundaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesSegundaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesTerceraTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break
        
        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada

                print(f"CUARTA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSegundaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesTerceraTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesTerceraTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesTerceraTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesTerceraTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesCuartaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada

                print(f"QUINTA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesTerceraTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesCuartaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesCuartaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesCuartaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesCuartaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesQuintaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")
            
            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesTerceraTirada == 0:
                    dadosDisponiblesTerceraTirada += 5
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada

                print(f"SEXTA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesCuartaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesQuintaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesQuintaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesQuintaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesQuintaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesSextaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesCuartaTirada == 0:
                    dadosDisponiblesCuartaTirada += 5
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada

                print(f"SEPTIMA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesSextaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesSextaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesSextaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesSextaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesSeptimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesQuintaTirada == 0:
                    dadosDisponiblesQuintaTirada += 5
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada

                print(f"OCTAVA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesSeptimaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesSeptimaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesSeptimaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesSeptimaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesOctavaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSextaTirada == 0:
                    dadosDisponiblesSextaTirada += 5
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada

                print(f"NOVENA TIRADA DE {jugador2}! (Tanta suerte tendras {jugador1}, me pregunto si alguien más vera esto siquiera)")
                sleep(1)
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSextaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesOctavaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesOctavaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesOctavaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesOctavaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesNovenaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSeptimaTirada == 0:
                    dadosDisponiblesSeptimaTirada += 5
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada

                print(f"DECIMA Y ULTIMA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesDecimaTirada = dadosDisponiblesNovenaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSeptimaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesNovenaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesNovenaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesNovenaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesNovenaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesDecimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5]):
                sumaDeDadosSegundoJugador += 400

            elif all(nums in numsDeDados for nums in [2, 3, 4, 5, 6]):
                sumaDeDadosSegundoJugador += 450

            contadorDados = {1: unoContador, 2: dosContador, 3: tresContador, 4: cuatroContador, 5: cincoContador, 6: seisContador}
            for valor, cantidad in contadorDados.items():
                if cantidad == 5:
                    sumaDeDadosPrimerJugador += valor * 1000 if valor != 1 else valor * 10000

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        sumaTotalDeDadosSegundoJugador += sumaDeDadosSegundoJugador

        if sumaTotalDeDadosSegundoJugador < 750:
            sumaTotalDeDadosSegundoJugador -= sumaTotalDeDadosSegundoJugador
            print(f"Lamentablemente {jugador2} tu puntaje es menor a 750 por lo tanto se te reinician los puntos a 0, mejor suerte en la proxima tirada!")
 
        elif sumaTotalDeDadosSegundoJugador > 10000:
            sumaTotalDeDadosSegundoJugador -= sumaDePuntosDelJugadorHastaEstaRonda
            print(f"Lamentablemente {jugador2} tu puntaje es de mas de 10.000 por lo tanto se te restaran los puntos conseguidos en este turno!")

        elif sumaTotalDeDadosSegundoJugador == 10000:
            print(f"¡Enhorabuena, {jugador2}! Has alcanzado la victoria sobre {jugador1} en este emocionante duelo. Espero que les haya gustado el codigo y lo mas importante que se hayan divertido. Hasta la proxima!")
        
def funcionJugarConSeisDados(posicionDado, numsDeDados, sumaTotalDeDadosPrimerJugador, sumaTotalDeDadosSegundoJugador, unoContador, dosContador, tresContador, cuatroContador, cincoContador, seisContador):

    jugador1 = pedirCadena("Ingrese el nombre del primer jugador: ", "Nombre no valido!")
    jugador2 = pedirCadena("Ingrese el nombre del segundo jugador: ", "Nombre no valido!")

    while sumaTotalDeDadosPrimerJugador != 10000 or sumaTotalDeDadosSegundoJugador != 10000:

        cantidadDePuntosQueLeFaltanAlPrimerJugadorParaLlegarA10000 = 10000 - sumaTotalDeDadosPrimerJugador
        cantidadDePuntosQueLeFaltanAlSegundoJugadorParaLlegarA10000 = 10000 - sumaTotalDeDadosSegundoJugador

        print(f"TURNO DE: {jugador1}!!!!")
        sleep(2)

        while True:
            if sumaTotalDeDadosPrimerJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje inicial es {sumaTotalDeDadosPrimerJugador}, necesitas 750 puntos como minimo para seguir sumando!")
                print("-------------------------------------------")
            else:
                print("-------------------------------------------")
                print(f"Tu puntaje es {sumaTotalDeDadosPrimerJugador} y faltan {cantidadDePuntosQueLeFaltanAlPrimerJugadorParaLlegarA10000} puntos para llegar a 10.000!")
                print("-------------------------------------------")

            print(f"PRIMERA TIRADA DE {jugador1}!")
            sleep(1)
            sumaDeDadosPrimerJugador = 0
            variableParaSaberSiNoSumoNada = 0
            sumaDePuntosDelJugadorHastaEstaRonda = 0
            unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0
            dadosDisponibles = 6
            dadosDisponiblesPrimerTirada = dadosDisponibles

            for i in range(dadosDisponiblesPrimerTirada):
                dado = random.randint(1,6)
                if dado == 1:
                    unoContador += 1
                    sumaDeDadosPrimerJugador += 100
                    dadosDisponibles -= 1
                elif dado == 2:
                    dosContador += 1
                elif dado == 3:
                    tresContador += 1
                elif dado == 4:
                    cuatroContador += 1
                elif dado == 5:
                    cincoContador += 1
                    sumaDeDadosPrimerJugador += 50
                    dadosDisponibles -= 1
                elif dado == 6:
                    seisContador += 1

                numsDeDados[i] = dado

            if unoContador >= 3:
                sumaDeDadosPrimerJugador += 700
            elif dosContador >= 3:
                sumaDeDadosPrimerJugador += 200
                dadosDisponibles -= 3
            elif tresContador >= 3:
                sumaDeDadosPrimerJugador += 300
                dadosDisponibles -= 3
            elif cuatroContador >= 3:
                sumaDeDadosPrimerJugador += 400
                dadosDisponibles -= 3
            elif cincoContador >= 3:
                sumaDeDadosPrimerJugador += 350
            elif seisContador >= 3:
                sumaDeDadosPrimerJugador += 600
                dadosDisponibles -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesPrimerTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponibles = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponibles = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")

            if sumaTotalDeDadosPrimerJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total hasta el momento es: {sumaTotalDeDadosPrimerJugador}")
                print("-------------------------------------------")

            elif sumaTotalDeDadosPrimerJugador > 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
                print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            
            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponibles == 0:
                    dadosDisponibles += 5
                dadosDisponiblesPrimerTirada = dadosDisponibles

                print(f"SEGUNDA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponibles):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesPrimerTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesPrimerTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesPrimerTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesPrimerTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesSegundaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesPrimerTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesPrimerTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break                      
            elif decision == "SI":
                if dadosDisponiblesPrimerTirada == 0:
                    dadosDisponiblesPrimerTirada += 5
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada

                print(f"TERCERA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesPrimerTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 6:
                        seisContador += 1

                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesSegundaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesSegundaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesSegundaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesSegundaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesTerceraTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSegundaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSegundaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break
        
        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada

                print(f"CUARTA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSegundaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesTerceraTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesTerceraTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesTerceraTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesTerceraTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesCuartaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesTerceraTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesTerceraTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada

                print(f"QUINTA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesTerceraTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesCuartaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesCuartaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesCuartaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesCuartaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesQuintaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesCuartaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesCuartaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesTerceraTirada == 0:
                    dadosDisponiblesTerceraTirada += 5
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada

                print(f"SEXTA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesCuartaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesQuintaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesQuintaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesQuintaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesQuintaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesSextaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesQuintaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesQuintaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesCuartaTirada == 0:
                    dadosDisponiblesCuartaTirada += 5
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada

                print(f"SEPTIMA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesSextaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesSextaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesSextaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesSextaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesSeptimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSextaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSextaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesQuintaTirada == 0:
                    dadosDisponiblesQuintaTirada += 5
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada

                print(f"OCTAVA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesSeptimaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesSeptimaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesSeptimaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesSeptimaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesOctavaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSeptimaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSeptimaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSextaTirada == 0:
                    dadosDisponiblesSextaTirada += 5
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada

                print(f"NOVENA TIRADA DE {jugador1}! (Tanta suerte tendras {jugador1}, me pregunto si alguien más vera esto siquiera)")
                sleep(1)
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSextaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesOctavaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesOctavaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesOctavaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesOctavaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesNovenaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesOctavaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesOctavaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosPrimerJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosPrimerJugador:
                break
            elif sumaTotalDeDadosPrimerJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosPrimerJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosPrimerJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSeptimaTirada == 0:
                    dadosDisponiblesSeptimaTirada += 5
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada

                print(f"DECIMA Y ULTIMA TIRADA DE {jugador1}!")
                sleep(1)
                dadosDisponiblesDecimaTirada = dadosDisponiblesNovenaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSeptimaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosPrimerJugador += 100
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosPrimerJugador += 50
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosPrimerJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosPrimerJugador += 200
                    dadosDisponiblesNovenaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosPrimerJugador += 300
                    dadosDisponiblesNovenaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosPrimerJugador += 400
                    dadosDisponiblesNovenaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosPrimerJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosPrimerJugador += 600
                    dadosDisponiblesNovenaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosPrimerJugador

            for i in range(dadosDisponiblesDecimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesNovenaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesNovenaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosPrimerJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosPrimerJugador}")
            print("-------------------------------------------")
            break

        sumaTotalDeDadosPrimerJugador += sumaDeDadosPrimerJugador

        if sumaTotalDeDadosPrimerJugador < 750:
            sumaTotalDeDadosPrimerJugador -= sumaTotalDeDadosPrimerJugador
            print(f"Lamentablemente {jugador1} tu puntaje es menor a 750 por lo tanto se te reinician los puntos a 0, mejor suerte en la proxima tirada!")
 
        elif sumaTotalDeDadosPrimerJugador > 10000:
            sumaTotalDeDadosPrimerJugador -= sumaDePuntosDelJugadorHastaEstaRonda
            print(f"Lamentablemente {jugador1} tu puntaje es de mas de 10.000 por lo tanto se te restaran los puntos conseguidos en este turno!")

        elif sumaTotalDeDadosSegundoJugador == 10000:
            print(f"¡Enhorabuena, {jugador1}! Has alcanzado la victoria sobre {jugador2} en este emocionante duelo. Espero que les haya gustado el codigo y lo mas importante que se hayan divertido. Hasta la proxima!")

#--------------------------------------------------------------------------------------------------------------
# SIGUIENTE JUGADOR
#--------------------------------------------------------------------------------------------------------------
        print(f"TURNO DE: {jugador2}!!!!")
        sleep(2)

        while True:
            if sumaTotalDeDadosSegundoJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje inicial es {sumaTotalDeDadosSegundoJugador}, necesitas 750 puntos para seguir sumando!")
                print("-------------------------------------------")
            else:
                print("-------------------------------------------")
                print(f"Tu puntaje es {sumaTotalDeDadosSegundoJugador} y faltan {cantidadDePuntosQueLeFaltanAlSegundoJugadorParaLlegarA10000} puntos para llegar a 10.000!")
                print("-------------------------------------------")

            print(f"PRIMERA TIRADA DE {jugador2}!")
            sleep(1)
            sumaDeDadosSegundoJugador = 0
            variableParaSaberSiNoSumoNada = 0
            sumaDePuntosDelJugadorHastaEstaRonda = 0
            unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0
            dadosDisponibles = 5
            dadosDisponiblesPrimerTirada = dadosDisponibles

            for i in range(dadosDisponiblesPrimerTirada):
                dado = random.randint(1,6)
                if dado == 1:
                    unoContador += 1
                    sumaDeDadosSegundoJugador += 100
                    dadosDisponibles -= 1
                elif dado == 2:
                    dosContador += 1
                elif dado == 3:
                    tresContador += 1
                elif dado == 4:
                    cuatroContador += 1
                elif dado == 5:
                    cincoContador += 1
                    sumaDeDadosSegundoJugador += 50
                    dadosDisponibles -= 1
                elif dado == 6:
                    seisContador += 1

                numsDeDados[i] = dado

            if unoContador >= 3:
                sumaDeDadosSegundoJugador += 700
            elif dosContador >= 3:
                sumaDeDadosSegundoJugador += 200
                dadosDisponibles -= 3
            elif tresContador >= 3:
                sumaDeDadosSegundoJugador += 300
                dadosDisponibles -= 3
            elif cuatroContador >= 3:
                sumaDeDadosSegundoJugador += 400
                dadosDisponibles -= 3
            elif cincoContador >= 3:
                sumaDeDadosSegundoJugador += 350
            elif seisContador >= 3:
                sumaDeDadosSegundoJugador += 600
                dadosDisponibles -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesSegundaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesPrimerTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesPrimerTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")

            if sumaTotalDeDadosSegundoJugador == 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total hasta el momento es: {sumaTotalDeDadosSegundoJugador}")
                print("-------------------------------------------")

            elif sumaTotalDeDadosSegundoJugador > 0:
                print("-------------------------------------------")
                print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
                print("-------------------------------------------")
            break
        
        while True:
            if sumaDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador 

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            
            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponibles == 0:
                    dadosDisponibles += 5
                dadosDisponiblesPrimerTirada = dadosDisponibles

                print(f"SEGUNDA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSegundaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesPrimerTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesPrimerTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesPrimerTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesPrimerTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesPrimerTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesSegundaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesPrimerTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesPrimerTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break                      
            elif decision == "SI":
                if dadosDisponiblesPrimerTirada == 0:
                    dadosDisponiblesPrimerTirada += 5
                dadosDisponiblesSegundaTirada = dadosDisponiblesPrimerTirada

                print(f"TERCERA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesTerceraTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesSegundaTirada -= 1
                    elif dado == 6:
                        seisContador += 1

                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesSegundaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesSegundaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesSegundaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesSegundaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesTerceraTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSegundaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSegundaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break
        
        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesTerceraTirada = dadosDisponiblesSegundaTirada

                print(f"CUARTA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSegundaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesTerceraTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesTerceraTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesTerceraTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesTerceraTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesTerceraTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesCuartaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesTerceraTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesTerceraTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSegundaTirada == 0:
                    dadosDisponiblesSegundaTirada += 5
                dadosDisponiblesCuartaTirada = dadosDisponiblesTerceraTirada

                print(f"QUINTA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesTerceraTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesCuartaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesCuartaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesCuartaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesCuartaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesCuartaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesQuintaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesCuartaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesCuartaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesTerceraTirada == 0:
                    dadosDisponiblesTerceraTirada += 5
                dadosDisponiblesQuintaTirada = dadosDisponiblesCuartaTirada

                print(f"SEXTA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesCuartaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesQuintaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesQuintaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesQuintaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesQuintaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesQuintaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesSextaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesQuintaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesQuintaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesCuartaTirada == 0:
                    dadosDisponiblesCuartaTirada += 5
                dadosDisponiblesSextaTirada = dadosDisponiblesQuintaTirada

                print(f"SEPTIMA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesSextaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesSextaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesSextaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesSextaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesSextaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesSeptimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSextaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSextaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesQuintaTirada == 0:
                    dadosDisponiblesQuintaTirada += 5
                dadosDisponiblesSeptimaTirada = dadosDisponiblesSextaTirada

                print(f"OCTAVA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesQuintaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesSeptimaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesSeptimaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesSeptimaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesSeptimaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesSeptimaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesOctavaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSeptimaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesSeptimaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSextaTirada == 0:
                    dadosDisponiblesSextaTirada += 5
                dadosDisponiblesOctavaTirada = dadosDisponiblesSeptimaTirada

                print(f"NOVENA TIRADA DE {jugador2}! (Tanta suerte tendras {jugador1}, me pregunto si alguien más vera esto siquiera)")
                sleep(1)
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSextaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesOctavaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesOctavaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesOctavaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesOctavaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesOctavaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesNovenaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesOctavaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesOctavaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        while True:
            if sumaTotalDeDadosSegundoJugador == 0 or variableParaSaberSiNoSumoNada == sumaDeDadosSegundoJugador:
                break
            elif sumaTotalDeDadosSegundoJugador > 10000:
                print(f"Te pasaste de los 10.000 puntos, tu puntaje total fue: {sumaTotalDeDadosSegundoJugador}")

            variableParaSaberSiNoSumoNada = sumaDeDadosSegundoJugador

            decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")
            while decision != "NO" and decision != "SI":
                decision = pedirCadena("Quiere seguir tirando (SI/NO): ", "Valor incorrecto!")

            if decision == "NO":
                break
            elif decision == "SI":
                if dadosDisponiblesSeptimaTirada == 0:
                    dadosDisponiblesSeptimaTirada += 5
                dadosDisponiblesNovenaTirada = dadosDisponiblesOctavaTirada

                print(f"DECIMA Y ULTIMA TIRADA DE {jugador2}!")
                sleep(1)
                dadosDisponiblesDecimaTirada = dadosDisponiblesNovenaTirada
                unoContador = dosContador = tresContador = cuatroContador = cincoContador = seisContador = 0

                for i in range(dadosDisponiblesSeptimaTirada):
                    dado = random.randint(1,6)
                    if dado == 1:
                        unoContador += 1
                        sumaDeDadosSegundoJugador += 100
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 2:
                        dosContador += 1
                    elif dado == 3:
                        tresContador += 1
                    elif dado == 4:
                        cuatroContador += 1
                    elif dado == 5:
                        cincoContador += 1
                        sumaDeDadosSegundoJugador += 50
                        dadosDisponiblesNovenaTirada -= 1
                    elif dado == 6:
                        seisContador += 1
                            
                    numsDeDados[i] = dado

                if unoContador >= 3:
                    sumaDeDadosSegundoJugador += 700
                elif dosContador >= 3:
                    sumaDeDadosSegundoJugador += 200
                    dadosDisponiblesNovenaTirada -= 3
                elif tresContador >= 3:
                    sumaDeDadosSegundoJugador += 300
                    dadosDisponiblesNovenaTirada -= 3
                elif cuatroContador >= 3:
                    sumaDeDadosSegundoJugador += 400
                    dadosDisponiblesNovenaTirada -= 3
                elif cincoContador >= 3:
                    sumaDeDadosSegundoJugador += 350
                elif seisContador >= 3:
                    sumaDeDadosSegundoJugador += 600
                    dadosDisponiblesNovenaTirada -= 3

            sumaDePuntosDelJugadorHastaEstaRonda += sumaDeDadosSegundoJugador

            for i in range(dadosDisponiblesDecimaTirada):
                print(f"{posicionDado[i]} dado: {numsDeDados[i]}")

            if all(nums in numsDeDados for nums in [1, 2, 3, 4, 5, 6]):
                sumaDeDadosPrimerJugador += 1350

            if unoContador == 6 or dosContador == 6 or tresContador == 6 or cuatroContador == 6 or cincoContador == 6 or seisContador == 6:
                sumaTotalDeDadosPrimerJugador = 10000

            if (unoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (unoContador == 2 and cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (cincoContador == 2 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)):

                decision = pedirCadena("Obtuviste 3 pares simultáneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste 3 pares simultaneos. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesNovenaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            elif (unoContador == 4 and (dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (dosContador == 4 and (unoContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (tresContador == 4 and (unoContador == 2 or dosContador == 2 or cuatroContador == 2 or cincoContador == 2 or seisContador == 2)) or (cuatroContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cincoContador == 2 or seisContador == 2)) or (cincoContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or seisContador == 2)) or (seisContador == 4 and (unoContador == 2 or dosContador == 2 or tresContador == 2 or cuatroContador == 2 or cincoContador == 2)):

                decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                while decision != "NO" and decision != "SI":
                    decision = pedirCadena("Obtuviste cuatro iguales y un par. ¿Quieres quedarte con los 1500 puntos? (SI/NO): ", "Valor incorrecto!")

                if decision == "SI":
                    dadosDisponiblesNovenaTirada = 0
                    sumaDeDadosPrimerJugador -= sumaDeDadosPrimerJugador
                    sumaDeDadosPrimerJugador += 1500

            print("-------------------------------------------")
            print(f"Tu puntaje en esta tirada fue: {sumaDeDadosSegundoJugador}")
            print("-------------------------------------------")
            print("-------------------------------------------")
            print(f"Tu puntaje total es: {sumaTotalDeDadosSegundoJugador}")
            print("-------------------------------------------")
            break

        sumaTotalDeDadosSegundoJugador += sumaDeDadosSegundoJugador

        if sumaTotalDeDadosSegundoJugador < 750:
            sumaTotalDeDadosSegundoJugador -= sumaTotalDeDadosSegundoJugador
            print(f"Lamentablemente {jugador2} tu puntaje es menor a 750 por lo tanto se te reinician los puntos a 0, mejor suerte en la proxima tirada!")
 
        elif sumaTotalDeDadosSegundoJugador > 10000:
            sumaTotalDeDadosSegundoJugador -= sumaDePuntosDelJugadorHastaEstaRonda
            print(f"Lamentablemente {jugador2} tu puntaje es de mas de 10.000 por lo tanto se te restaran los puntos conseguidos en este turno!")

        elif sumaTotalDeDadosSegundoJugador == 10000:
            print(f"¡Enhorabuena, {jugador2}! Has alcanzado la victoria sobre {jugador1} en este emocionante duelo. Espero que les haya gustado el codigo y lo mas importante que se hayan divertido. Hasta la proxima!")
    
#--------------------------------------------------------------------------------------------------------------
# Inicialización de variables
#--------------------------------------------------------------------------------------------------------------
posicionDado = ["1°", "2°","3°", "4°", "5°", "6°"]
numsDeDados = [0, 0, 0, 0, 0, 0]
sumaDeDadosPrimerJugador = 0
sumaTotalDeDadosPrimerJugador = 0
sumaDeDadosSegundoJugador = 0
sumaTotalDeDadosSegundoJugador = 0
unoContador = 0
dosContador = 0
tresContador = 0
cuatroContador = 0
cincoContador = 0
seisContador = 0
#--------------------------------------------------------------------------------------------------------------
# Bloque de menú
#--------------------------------------------------------------------------------------------------------------

while True:
    while True:
        try:
            print()
            print("-------------------------------------------")
            print("MENÚ DEL SISTEMA")
            print("-------------------------------------------")
            print("[1] Mostrar reglas")
            print("[2] Jugar con 5 dados")
            print("[3] Jugar con 6 dados")
            print("-------------------------------------------")
            print("[0] Salir")
            print("-------------------------------------------")
            print()

            opcion = input("Seleccione una opción: ")
            if opcion in ["0", "1", "2", "3"]: #Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        except ValueError:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == "0":
        break

    elif opcion == "1":
       print()
       reglas()
        
    elif opcion == "2":
        print()
        funcionJugarConCincoDados(posicionDado, numsDeDados, sumaTotalDeDadosPrimerJugador, sumaTotalDeDadosSegundoJugador, unoContador, dosContador, tresContador, cuatroContador, cincoContador, seisContador)

    elif opcion == "3":
        print()
        funcionJugarConSeisDados(posicionDado, numsDeDados, sumaTotalDeDadosPrimerJugador, sumaTotalDeDadosSegundoJugador, unoContador, dosContador, tresContador, cuatroContador, cincoContador, seisContador)

    print()
    input("Presione ENTER para volver al menú.")