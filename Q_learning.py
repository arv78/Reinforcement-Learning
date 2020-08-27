import random

def reward(index):
    if (index.goal == 1):
        return 100
    else:
        return 0

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

def max_next(Board,Q,index):
    v_a = valid_actions(Board[index])
    maximum = -1
    for i in range (len(v_a)):
        for j in range (len(Q)):
            if (index == Q[j][0] and v_a[i] == Q[j][1]):
                if (Q[j][2] >= maximum):
                    maximum = Q[j][2]
                break
    return maximum

def Q_learning(Board,row):
    Q = []
    gama = 0.7
    for i in range (len(Board)):
        v_actions = valid_actions(Board[i])
        for j in range (len(v_actions)):
            Q.append([i,v_actions[j],0])
    # p = 0
    # i = 0
    # while (i < 25):
    #     while (Q[p][0] == i):
    #         print(Q[p][0],Q[p][1],Q[p][2])
    #         p += 1
    #     i += 1
    #     print("______________")

    for i in range (len(Board)):
        current = i
        next_state = current
        thresh = 5
        print(i)
        while (True):

            chosen_action = ""
            # choosing a random action between valid actions for each state
            v_actions = valid_actions(Board[current])
            if (len(v_actions) != 0):
                if (len(v_actions) == 1):
                    random_num = 0
                else:
                    random_num = random.randint(0,len(v_actions)-1)
                chosen_action = v_actions[random_num]

            if (chosen_action == "N"):
                next_state = current - 1
            elif (chosen_action == "E"):
                next_state = current + row
            elif (chosen_action == "S"):
                next_state = current + 1
            elif (chosen_action == "W"):
                next_state = current - row

            for j in range (len(Q)):
                if (current == Q[j][0] and chosen_action == Q[j][1]):
                    Q[j][2] = reward(Board[next_state]) + gama * max_next(Board,Q,next_state)
                    break
            if (i == next_state):
                thresh -= 1

            if (Board[next_state].goal == 1):
                break
            if (thresh == 0):
                break
            current = next_state

    # now we want to calculate the policy
    for i in range (len(Board)):
        max_list = []
        for j in range(len(Q)):
            if (i == Q[j][0]):
                max_list.append(Q[j])
        maximum = -99
        for j in range(len(max_list)):
            if (max_list[j][2] >= maximum):
                maximum = max_list[j][2]
                best_action = max_list[j][1]
        Board[i].best_action = best_action

    return Board