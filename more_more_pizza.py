from random import randrange
import gurobipy as gp
from gurobipy import *

def preleva(fileName):
    inputDir = "./in/"
    inputFile = open(inputDir + fileName + ".in", "rt")

    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()


    MAX, NUM = list(map(int, firstLine.split()))

    #  Create the pizza list by reading the file
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
    print(m)
    for v in m.getVars():print(v.varName, v.x)
def greedy(MAX, inputList):
    temp = 0
    pizzaGreedy = 0
    greedySolution = 0
    selectedGreedyPizzas = []

    for pizza in inputList:
        if (temp + pizza) <= MAX:
            temp = temp + pizza
            selectedGreedyPizzas.append(pizza)
            pizzaGreedy += 1

    greedySolution = temp

    # Ottimizzazione dello pseudo-greedy
    selectedLocalPizzas = selectedGreedyPizzas
    localSolution = greedySolution

    unselectedPizzas = list(set(inputList) - set(selectedLocalPizzas))

    j = 0
    while (localSolution < MAX and j < 1000):
        indexUnselectedPizza = randrange(len(unselectedPizzas) - 1)
        indexSelectedPizza = randrange(len(selectedLocalPizzas) - 1)

        print(indexSelectedPizza)
        selectedLocalPizzas, unselectedPizzas = swap_list(selectedLocalPizzas, unselectedPizzas, indexSelectedPizza, indexUnselectedPizza)

        newLocalSolution = sum(selectedLocalPizzas)

        if newLocalSolution > MAX or newLocalSolution < localSolution:
            selectedLocalPizzas, unselectedPizzas = swap_list(selectedLocalPizzas, unselectedPizzas, indexSelectedPizza, indexUnselectedPizza)
        else:
            localSolution = sum(selectedLocalPizzas)

        print(selectedLocalPizzas)
        if localSolution == MAX:
            break
        j += 1
    return localSolution

def swap_list(listA, listB, indexA, indexB):
    t = listA[indexA]
    listA[indexA] = listB[indexB]
    listB[indexB] = t
    return listA, listB


MAX, NUM, inputList = preleva('b_small')

#print("Lancio il greedy, figli di puttana:")
#greedySolution = greedy(MAX, inputList)
#print(greedySolution)

gurobi(MAX, inputList)
