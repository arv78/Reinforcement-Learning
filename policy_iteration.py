import random
import value_iteration
from tkinter import *

def reward(index):
    if (index.goal == 1):
        return 100
    else:
        return 1

def arg_max(max_list):
    maximum = -99
    max_index = -1
    for i in range(len(max_list)):
        if (max_list[i] >= maximum):
            maximum = max_list[i]
            max_index = i
    return max_index

def policy_evaluation(Board,epsilon,row):
    gama = 0.7
    z = 0

    while(TRUE):
        delta = 0
        v_new = []
        for i in range(len(Board)):
            v_new.append(0)

        for i in range(len(Board)):
            v_fn = 0
            # count = count_actions(Board[i])
            # high_prob = count/(count+1)
            # if (count == 1):
            #     low_prob = 0
            # else:
            #     low_prob = (1 - high_prob)/count-1

            if (Board[i].best_action == "N"):
                v_fn += reward(Board[i-1]) + gama * Board[i-1].value
                # if (Board[i].E == "1"):
                #     max_list[0] += low_prob * (reward(Board[i+row]) + gama * values[i+row])
                # if (Board[i].S == "1"):
                #     max_list[0] += low_prob * (reward(Board[i+1]) + gama * values[i+1])
                # if (Board[i].W == "1"):
                #     max_list[0] += low_prob * (reward(Board[i-row]) + gama * values[i-row])

            elif (Board[i].best_action == "E"):
                v_fn += reward(Board[i+row]) + gama * Board[i+row].value
                # if (Board[i].N == "1"):
                #     max_list[1] += low_prob * (reward(Board[i-1]) + gama * values[i-1])
                # if (Board[i].S == "1"):
                #     max_list[1] += low_prob * (reward(Board[i+1]) + gama * values[i+1])
                # if (Board[i].W == "1"):
                #     max_list[1] += low_prob * (reward(Board[i-row]) + gama * values[i-row])

            elif (Board[i].best_action == "S"):
                v_fn += reward(Board[i+1]) + gama * Board[i+1].value
                # if (Board[i].E == "1"):
                #     max_list[2] += low_prob * (reward(Board[i+row]) + gama * values[i+row])
                # if (Board[i].N == "1"):
                #     max_list[2] += low_prob * (reward(Board[i-1]) + gama * values[i-1])
                # if (Board[i].W == "1"):
                #     max_list[2] += low_prob * (reward(Board[i-row]) + gama * values[i-row])

            elif (Board[i].best_action == "W"):
                v_fn += reward(Board[i-row]) + gama * Board[i-row].value
                # if (Board[i].E == "1"):
                #     max_list[3] += low_prob * (reward(Board[i+row]) + gama * values[i+row])
                # if (Board[i].S == "1"):
                #     max_list[3] += low_prob * (reward(Board[i+1]) + gama * values[i+1])
                # if (Board[i].N == "1"):
                #     max_list[3] += low_prob * (reward(Board[i-1]) + gama * values[i-1])

            # print(max_list[0]," ",max_list[1]," ",max_list[2]," ",max_list[3])

            delta = max(delta,abs(v_fn - Board[i].value))

            v_new[i] = v_fn
        
        for j in range(len(Board)):
            Board[j].value = v_new[j]

        z += 1

        if (delta < epsilon * (1 - gama)/gama):
                break
    # print("z: ",z)
    return Board

# this function returns all the action values
def values_action(Board,state,gama,row):

    max_arg = [0,0,0,0]

    if (state.N == "1"):
        max_arg[0] = reward(Board[(state.position-1)-1]) + gama * Board[(state.position-1)-1].value
    if (state.E == "1"):
        max_arg[1] = reward(Board[(state.position-1)+row]) + gama * Board[(state.position-1)+row].value
    if (state.S == "1"):
        max_arg[2] = reward(Board[(state.position-1)+1]) + gama * Board[(state.position-1)+1].value
    if (state.W == "1"):
        max_arg[3] = reward(Board[(state.position-1)-row]) + gama * Board[(state.position-1)-row].value

    return max_arg

def valid_actions(state):
    v_actions = []
    if (state.N == "1"):
        v_actions.append("N")
    if (state.E == "1"):
        v_actions.append("E")
    if (state.S == "1"):
        v_actions.append("S")
    if (state.W == "1"):
        v_actions.append("W")

    return v_actions
# policy improvement
def policy_iteration(Board,epsilon,row):
    gama = 0.7
    # makeing random policy
    for i in range(len(Board)):
        v_actions = valid_actions(Board[i])
        if (len(v_actions) != 0):
            if (len(v_actions) == 1):
                random_num = 0
            else:
                random_num = random.randint(0,len(v_actions)-1)
            Board[i].best_action = v_actions[random_num]

    action_values = []
    for k in range(len(Board)):
        action_values.append(0)
    while (TRUE):
        # values = []
        # random values
        Board = policy_evaluation(Board,epsilon,row)
        unchanged = TRUE

        for i in range (len(Board)):
            action_values = values_action(Board,Board[i],gama,row)
            best_action = arg_max(action_values)
            # choosing the chosen action of the policy
            if (Board[i].best_action == "N"):
                chosen_action = 0
            if (Board[i].best_action == "E"):
                chosen_action = 1
            if (Board[i].best_action == "S"):
                chosen_action = 2
            if (Board[i].best_action == "W"):
                chosen_action = 3
            

            if (chosen_action != best_action):
                unchanged = FALSE
                
            # print("chosen_action: ",chosen_action," best_action: ",best_action)
            # chosen_action = best_action
            if (best_action == 0):
                Board[i].best_action = "N"
            if (best_action == 1):
                Board[i].best_action = "E"
            if (best_action == 2):
                Board[i].best_action = "S"
            if (best_action == 3):
                Board[i].best_action = "W"
            
        # print("________________________________")
        if (unchanged):
            return Board