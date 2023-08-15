from tkinter import *
from random import *
from tkinter import messagebox
import time
import json
root = Tk()
root.title("Minesweeper")
root.config(bg="#D4FBFF")


# initial values
y_len = 10                 # size of grid 
x_len = 10                 # size of grid
chance = 10                # percentage of tiles to be mines
base_color = "#7EE6FC"
move_color = "blue"
flag_color = "#CB0C0C"
blast_color = "#D4FBFF"


prev_color = base_color

all_b = []
mine_b = []
safe_b = []

co_m = 0
co_red = 0

c_time = time.time()

def exit(eff, current_b, row, column):
    global p_color

    current_b["bg"] = p_color

def enter(eff, current_b, row, column):
    global p_color
    global current

    p_color = current_b["bg"]

    if current_b["bg"] != flag_color: current_b["bg"] = move_color

    current = [row, column]

def place_flag(eff, current_b, row, column):
    global p_color,co_m,co_red
    
    if eff.num == 3 and current_b["text"] == "  ":
        if p_color != flag_color:
            current_b["bg"] = flag_color
            p_color = flag_color
            if current_b in mine_b: co_m +=1
            co_red+=1
        elif p_color == flag_color:
            current_b["bg"] = base_color
            p_color = base_color
            if current_b in mine_b: co_m -=1
            co_red-=1

    if co_m==len(mine_b) and co_m == co_red:
        ending('Win')
    

# making and saving buttons
for i in range(1, y_len + 1):
    for j in range(1, x_len + 1):
        b = Button(root, bg=base_color, text="  ")
        b.grid(row=i, column=j, ipadx=15, ipady=5)
        b.bind("<Enter>", lambda eff, i=i, j=j, b=b: enter(eff, current_b=b, row=i, column=j))
        b.bind("<Leave>", lambda eff, i=i, j=j, b=b: exit(eff, current_b=b, row=i, column=j))
        b.bind("<Button>", lambda eff, i=i, j=j, b=b: place_flag(eff, current_b=b, row=i, column=j))
        all_b.append(b)

# making mines
tri_list = []
for a in range(101):
    tri_list.append(a)
for b in all_b:
    if choice(tri_list) <= chance:
        mine_b.append(b)
    else:
        safe_b.append(b)

def clicked():
    global p_color
    current_b = all_b[(x_c() - 1) * x_len + y_c() - 1]
    if current_b["bg"] == flag_color:
        return

    if co_m==len(mine_b) and co_m == co_red:
        ending('Win')

    if current_b in mine_b:
        ending('Lose')
    else:
        current_b["bg"] = blast_color
        p_color = blast_color

        m = x_len * y_len
        num = 0
        l = []


        if x_c() == 1 and y_c() == 1:
            l.append(all_b[1])
            l.append(all_b[x_len])
            l.append(all_b[x_len + 1])
        elif x_c() == 1 and y_c() == x_len:
            l.append(all_b[x_len + x_len - 2 ])
            l.append(all_b[x_len + x_len - 1 ])
            l.append(all_b[x_len - 2])
        elif x_c() == y_len and y_c() == 1:
            l.append(all_b[(x_c() - 1) * x_len + y_c()])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  - x_len])
        elif x_c() == y_len and y_c() == x_len:
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  - 2 - x_len])

        elif x_c() == 1:
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2])
            l.append(all_b[(x_c() - 1) * x_len + y_c()])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2 + x_len])
        elif x_c() == y_len:
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2])
            l.append(all_b[(x_c() - 1) * x_len + y_c()])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2 - x_len])
        elif y_c() == 1:
            l.append(all_b[(x_c() - 1) * x_len + y_c() + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  - 1 - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  - x_len])
        elif y_c() == x_len:
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2  + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  - 1 - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c()  -2 - x_len])
        else:
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 + 1])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 - 1])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 1 - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2 + x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - x_len])
            l.append(all_b[(x_c() - 1) * x_len + y_c() - 2 - x_len])


        for b in l:
            if b in mine_b:
                num += 1

        current_b["text"] = num

        win = True

        for b in all_b:
            if b["bg"] == base_color:
                win = False
        if win:
            ending('Win')

def submit(name, total_tame):
    f= open('data.json',"r")

    j = json.load(f)
    j['name'].append(name)
    j['time'].append(total_tame)
    # j = {"name": [name], "time": [total_tame]}     # Comment the above two line and uncomment this line to overwrite the file
    f.close()
    f= open('data.json',"w")

    
    json.dump(j, f)
    f.close()

    # f.write(f"{name} - {total_tame}")
    root.destroy()

def ending(wi_lo):
    global root1
    e_ti = time.time()
    total_tame = -(c_time - e_ti)
    total_tame = round(total_tame,3)

    if wi_lo == 'Win':
        messagebox.showinfo("You win", f"You Win!!!, {total_tame}s")

    if wi_lo == 'Lose':
        messagebox.showinfo("Game over", f"You Lost!!!, {total_tame}s")
        quit()


    root.withdraw()
    root1 = Toplevel(root)


    root1.title("Name")
    root1.geometry("300x100")

    e = Entry(root1)
    e.pack()
    e.focus()
    
    Button(root1, text="Submit", command=lambda: submit(e.get(), total_tame)).pack()

            
    root1.mainloop()


#uncomment to show the mines on screen 
# for b in mine_b:
#    b["bg"] = "green"

for b in all_b:
    b["command"] = clicked

current = [1, 1]

x_c = lambda: current[0]
y_c = lambda: current[1]

root.mainloop()
