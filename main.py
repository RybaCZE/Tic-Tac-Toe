import tkinter as tk
import ctypes
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font as font
import os
import random

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
    position = y_res//2
    spacing= 10+(position//10)
    clearwin()
    end = tk.Button(root,bg='black', fg='white', text="quit", command=konec)
    main_menu = tk.Button(root,bg='black',fg='white', text="main menu", command=main_menu_fun)
    back = tk.Button(root,bg='black',fg='white', text="continue", command=back_fun)
    back.place(x=position,y=position- spacing- spacing)
    main_menu.place(x=position, y=position- spacing)
    end.place(x=position, y=position)
    back['font'] = main_font
    main_menu['font'] = main_font
    end['font'] = main_font
def replace_button_with_image_continue(button,one_or_null):
    match one_or_null:
        case 1:
            image = Image.open('img/krizek.png')#img path for 1th player
        case 0:
            image = Image.open('img/kolecko.png')#img path for 2nd player
    img_size = canvas_size//3
    image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    button.configure(image=image, bg='white')
    button.image = image
def play_as():
    clearwin()
    player = None
    circle = Image.open('img/kolecko.png')#0
    cross = Image.open('img/krizek.png')#1
    img_size = y_res//3
    
    circle = circle.resize((img_size, img_size), resample=Image.LANCZOS)
    cross = cross.resize((img_size, img_size), resample=Image.LANCZOS)
    play_as_label = tk.Label(root, text="Who do you want to play as?")
    play_as_circle = tk.Button(root, anchor="w", command=lambda: player_is(1))
    play_as_cross = tk.Button(root, anchor="e", command=lambda: player_is(2))
    play_as_label['font']= main_font
    circle_tk = ImageTk.PhotoImage(circle)
    cross_tk = ImageTk.PhotoImage(cross)
    play_as_circle.config(image=circle_tk, width=img_size, height=img_size)
    play_as_cross.config(image=cross_tk, width=img_size, height=img_size)
    play_as_circle.image = circle_tk
    play_as_cross.image = cross_tk
    play_as_label.config(font=main_font)
    play_as_label.place(relx=0.5, rely=0.3, anchor="center")
    play_as_circle.place(relx=0.25, rely=0.5, anchor="center")
    play_as_cross.place(relx=0.75, rely=0.5, anchor="center")
def player_is(player_fun):
    global player, turn
    if player_fun == 1:
        player = 0
        turn = 0
    elif player_fun == 2:
        player =1
        turn = 1
    match diff:
        case 1:

            menu_button_fun()
        case 2:
            menu_button_fun()
        case 3:
            menu_button_fun()

def continue_game():
    button_count = 0
    for o in range(3):
            for k in range(3):
                button_count += 1
                if board[o][k] == 1:
                    player_con = 1
                    continue_buttons(button_count, player_con)
                elif board[o][k] ==0:
                    player_con = 0
                    continue_buttons(button_count, player_con)
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

    game_progress = 1
    match diff:
        case 0:
            play_w_friend()
        case 1:
            lehka()
        case 2:
            stredni()
        case 3:
            tezka()
        
def main_menu_fun():#main menu screen(play, settings,quit)
    clearwin()
    position = y_res//2
    spacing= 10+(position//10)
    size = y_res//5
    main_play = tk.Button(root, bg='black',fg='white',text="play", command=play)
    end = tk.Button(root, bg='black',fg='white',text="quit", command=konec)
    settings = tk.Button(root,bg='black', fg='white',text="settings", command=nastaveni)
    main_play.place(x=position,y= position-spacing-spacing)
    end.place(x=position,y= position)
    settings.place(x=position,y= position-spacing)
    main_play['font'] = main_font
    settings['font'] = main_font
    end['font'] = main_font
def nastaveni():#settings(resolution, theme???)
    clearwin()
    if full_scr == False:
        root.geometry("{}x{}".format(x_res, y_res))
        root.attributes('-fullscreen',False)
    elif full_scr ==True:
        root.attributes('-fullscreen',True)
    center(root)
    position = y_res//2
    spacing= 10+(position//10)
    res_opt = ["800 x 600", "1920 x 1080","1920 x 1200", "full screen"]
    clicked = tk.StringVar()
    clicked.set("resolution") 
    resulution = tk.OptionMenu(root, clicked, *res_opt) 
    Menu_sett = tk.Button(root,bg='black',fg='white', text="Menu", command=main_menu_fun)
    resulution.place(x=position, y=position- spacing-spacing)
    Menu_sett.place(x= position, y=position- spacing)
    save = tk.Button(root,bg='black',fg='white', text="save settings", command=nastaveni)
    resulution.config(bg="black",fg="white" ,activebackground="black", activeforeground="white")
    resulution["menu"].config(bg="black",fg="white" ,activebackground="black", activeforeground="gray")
    save.place(x=position,y= position)
    save['font'] = main_font
    Menu_sett['font'] = main_font
    resulution['font'] = main_font
    def res_change(option, value, op):
        global x_res, y_res, full_scr, main_font
        selected_value = clicked.get()
        match selected_value:
            case "800 x 600":
                full_scr = False
                x_res = 800
                y_res = 600
                font_size = y_res//60
                main_font = font.Font(family='DejaVu Sans', size=font_size )
            case "1920 x 1080":
                full_scr = False
                x_res = 1920
                y_res = 1080
                font_size = y_res//60
                main_font = font.Font(family='DejaVu Sans', size=font_size )
            case "1920 x 1200":
                full_scr = False
                x_res = 1920
                y_res = 1200
                font_size = y_res//60
                main_font = font.Font(family='DejaVu Sans', size=font_size )
            case "full screen":
                x_res= root.winfo_screenwidth()
                y_res =root.winfo_screenheight()
                font_size = y_res//60
                main_font = font.Font(family='DejaVu Sans', size=font_size )
                full_scr = True
    clicked.trace("w", res_change)
def play():#play menu screen (diffisulty selector)
    global diff_easy, diff_medium, diff_hard, game_progress
    game_progress = 0
    clearwin()
    root.configure(bg="black") #test duvody
    play_with_friend = tk.Button(root, bg='black',fg='white',text="Local play with friend", command=play_w_friend)
    diff_easy = tk.Button(root,bg='black',fg='white', text="Easy", command=lehka)
    diff_medium = tk.Button(root,bg='black',fg='white', text="Normal", command=stredni)
    diff_hard = tk.Button(root,bg='black', fg='white',text="Hard", command=tezka)
    position = y_res//2
    spacing= 10+(position//10)
    play_with_friend.place(x=position,y=position- spacing- spacing- spacing)
    diff_easy.place(x=position,y= position - spacing- spacing)
    diff_medium.place(x=position,y= position- spacing)
    diff_hard.place(x=position,y=position)
    play_with_friend['font'] = main_font
    diff_easy['font'] = main_font
    diff_medium['font'] = main_font
    diff_hard['font'] = main_font
def play_w_friend():
    global diff_easy, diff_medium, diff_hard, menu_button, diff
    clearwin()
    menu_button = tk.Button(root, bg='black',fg='white',text="menu", command=menu)
    menu_button.place(x= 5,y=5)
    menu_button['font'] = main_font
    diff = 0
    play_field(y_res)#do not delete parameter it wont work without it 
def lehka():#ez difficculty
    global diff_easy, diff_medium, diff_hard, menu_button, diff
    diff = 1
    play_as()

def stredni():#medium difficulty
    global diff_easy, diff_medium, diff_hard, menu_button, diff
    diff = 2
    play_as()

def tezka():#hard difficulty
    global diff_easy, diff_medium, diff_hard, menu_button, diff
    diff = 3
    play_as()

def menu_button_fun():
    clearwin()
    menu_button = tk.Button(root,bg='black', fg='white', text="menu", command=menu)
    menu_button.place(x= 5,y=5)
    menu_button['font'] = main_font
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
    y_res1 = y_res -20
    img_size = y_res1 //3 - 2
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
    position = y_res//2
    spacing= 10+(position//10)
    if result is True:
        if turn ==0:
            player_won = "circles"
        elif turn == 1:
            player_won= "crosses"
        winner = tk.StringVar(value=f"Player {player_won} has won")
        label = tk.Label(root, textvariable=winner, font=("DejaVu Sans", 20, "normal"))
        label.place(x=position,y=position-spacing-spacing-10)
        play_again = tk.Button(root,bg='black', fg='white',text="Play again", command=play)
        go_to_menu = tk.Button(root,bg='black', fg='white',text="Main menu", command=main_menu_fun)
        play_again.place(x=position,y=position-spacing)
        play_again['font'] = main_font
        go_to_menu['font'] = main_font
        go_to_menu.place(x=position,y=position)
    elif result == "Draw":
        winner = tk.StringVar(value=f"That's a draw")
        label = tk.Label(root, textvariable=winner, font=("DejaVu Sans", 20, "normal"))
        label.place(x=position,y=position-spacing-spacing-10)
        play_again = tk.Button(root,bg='black', fg='white', text="Play again", command=play)
        go_to_menu = tk.Button(root, bg='black',fg='white', text="Main menu", command=main_menu_fun)
        play_again.place(x=position,y=position-spacing)
        go_to_menu.place(x=position,y=position)
        play_again['font'] = main_font
        go_to_menu['font'] = main_font

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
    canvas_size = y_res-10
    canvas_padding = (y_res - canvas_size) // 2
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
    canvas.place(relx=0.5, rely=0.5, anchor='center')
    #canvas.pack(side="top", padx=canvas_padding, pady=canvas_padding)

    #top to bottom field lines


    x1, x2,y1,y2 = 0,0,0,0
    for i in range(2):
        x1 += ((canvas_size/3)-5) 
        y1 = 0
        x2 += ((canvas_size/3)-5) 
        y2 = canvas_size-10
        canvas.create_line(x1, y1, x2, y2, fill="white", width=1)
    
    # left to right field lines
    x1, x2,y1,y2 = 0,0,0,0
    for i in range(2):
        y1 += ((canvas_size/3)-5) 
        x1 = 0
        y2 +=((canvas_size/3)-5)
        x2= canvas_size-10
        canvas.create_line(x1, y1, x2, y2, fill="white", width=1)
        play_field_buttons(y_res)
def play_field_buttons(y_res):#makes buttons in play field 
    global turn, bot_turns
    y_res1 = y_res -20
    btn_size = y_res1 //3 - 2

    #btn_row_colum
    global btn_1_1 ,btn_1_2 , btn_1_3, btn_2_1, btn_2_2, btn_2_3, btn_3_1, btn_3_2, btn_3_3
    btn_1_1 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_1_1,1))
    btn_1_2 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_1_2,2))
    btn_1_3 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_1_3,3))
    btn_2_1 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_2_1,4))
    btn_2_2 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_2_2,5))
    btn_2_3 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_2_3,6))
    btn_3_1 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_3_1,7))
    btn_3_2 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_3_2,8))
    btn_3_3 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda: place_x_or_o(btn_3_3,9))
    y_res2 = y_res//3
    btn_1_1.place(x=1+(y_res2*0),y=1+(y_res2*0))
    btn_1_2.place(x=1+(y_res2*1),y=1+(y_res2*0))
    btn_1_3.place(x=1+(y_res2*2),y=1+(y_res2*0))
    btn_2_1.place(x=1+(y_res2*0),y=1+(y_res2*1))
    btn_2_2.place(x=1+(y_res2*1),y=1+(y_res2*1))
    btn_2_3.place(x=1+(y_res2*2),y=1+(y_res2*1))
    btn_3_1.place(x=1+(y_res2*0),y=1+(y_res2*2))
    btn_3_2.place(x=1+(y_res2*1),y=1+(y_res2*2))
    btn_3_3.place(x=1+(y_res2*2),y=1+(y_res2*2))

    if game_progress == 1:
        continue_game()
    bot_turns = []
    if diff == 1:
        whos_playing()
        

def ez_bot_play():
    global bot_turns
    
    if turn != player:
        while True:
            bot_ez = random.randint(1,9)
            if bot_ez not in bot_turns:
                match bot_ez:
                    case 1:
                        btn_1_1.invoke()
                    case 2:
                        btn_1_2.invoke()
                    case 3:
                        btn_1_3.invoke()
                    case 4:
                        btn_2_1.invoke()
                    case 5:
                        btn_2_2.invoke()
                    case 6:
                        btn_2_3.invoke()
                    case 7:
                        btn_3_1.invoke()
                    case 8:
                        btn_3_2.invoke()
                    case 9:
                        btn_3_3.invoke()
                break
            else:
                continue
def whos_playing():
    match diff:
        case 1:
            if turn != player:
                ez_bot_play()
            elif turn == player:
                pass
        case 2:
            pass
        case 3:
            pass


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
                    bot_turns.append(1)
                case 2:
                    board[0][1]=0
                    bot_turns.append(2)
                case 3:
                    board[0][2]=0
                    bot_turns.append(4)
                case 4:
                    board[1][0]=0
                    bot_turns.append(4)
                case 5:
                    board[1][1]=0
                    bot_turns.append(5)
                case 6:
                    board[1][2]=0
                    bot_turns.append(6)
                case 7:
                    board[2][0]=0
                    bot_turns.append(7)
                case 8:
                    board[2][1]=0
                    bot_turns.append(8)
                case 9:
                    board[2][2]=0
                    bot_turns.append(9)
        case 1:
            turn = 0
            replace_button_with_image(position)
            position['state'] = tk.DISABLED
            match witch_btn:
                case 1:
                    board[0][0]=1
                    bot_turns.append(1)
                case 2:
                    board[0][1]=1
                    bot_turns.append(2)
                case 3:
                    board[0][2]=1
                    bot_turns.append(4)
                case 4:
                    board[1][0]=1
                    bot_turns.append(4)
                case 5:
                    board[1][1]=1
                    bot_turns.append(5)
                case 6:
                    board[1][2]=1
                    bot_turns.append(6)
                case 7:
                    board[2][0]=1
                    bot_turns.append(7)
                case 8:
                    board[2][1]=1
                    bot_turns.append(8)
                case 9:
                    board[2][2]=1
                    bot_turns.append(9)
    whos_playing()
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
font_size = y_res//60
main_font = font.Font(family='DejaVu Sans', size=font_size )
main_menu_fun()
#SPRAVIT TURN
#do not delete wont work without it
root.mainloop()
