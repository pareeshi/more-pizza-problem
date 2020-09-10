# --------------------------------------------------------------------


#	Corso di Ricerca Operativa (9 CFU), prof. Maurizio Boccia
#	Google Hash Code Problem - More Pizza (2020)


# --------------------------------------------------------------------



from random import randrange
# Lanciare Gurobi con interprete Python3.7 da terminale
import gurobipy as gp
from gurobipy import *

def preleva(fileName):

    inputDir = "./in/"
    inputFile = open(inputDir + fileName + ".in", "rt")
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()
    MAX, NUM = list(map(int, firstLine.split()))
    inputList = list(map(int, secondLine.split()))

    return MAX, NUM, inputList

def gurobi(MAX, inputList):

    m = gp.Model("mip1")
    expr = LinExpr()
    x = m.addVars(len(inputList), vtype=GRB.BINARY)
    for idx, pizza in enumerate(inputList):
        print(pizza)
        print(x[idx])
        expr.addTerms(pizza, x[idx])
    m.addConstr(expr, GRB.LESS_EQUAL, MAX, 'Fette massime')
    m.setObjective(expr,GRB.MAXIMIZE);
    m.Params.MIPGap = 0
    m.write("model.lp");

    m.optimize();
    #Se voglio stampare l'intero modello e le pizze scelte:
    #print(m)
    #for v in m.getVars():print(v.varName, v.x)
    
    #Ritorno della funzione obiettivo
    obj = m.getObjective()
    #Ne ottengo il valore per il calcolo del punteggio
    return obj.getValue()
    
def greedy(MAX, inputList):

    temp = 0
    pizzaGreedy = 0
    greedySolution = 0
    selectedGreedyPizzas = []
    #Costruzione della prima soluzione
    for pizza in inputList:
        if (temp + pizza) <= MAX:
            temp = temp + pizza
            selectedGreedyPizzas.append(pizza)
            pizzaGreedy += 1

    greedySolution = temp

    #Ricerca migliorativa della soluzione, considerando l'ottimo locale
    selectedLocalPizzas = selectedGreedyPizzas
    localSolution = greedySolution

    unselectedPizzas = list(set(inputList) - set(selectedLocalPizzas))

    j = 0
    
    # j è un indice che mi dichiara il numero di tentativi per migliorare la soluzione
    # chiaramente, più è grande, più i tempi di calcolo sono meno ragionevoli a favore
    # di una ricerca di una soluzione migliore
    
    while (localSolution < MAX and j < 1000):
        indexUnselectedPizza = randrange(len(unselectedPizzas) - 1)
       	indexSelectedPizza = randrange(len(selectedLocalPizzas) - 1)

        #print(indexSelectedPizza)
        selectedLocalPizzas, unselectedPizzas = swap_list(selectedLocalPizzas, unselectedPizzas, indexSelectedPizza, indexUnselectedPizza)

        newLocalSolution = sum(selectedLocalPizzas)

        if newLocalSolution > MAX or newLocalSolution < localSolution:
            selectedLocalPizzas, unselectedPizzas = swap_list(selectedLocalPizzas, unselectedPizzas, indexSelectedPizza, indexUnselectedPizza)
        else:
            localSolution = sum(selectedLocalPizzas)

        #print(selectedLocalPizzas)
        if localSolution == MAX:
            break
        j += 1
    return localSolution

#Definisco una funzione di swap
def swap_list(listA, listB, indexA, indexB):
    t = listA[indexA]
    listA[indexA] = listB[indexB]
    listB[indexB] = t
    return listA, listB
    
total_score = 0
    
ingressi = [
        "a_example",
        "b_small",
        "c_medium",
        "d_quite_big",
        "e_also_big"
	]


print("------------------------\n")
print("Google Hash Code 2020 \n")
print("More Pizza \n")
print("Di: Daniel Parisi e Francesco Ottata \n")
print("------------------------\n")

for input in ingressi:
	MAX, NUM, inputList = preleva(input)
	if MAX>10000 or NUM>250:
		print("Sto usando un approccio Greedy!")
		greedySolution = greedy(MAX, inputList)
		print("Score con approccio Greedy: " + str(greedySolution))
		total_score += greedySolution
	else:
		print("Sto usando Gurobi trovare l'ottimo")
		gurobiSolution = gurobi(MAX, inputList)
		print("Score con Gurobi: " + str(gurobiSolution))
		total_score += gurobiSolution

print("Il punteggio totale e' : " + str(total_score))


