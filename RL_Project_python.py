import numpy as np
import random
from tkinter import *
import GUI
import value_iteration
import policy_iteration
import Q_learning
        
class index:
    def __init__(self,north,east,south,west,goal,pos,value,best_action):

        self.position = pos
        self.N = bool(north)    
        self.E = bool(east)
        self.S = bool(south)
        self.W = bool(west)
        self.goal = bool(goal)
        self.value = value
        self.best_action = best_action

    def print_index(self):
        print ("position: ",self.position)
        print ("North: ",self.N," East: ",self.E," South: ",self.S," West: ",self.W)
        print ("goal: ",self.goal)
        print ("value: ",self.value)
        print ("best_action: ",self.best_action)  

def main():
    mode = 25
    in_file = open("F:\\AI-1\\projects\\reinforcement learning\\RL_Project_python\\sample_%s.txt"%(mode))
    row_col = in_file.readline().split()
    row = eval(row_col[0])
    column = eval(row_col[1])

    Board = []
    k = 1
    for i in range(row):
        for j in range(column):
            Board.append(index(0,0,0,0,0,k,0,""))
            k += 1

    North = []
    East = []
    South = []
    West = []

    for i in range (0,row * column):
        coordinates = in_file.readline().split()
        North.append(eval(coordinates[0]))
        East.append(eval(coordinates[1]))

        South.append(eval(coordinates[2]))
        West.append(eval(coordinates[3]))
        Board[i].N = coordinates[0]
        Board[i].E = coordinates[1]
        Board[i].S = coordinates[2]
        Board[i].W = coordinates[3]

    temp = in_file.readline().split()

    Source = eval(temp[0])
    goals = []
    for i in range (1,len(temp)):
        goals.append(eval(temp[i]))
        Board[eval(temp[i])-1].goal = TRUE
    
    M = GUI.maze(Board,row,column,North,East,South,West,Source,goals,mode)

    selection= eval(input("1.value iteration\n2.policy iteration\n3.Q_learning\n"))
    if (selection == 1):
        Board = value_iteration.value_iteration(Board,0.0001,row)
    elif (selection == 2):
        Board = policy_iteration.policy_iteration(Board,0.0001,row)
    elif (selection ==3):
        Board = Q_learning.Q_learning(Board,row)

    for i in range (len(Board)):
        Board[i].print_index()
    
    # displaying the policy
    M = GUI.maze(Board,row,column,North,East,South,West,Source,goals,mode)

    # playing the game starting with source point
    current_index = Source-1
    final_points = []

    for i in range(len(goals)):
        final_points.append(goals[i]-1)
        print(final_points[i])
    while (current_index not in final_points):

        if (Board[current_index].best_action == "N"):
            current_index -= 1
            print("N",current_index)
            
            M = GUI.maze(Board,row,column,North,East,South,West,current_index+1,goals,mode)

        elif (Board[current_index].best_action == "E"):
            current_index += row
            print("E",current_index)

            M = GUI.maze(Board,row,column,North,East,South,West,current_index+1,goals,mode)

        elif (Board[current_index].best_action == "S"):
            current_index += 1
            print("S",current_index)

            M = GUI.maze(Board,row,column,North,East,South,West,current_index+1,goals,mode)

        elif (Board[current_index].best_action == "W"):
            current_index -= row
            print("W",current_index)
            
            M = GUI.maze(Board,row,column,North,East,South,West,current_index+1,goals,mode)

main()
        