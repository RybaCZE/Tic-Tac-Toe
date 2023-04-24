import tkinter as tk
import ctypes
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font as font
import os

def konec():
    quit()
def clearwin():#makes your screen clear(woooow)
    for widget in root.winfo_children():
        widget.destroy()
class SquareButton(tk.Button):#buttons goo squareee!!!!(used to make buttons with text square)
    def __init__(self, master=None, size=None, **kwargs):
        self.img = tk.PhotoImage()
        tk.Button.__init__(self, master, image=self.img, compound=tk.CENTER, width=size, height=size, **kwargs)

def menu():#pause menu screen
    global menu_button
    clearwin()
    end = tk.Button(root, text="quit", command=konec)
    main_menu = tk.Button(root, text="main menu", command=main_menu_fun)
    back = tk.Button(root, text="continue", command=back_fun)
    end.place(x=200,y=280)
    back.place(x=200,y=220)
    main_menu.place(x=200, y=250)

def replace_button_with_image_continue(button,one_or_null):
    match one_or_null:
        case 0:
            image = Image.open('img/krizek.png')#img path for 1th player
        case 1:
            image = Image.open('img/kolecko.png')#img path for 2nd player
    img_size = canvas_size//3
    image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    button.configure(image=image, bg='white')
    button.image = image
def continue_game():
    button_count = 0
    for o in range(3):
            for k in range(3):
                button_count += 1
                if board[o][k] == 1:
                    player = 1
                    continue_buttons(button_count, player)
                elif board[o][k] ==0:
                    player = 0
                    continue_buttons(button_count, player)
                else:
                    continue

                    
def continue_buttons(button_count, player):
    match button_count:
        case 1:
            replace_button_with_image_continue(btn_1_1, player)
            btn_1_1['state'] = tk.DISABLED
        case 2:
            replace_button_with_image_continue(btn_1_2, player)
            btn_1_2['state'] = tk.DISABLED
        case 3:
            replace_button_with_image_continue(btn_1_3, player)
            btn_1_3['state'] = tk.DISABLED
        case 4:
            replace_button_with_image_continue(btn_2_1, player)
            btn_2_1['state'] = tk.DISABLED
        case 5:
            replace_button_with_image_continue(btn_2_2, player)
            btn_2_2['state'] = tk.DISABLED
        case 6:
            replace_button_with_image_continue(btn_2_3, player)
            btn_2_3['state'] = tk.DISABLED
        case 7:
            replace_button_with_image_continue(btn_3_1, player)
            btn_3_1['state'] = tk.DISABLED
        case 8:
            replace_button_with_image_continue(btn_3_2, player)
            btn_3_2['state'] = tk.DISABLED
        case 9:
            replace_button_with_image_continue(btn_3_3, player)
            btn_3_3['state'] = tk.DISABLED
def back_fun():#remember diffisulty menu
    global game_progress
    # btn_1_1.destroy()
    # btn_1_2.destroy()
    # btn_1_3.destroy()
    # btn_2_1.destroy()
    # btn_2_2.destroy()
    # btn_2_3.destroy()
    # btn_3_1.destroy()
    # btn_3_2.destroy()
    # btn_3_3.destroy()
    game_progress = 1
    match diff:
        case 1:
            lehka()
        case 2:
            stredni()
        case 3:
            tezka()
def main_menu_fun():#main menu screen(play, settings,quit)
    clearwin()
    size = y_res//5
    main_play = tk.Button(root, text="play", command=play)
    main_play.place(x=200,y= 180)
    end = tk.Button(root, text="quit", command=konec)
    settings = tk.Button(root, text="settings", command=nastaveni)
    end.place(x=200,y= 250)
    settings.place(x=200,y= 210)
def nastaveni():#settings(resolution, theme???)
    clearwin()
    if full_scr == False:
        root.geometry("{}x{}".format(x_res, y_res))
        root.attributes('-fullscreen',False)
    elif full_scr ==True:
        root.attributes('-fullscreen',True)
    center(root)
    res_opt = ["800 x 600", "1920 x 1080","1920 x 1200", "full screen"]
    clicked = tk.StringVar()
    clicked.set("resolution") 
    resulution = tk.OptionMenu(root, clicked, *res_opt) 
    Menu_sett = tk.Button(root, text="Menu", command=main_menu_fun)
    resulution.place(x=200, y=200)
    Menu_sett.place(x=200, y=280)
    theme = tk.Button(root, text="theme" )# dodelat 
    save = tk.Button(root, text="save settings", command=nastaveni)
    save.place(x=200,y= 250)
    def res_change(option, value, op):
        global x_res, y_res, full_scr
        selected_value = clicked.get()
        match selected_value:
            case "800 x 600":
                full_scr = False
                x_res = 800
                y_res = 600
            case "1920 x 1080":
                full_scr = False
                x_res = 1920
                y_res = 1080
            case "1920 x 1200":
                full_scr = False
                x_res = 1920
                y_res = 1200
            case "full screen":
                x_res= root.winfo_screenwidth()
                y_res =root.winfo_screenheight()
                full_scr = True
    clicked.trace("w", res_change)
def play():#play menu screen (diffisulty selector)
    global diff_lehka, diff_stredni, diff_tezka, game_progress
    game_progress = 0
    clearwin()
    root.configure(bg="black") #test duvody
    diff_lehka = tk.Button(root, text="easy", command=lehka)
    diff_stredni = tk.Button(root, text="normal", command=stredni)
    diff_tezka = tk.Button(root, text="hard", command=tezka)
    diff_lehka.place(x=200,y= 160)
    diff_stredni.place(x=200,y= 200)
    diff_tezka.place(x=200,y= 240)
def lehka():#ez difficculty
    global diff_lehka, diff_stredni, diff_tezka, menu_button, diff
    clearwin()
    menu_button = tk.Button(root, text="menu", command=menu)
    menu_button.place(x= 5,y=5)
    diff = 1
    play_field(y_res)#do not delete parameter it wont work without it 
def stredni():#medium difficulty
    global diff_lehka, diff_stredni, diff_tezka, menu_button, diff
    clearwin()
    menu_button = tk.Button(root, text="menu", command=menu)
    menu_button.place(x= 5,y=5)
    diff = 2
    play_field(y_res)#do not delete parameter it wont work without it 
def tezka():#hard difficulty
    global diff_lehka, diff_stredni, diff_tezka, menu_button, diff
    clearwin()
    menu_button = tk.Button(root, text="menu", command=menu)
    menu_button.place(x= 5,y=5)
    diff = 3
    play_field(y_res)#do not delete parameter it wont work without it 
def disable_buttons():
    btn_1_1['state'] = tk.DISABLED
    btn_1_2['state'] = tk.DISABLED
    btn_1_3['state'] = tk.DISABLED
    btn_2_1['state'] = tk.DISABLED
    btn_2_2['state'] = tk.DISABLED
    btn_2_3['state'] = tk.DISABLED
    btn_3_1['state'] = tk.DISABLED
    btn_3_2['state'] = tk.DISABLED
    btn_3_3['state'] = tk.DISABLED

def check_win(board):
    # line check
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] is not None:
            if board[row][0] == board[row][1] == board[row][2]:
                disable_buttons()
                return True
    # col check
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] is not None:
            if board[0][col] == board[1][col] == board[2][col]:
                disable_buttons()
                return True
    # diagonal
    if board[0][0] == board[1][1] == board[2][2] is not None:
        if board[0][0] == board[1][1] == board[2][2]:
            disable_buttons()
            return True
    if board[0][2] == board[1][1] == board[2][0] is not None:
        if board[0][2] == board[1][1] == board[2][0]:
            disable_buttons()
            return True
    # draw
    if all(board[row][col] is not None for row in range(3) for col in range(3)):
        return "Draw"
    #if no one made draw or won
    return False


def replace_button_with_image(button):
    img_size = canvas_size//3
    match turn:
        case 0 :
            image = Image.open('img/krizek.png')#img path for 1th player
        case 1:
            image = Image.open('img/kolecko.png')#img path for 2nd player
    image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    button.configure(image=image, bg='white')
    button.image = image
def winner(board):
    result = check_win(board)
    if result is True:
        size = canvas_size //2
        size2 = size // 5
        winner = tk.StringVar(value=f"Player {turn+1} has won")
        label = tk.Label(root, textvariable=winner, font=("DejaVu Sans", 20, "normal"))
        label.place(x=size,y=size- size2)
        play_again = tk.Button(root, text="Play again", command=play)
        go_to_menu = tk.Button(root, text="Main menu", command=main_menu_fun)
        play_again.place(x=size,y=size)
        go_to_menu.place(x=size,y=size + size2)

    elif result == "Draw":
        print("draw")
def chceck_progress():
    global board
    if game_progress ==0:
        board = [[None, None, None],
                [None, None, None],
                [None, None, None]]
    elif game_progress == 1:
        play_field(y_res)
def play_field(y_res):#create play field 
    #do not delete parameter it wont work without it 
    global canvas, canvas_size,board
    if game_progress ==0:
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
    canvas_size = y_res-20
    canvas = tk.Canvas(root, width=y_res-20, height=y_res-20, bg="grey")
    canvas.pack()

    #top to bottom field lines
    x1, x2,y1,y2 = 0,0,0,0
    for i in range(2):
        x1 += (y_res/3) 
        y1 = 0
        x2 += (y_res/3) 
        y2 = y_res-10
        canvas.create_line(x1, y1, x2, y2, fill="white", width=5)
    
    # left to right field lines
    x1, x2,y1,y2 = 0,0,0,0
    for i in range(2):
        y1 += (y_res/3) 
        x1 = 0
        y2 +=(y_res/3)
        x2= y_res-10
        canvas.create_line(x1, y1, x2, y2, fill="white", width=5)
        play_field_buttons(y_res)
def play_field_buttons(y_res):#makes buttons in play field and no i trided to kame it in for loops 
    global turn
    y_res1 = y_res -20
    btn_size = y_res1 //3
    btn_size = btn_size -2
    #btn_radek_sloupex
    global btn_1_1 ,btn_1_2 , btn_1_3, btn_2_1, btn_2_2, btn_2_3, btn_3_1, btn_3_2, btn_3_3
    btn_1_1 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_1_1,1))
    btn_1_2 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_1_2,2))
    btn_1_3 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_1_3,3))
    btn_2_1 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_2_1,4))
    btn_2_2 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_2_2,5))
    btn_2_3 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_2_3,6))
    btn_3_1 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_3_1,7))
    btn_3_2 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_3_2,8))
    btn_3_3 = SquareButton(canvas, size=btn_size, bg='gray' ,command=lambda: place_x_or_o(btn_3_3,9))
    y_res2 = y_res//3
    btn_1_1 .place(x= 1+(y_res2* 0 ),y= 1+(y_res2* 0 ))
    btn_1_2 .place(x= 1+(y_res2* 1 ),y= 1+(y_res2* 0 ))
    btn_1_3 .place(x= 1+(y_res2* 2 ),y= 1+(y_res2* 0 ))
    btn_2_1 .place(x= 1+(y_res2* 0 ),y= 1+(y_res2* 1 ))
    btn_2_2 .place(x= 1+(y_res2* 1 ),y= 1+(y_res2* 1 ))
    btn_2_3 .place(x= 1+(y_res2* 2 ),y= 1+(y_res2* 1 ))
    btn_3_1 .place(x= 1+(y_res2* 0 ),y= 1+(y_res2* 2 ))
    btn_3_2 .place(x= 1+(y_res2* 1 ),y= 1+(y_res2* 2 ))
    btn_3_3 .place(x= 1+(y_res2* 2 ),y= 1+(y_res2* 2 ))
    turn = 0
    if game_progress == 1:
        continue_game()
    
    
def place_x_or_o(position, witch_btn):
    global turn

    match turn:
        case 0:
            turn = 1
            replace_button_with_image(position)
            position['state'] = tk.DISABLED
            match witch_btn:
                case 1:
                    board[0][0]=0
                case 2:
                    board[0][1]=0
                case 3:
                    board[0][2]=0
                case 4:
                    board[1][0]=0
                case 5:
                    board[1][1]=0
                case 6:
                    board[1][2]=0
                case 7:
                    board[2][0]=0
                case 8:
                    board[2][1]=0
                case 9:
                    board[2][2]=0
        case 1:
            turn = 0
            replace_button_with_image(position)
            position['state'] = tk.DISABLED
            match witch_btn:
                case 1:
                    board[0][0]=1
                case 2:
                    board[0][1]=1
                case 3:
                    board[0][2]=1
                case 4:
                    board[1][0]=1
                case 5:
                    board[1][1]=1
                case 6:
                    board[1][2]=1
                case 7:
                    board[2][0]=1
                case 8:
                    board[2][1]=1
                case 9:
                    board[2][2]=1
    winner(board)
def center(win):#makes the window allways be in center not in corner(usefull for bigger resolutions)
    root.update_idletasks()
    width = root.winfo_width()
    frm_width = root.winfo_rootx() - root.winfo_x()
    win_width = width + 2 * frm_width
    height = root.winfo_height()
    titlebar_height = root.winfo_rooty() - root.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = root.winfo_screenwidth() // 2 - win_width // 2
    y = root.winfo_screenheight() // 2 - win_height // 2
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.deiconify()


#makes windows stupid and useful zoom not work on this
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("800x600")
x_res, y_res= 800,600
full_scr = False
root.resizable(False, False)
center(root)
root.configure(bg="black")

main_menu_fun()

#do not delete wont work without it
root.mainloop()
