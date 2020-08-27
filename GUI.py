from tkinter import *

class cell:
    def __init__(self,best_action,n,e,s,w,Canvas,i,j,current_cell,source,goals,r,c):
        
        if (current_cell == source):
            Canvas.create_text((i*50*(5/c))+25,(j*50*(5/r))+25,text="S",fill="red",font="Times 20 bold")
        for k in range (0,len(goals)):
            if (current_cell == goals[k]):
                Canvas.create_text((i*50*(5/c))+25,(j*50*(5/r))+25,text="G",fill="red",font="Times 20 bold")
                best_action = ""
        if (n == 0):
            Canvas.create_line(i*50*(5/c),j*50*(5/r),(i*50*(5/c))+50,j*50*(5/r),width = 3)
        else:
            Canvas.create_line(i*50*(5/c),j*50*(5/r),(i*50*(5/c))+50,j*50*(5/r),width = 2,dash=(3,5))
        if (e == 0):
            Canvas.create_line((i*50*(5/c))+50,j*50*(5/r),(i*50*(5/c))+50,(j*50*(5/r))+50,width = 3)
        else:
            Canvas.create_line((i*50*(5/c))+50,j*50*(5/r),(i*50*(5/c))+50,(j*50*(5/r))+50,width = 2,dash=(3,5))
        if (s == 0):
            Canvas.create_line(i*50*(5/c),(j*50*(5/r))+50,(i*50*(5/c))+50,(j*50*(5/r))+50,width = 3)
        else:
            Canvas.create_line(i*50*(5/c),(j*50*(5/r))+50,(i*50*(5/c))+50,(j*50*(5/r))+50,width = 2,dash=(3,5))
        if (w == 0):
            Canvas.create_line(i*50*(5/c),j*50*(5/r),i*50*(5/c),(j*50*(5/r))+50,width = 3)
        else:
            Canvas.create_line(i*50*(5/c),j*50*(5/r),i*50*(5/c),(j*50*(5/r))+50,width = 2,dash=(3,5))
        if (best_action != ""):
            if (best_action == "N"):
                Canvas.create_line((i*50*(5/c))+20,(j*50*(5/r))+10,(i*50*(5/c))+20,(j*50*(5/r))-10,arrow=LAST,fill="red")
            if (best_action == "E"):
                Canvas.create_line((i*50*(5/c))+40,(j*50*(5/r))+30,(i*50*(5/c))+60,(j*50*(5/r))+30,arrow=LAST,fill="red")
            if (best_action == "S"):
                Canvas.create_line((i*50*(5/c))+30,(j*50*(5/r))+40,(i*50*(5/c))+30,(j*50*(5/r))+60,arrow=LAST,fill="red")
            if (best_action == "W"):
                Canvas.create_line(i*50*(5/c)+10,j*50*(5/r)+20,i*50*(5/c)-10,j*50*(5/r)+20,arrow=LAST,fill="red")

class cell_25:
    def __init__(self,best_action,n,e,s,w,Canvas,i,j,current_cell,source,goals,r,c):
        
        if (current_cell == source):
            Canvas.create_text((i*25)+12,(j*25)+12,text="S",fill="red",font="Times 10 bold")
        for k in range (0,len(goals)):
            if (current_cell == goals[k]):
                Canvas.create_text((i*25)+12,(j*25)+12,text="G",fill="red",font="Times 10 bold")
                best_action = ""
        if (n == 0):
            Canvas.create_line(i*25,j*25,(i*25)+25,j*25,width = 3)
        else:
            Canvas.create_line(i*25,j*25,(i*25)+25,j*25,width = 2,dash=(3,5))
        if (e == 0):
            Canvas.create_line((i*25)+25,j*25,(i*25)+25,(j*25)+25,width = 3)
        else:
            Canvas.create_line((i*25)+25,j*25,(i*25)+25,(j*25)+25,width = 2,dash=(3,5))
        if (s == 0):
            Canvas.create_line(i*25,(j*25)+25,(i*25)+25,(j*25)+25,width = 3)
        else:
            Canvas.create_line(i*25,(j*25)+25,(i*25)+25,(j*25)+25,width = 2,dash=(3,5))
        if (w == 0):
            Canvas.create_line(i*25,j*25,i*25,(j*25)+25,width = 3)
        else:
            Canvas.create_line(i*25,j*25,i*25,(j*25)+25,width = 2,dash=(3,5))
        if (best_action != ""):
            if (best_action == "N"):
                Canvas.create_line((i*25)+10,(j*25)+5,(i*25)+10,(j*25)-5,arrow=LAST,fill="red")
            if (best_action == "E"):
                Canvas.create_line((i*25)+20,(j*25)+20,(i*25)+30,(j*25)+20,arrow=LAST,fill="red")
            if (best_action == "S"):
                Canvas.create_line((i*25)+20,(j*25)+20,(i*25)+20,(j*25)+30,arrow=LAST,fill="red")
            if (best_action == "W"):
                Canvas.create_line((i*25)+5,(j*25)+10,(i*25)-5,(j*25)+10,arrow=LAST,fill="red")

class maze:
    def __init__(self,Board,row,column,North,East,South,West,Source,goals,mode):
        self.window = Tk()

        # middle window
        if (mode == 5):
            window_height = 395
            window_width = 350
        elif (mode == 25):
            window_height = 800
            window_width = 1000
        window_height = int(window_height)
        window_width = int(window_width)
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.title("Maze")
        self.Board = Board
        self.r = row
        self.c = column
        self.North = North
        self.East = East
        self.South = South
        self.West = West
        self.source = Source
        self.goals = goals
        self.mode = mode

        if (self.mode == 5):
            self.canvas = Canvas(self.window, width = 350,height = 350,bg = "lightsky blue")
        elif (self.mode == 25):
            self.canvas = Canvas(self.window, width = 1000,height = 755,bg = "lightsky blue")
        self.canvas.grid(row = 1, column = 1, columnspan = 3)
        self.make_maze()
        bt_start = Button(self.window,text = "Go",bg="lightblue",fg="red",font="Times 15 bold",command = self.window.destroy).grid(row=2,column=2,rowspan=2)
        self.window.mainloop()

    def make_maze(self):
        z = 1
        for i in range (1, self.c +1):
            for j in range (1, self.r +1):
                if (self.mode == 5):
                    C = cell(self.Board[z-1].best_action,self.North[z-1], self.East[z-1], self.South[z-1], self.West[z-1], self.canvas, i, j, z, self.source,self.goals,self.r,self.c)
                elif (self.mode == 25):
                    C = cell_25(self.Board[z-1].best_action,self.North[z-1], self.East[z-1], self.South[z-1], self.West[z-1], self.canvas, i, j, z, self.source,self.goals,self.r,self.c) 
                z += 1