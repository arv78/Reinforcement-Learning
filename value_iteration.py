from tkinter import *
import policy_iteration

def reward(index):

    if (index.goal == 1):
        return 100
    else:
        return 1

def max_norm(list1,list2):
    max = 0
    for i in range (len(list1)):
        temp = abs(list1[i]-list2[i])
        if (temp > max):
            max = temp
    return max

def arg_max(max_list):
    maximum = -99
    max_index = -1
    for i in range(len(max_list)):
        if (max_list[i] != 0):
            if (max_list[i] >= maximum):
                maximum = max_list[i]
                max_index = i
    return max_index

def value_iteration(Board,epsilon,row):
    gama = 0.7 
    z = 0
    while(TRUE):

        delta = 0

        for i in range(len(Board)):
            max_list = [0,0,0,0]
            best_action_value = 0
            if (Board[i].N == "1"):
                max_list[0] = reward(Board[i-1]) + gama * Board[i-1].value
            if (Board[i].E == "1"):
                max_list[1] = reward(Board[i+row]) + gama * Board[i+row].value
            if (Board[i].S == "1"):
                max_list[2] = reward(Board[i+1]) + gama * Board[i+1].value
            if (Board[i].W == "1"):
                max_list[3] = reward(Board[i-row]) + gama * Board[i-row].value

            # print(max_list[0]," ",max_list[1]," ",max_list[2]," ",max_list[3])

            best_action_value = max(max_list)

            delta = max(delta,abs(best_action_value - Board[i].value))
            
            Board[i].value = best_action_value

            max_index = arg_max(max_list)

            if (max_index == 0):
                Board[i].best_action = "N"
            elif (max_index == 1):
                Board[i].best_action = "E"
            elif (max_index == 2):
                Board[i].best_action = "S"
            else:
                Board[i].best_action = "W"

        if (delta < epsilon * (1 - gama)/gama):
                break
        z += 1
    print("z: ",z)
    
    return Board