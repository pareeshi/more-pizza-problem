#!/bin/python3

# --------------------------------------------------------------------


#	Corso di Ricerca Operativa (9 CFU), prof. Maurizio Boccia


# --------------------------------------------------------------------


def preleva(input):
    inputFile = open(inputDir + fileName + ".in", "rt")

    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()

    print(firstLine)
    print(secondLine)

    MAX, NUM = list(map(int, firstLine.split()))

    #  Create the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))


def scrivi_output(input, pizze_scelte):

    print("")
    print("OUTPUT")
    print(len(pizze_scelte))

    outputString = ""
    for l in pizze_scelte:
        outputString = outputString + str(l) + " "
    print(outputString)

    outputFile = open(outputDir + fileName + ".out", "w")
    outputFile.write(str(len(pizze_scelte)) + "\n")
    outputFile.write(outputString)
    outputFile.close()


def approccio_greedy(num_max_fette, tipi_di_pizza):
    punteggio = 0
    somma = 0

    dim_tipi_pizza = len(tipi_di_pizza)

    sol_array_indici = []
    sol_array_fette = []

    temp_array_indici = []
    temp_array_fette = []

    start_counter = dim_tipi_pizza

    while((len(temp_array_indici) > 0 and temp_array_indici[0] != 0) or len(temp_array_indici) == 0):
        start_counter -= 1

        for index in range(start_counter, -1, -1):

            valore_corrente = tipi_di_pizza[index]

            somma_temp = somma + valore_corrente

            if(somma_temp == num_max_fette):
                somma = somma_temp
                temp_array_indici.append(index)
                temp_array_fette.append(valore_corrente)
                break

            elif (somma_temp > num_max_fette):
                continue

            elif (somma_temp < num_max_fette):
                somma = somma_temp
                temp_array_indici.append(index)
                temp_array_fette.append(currentValue)
                continue

        if (punteggio < somma):
            punteggio = somma

            for indice in temp_array_indici:
                sol_array_indici.append(indice)

            for valore in temp_array_fette:
                sol_array_fette.append(valore)

        if(punteggio == num_max_fette):
            break

        if(len(temp_array_fette) != 0):
            temp = temp_array_fette.pop()
            somma -= temp

        if (len(temp_array_indici) != 0):
            temp_ind = temp_array_indici.pop()
            start_counter = temp_ind

        if(len(temp_array_indici) == 0 and (start_counter) == 0):
            break

    print()
    print("Punteggio generato e' = " + str(punteggio))
    print()


    return punteggio, sol_array_indici

# def approccio_dinamico(num_max_fette, tipi_di_pizza):


# approccio migliorativo: clona la soluzione greedy e valuta l'ottimo locale, variando la soluzione ed effettuando tentativi
# in questo modo effettuo poi il confronto con la soluzione greedy ed eventualmente aggiorno il punteggio
# def approccio_migliorativo()

# def risolvi

# Score: un punto per ogni fetta di pizza ordinata.

# Ricevo il file in ingresso. Da esso, separo tutti gli attributi di cui ho bisogno
# Prendo il numero di fette massime, i tipi di pizza e un vettore di fette di pizza per ogni tipo di pizza
# con approccio Greedy (costruisco la soluzione gradualmente, scegliendo l'ottimo locale) e
# un approccio dinamico, che punta alla generazione della soluzione partendo dall'ultimo elemento
# del vettore, e procede fino a generare un punteggio massimo.

# Output: bisogna generare in output un file di estensione ".out" che rispetti le condizioni della traccia.

# Input selezionato

def risolvi(input):

    print("Input elaborato: " + input)

    num_max_fette, num_tipi_pizza, tipi_di_pizza = preleva(input)

    # Imposto il punteggio

    punteggio = 0

    # Scelgo tra metodo dinamico o greedy a seconda del numero di fette massime

    if(num_max_fette > 10000 or num_tipi_pizza > 250):
        punteggio, pizze_scelte = approccio_greedy(
            num_max_fette, tipi_di_pizza)
    else:
        punteggio, pizze_scelte = approccio_dinamico(
            num_max_fette, tipi_di_pizza)

    # Imposto un metodo per stampare il file in output
    scrivi_output(input, pizze_scelte)

    # Ritorno il punteggio

    return punteggio


if __name__ == '__main__':
    punteggio = 0
    # Istanze fornite dalla traccia, le passiamo in input e le operiamo una ad una

    inputDir = "in/"
    outputDir = "out/"

    ingressi = [
        "a_example",
        "b_small",
        "c_medium",
        "d_quite_big",
        "e_also_big"
    ]

    # Stampe a video

    print("------------------------\n")
    print("Google Hash Code 2020 \n")
    print("More Pizza \n")
    print("Di: Daniel Parisi e Francesco Ottata \n")
    print("------------------------\n")

    # Processiamo ogni input

    print()
    for input in ingressi:
        punteggio += risolvi(input)
        print()
