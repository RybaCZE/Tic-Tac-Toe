import tkinter as tk
import ctypes
from PIL import ImageTk, Image
import tkinter.font as font
import minimax
import numba
import random

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
    return
def konec():
    quit()

def clearwin():#makes your screen clear(woooow)
    for widget in root.winfo_children():
        widget.destroy()
    return

class SquareButton(tk.Button):#buttons goo squareee!!!!(used to make buttons with text square)
    def __init__(self, master=None, size=None, **kwargs):
        self.img = tk.PhotoImage()
        tk.Button.__init__(self, master, image=self.img, compound=tk.CENTER, width=size, height=size, **kwargs)
        return
def disable_play_field_buttons():#used to disable all buttons after someone won so you cant change any buttons 
    btn_1_1['state'] = tk.DISABLED
    btn_1_2['state'] = tk.DISABLED
    btn_1_3['state'] = tk.DISABLED
    btn_2_1['state'] = tk.DISABLED
    btn_2_2['state'] = tk.DISABLED
    btn_2_3['state'] = tk.DISABLED
    btn_3_1['state'] = tk.DISABLED
    btn_3_2['state'] = tk.DISABLED
    btn_3_3['state'] = tk.DISABLED
    return

def replace_button_with_image_continue(button,one_or_null):#used to replace images when you pause and come back. replaces 1 or 0 with "x" or "o"
    match one_or_null:
        case 1:
            image = Image.open('assets/img/krizek.png')#img path for 1th player
        case 0:
            image = Image.open('assets/img/kolecko.png')#img path for 2nd player
    img_size = canvas_size//3
    image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    button.configure(image=image, bg='white')
    button.image = image
    return

def replace_button_with_image(button):#used to play the game cuz it changes the blank images buttons to "X" or "O"
    y_res1 = y_res -20
    img_size = y_res1 //3 - 2
    match turn:
        case 0 :
            image = Image.open('assets/img/krizek.png')#img path for 1th player
        case 1:
            image = Image.open('assets/img/kolecko.png')#img path for 2nd player
    image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    button.configure(image=image, bg='white')
    button.image = image
    return

def menu_button_fun():#creates pause menu in top left of the window and creates play field
    clearwin()
    menu_button = tk.Button(root,bg='black', font=main_font,fg='white', text="pause", command=menu)
    menu_button.place(x= 5,y=5)
    play_field(y_res)#do not delete parameter it wont work without it(idk why)
    return
def menu():#this will show up when you click the pause button
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
    return

def play_as():# this will create a selection menu. play as "X" or "O" 
    clearwin()
    player = None
    img_size = y_res//3
    circle = Image.open('assets/img/kolecko.png')#0    opens the image
    cross = Image.open('assets/img/krizek.png')#1      opens the image
    
    circle = circle.resize((img_size, img_size), resample=Image.LANCZOS)#resizes the image to one third of the main window height
    cross = cross.resize((img_size, img_size), resample=Image.LANCZOS)#resizes the image to one third of the main window height
    circle_tk = ImageTk.PhotoImage(circle)
    cross_tk = ImageTk.PhotoImage(cross)

    play_as_label = tk.Label(root,font=main_font ,text="Who do you want to play as?")
    play_as_circle = tk.Button(root, anchor="w",font=main_font, command=lambda: player_is_circle())
    play_as_cross = tk.Button(root, anchor="e",font=main_font, command=lambda: player_is_cross())

    play_as_circle.config(image=circle_tk, width=img_size, height=img_size)
    play_as_cross.config(image=cross_tk, width=img_size, height=img_size)
    play_as_circle.image = circle_tk
    play_as_cross.image = cross_tk
    
    play_as_label.place(relx=0.5, rely=0.3, anchor="center")
    play_as_circle.place(relx=0.25, rely=0.5, anchor="center")
    play_as_cross.place(relx=0.75, rely=0.5, anchor="center")
    def player_is_circle():
        global player, turn, opponent
        player = 0
        turn = 0
        opponent = 1
        player_1 = "o"
        player_2 = "x"
        load_difficulty_gamemod()
    def player_is_cross():
        global player, turn, opponent
        player =1
        turn = 1
        opponent = 0
        player_1 = "x"
        player_2 = "o"
        load_difficulty_gamemod()
    def load_difficulty_gamemod():
        chceck_progress()
        match difficulty:
            case 0:
                menu_button_fun()
            case 1:
                menu_button_fun()
            case 2:
                menu_button_fun()
            case 3:
                menu_button_fun()
    return
def continue_game():#this will recreate images in a playfield from matrix 
    button_count = 0
    for o in range(3):
            for k in range(3):
                button_count += 1
                if game_board[o][k] == 1:  
                    witch_players_turn = 1
                    unpause_buttons_after_pause(button_count, witch_players_turn)
                elif game_board[o][k] ==0:
                    witch_players_turn = 0
                    unpause_buttons_after_pause(button_count, witch_players_turn)
                else:
                    continue
    return

def unpause_buttons_after_pause(button_count, player):#this will continue the game when you unpause. when the matrix(game_board) has 1 or 0 it will get the position(counting from 
    #top left). 
    #1input is witch button and what player button count is in continue_game 
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
    return

def back_fun():#used in witch difficulty to put player after pause #FIX IT OR REMOVE IT OR IMPLEMENT IT BETTER
    global game_progress
    game_progress = 1
    match difficulty:
        case 0:
            play_w_friend()
        case 1:
            lehka()
        case 2:
            stredni()
        case 3:
            tezka()
    return

def main_menu_fun():#creates the main menu screen(play, settings, quit)
    clearwin()
    position = y_res//2
    spacing= 10+(position//10)
    main_play = tk.Button(root,font=main_font, bg='black',fg='white',text="play", command=play)
    settings = tk.Button(root,font=main_font,bg='black', fg='white',text="settings", command=nastaveni)
    end = tk.Button(root, font=main_font,bg='black',fg='white',text="quit", command=konec)

    main_play.place(x=position,y= position-spacing-spacing)#on top
    settings.place(x=position,y= position-spacing)#lower
    end.place(x=position,y= position)#lowest
    return

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
    resolution_options = ["800 x 600", "1920 x 1080","1920 x 1200", "full screen"]
    clicked = tk.StringVar()
    clicked.set("resolution") 
    resulution = tk.OptionMenu(root, clicked, *resolution_options) 
    Menu_sett = tk.Button(root,bg='black',font=main_font,fg='white', text="Menu", command=main_menu_fun)
    save = tk.Button(root,bg='black',fg='white', font=main_font,text="save settings", command=nastaveni)

    resulution.place(x=position, y=position- spacing-spacing)
    Menu_sett.place(x= position, y=position- spacing)
    save.place(x=position,y= position)

    resulution.config(bg="black",fg="white" ,activebackground="black", activeforeground="white")
    resulution["menu"].config(bg="black",fg="white" ,activebackground="black", activeforeground="gray")
    resulution['font'] = main_font

    def resolution_change(option, value, op):
        global x_res, y_res, full_scr, main_font
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
        font_size = y_res//60
        main_font = font.Font(family='DejaVu Sans', size=font_size )
    clicked.trace("w", resolution_change)
    return

def play():#play menu screen (diffisulty selector)
    global diff_easy, diff_medium, diff_hard, game_progress
    clearwin()
    game_progress = 0
    position = y_res//2
    spacing= 10+(position//10)
    
    root.configure(bg="black") #test duvody
    play_with_friend = tk.Button(root,font=main_font, bg='black',fg='white',text="Local play with friend", command=play_w_friend)
    diff_easy = tk.Button(root,font=main_font,bg='black',fg='white', text="Easy", command=lehka)
    diff_medium = tk.Button(root,font=main_font,bg='black',fg='white', text="Normal", command=stredni)
    diff_hard = tk.Button(root,font=main_font,bg='black', fg='white',text="Hard", command=tezka)

    play_with_friend.place(x=position,y=position- spacing- spacing- spacing)#top to bottom positions
    diff_easy.place(x=position,y= position - spacing- spacing)
    diff_medium.place(x=position,y= position- spacing)
    diff_hard.place(x=position,y=position)
    return

def play_w_friend():
    global diff_easy, diff_medium, diff_hard,  difficulty
    difficulty = 0
    play_as()
    return

def lehka():#ez difficculty
    global diff_easy, diff_medium, diff_hard, difficulty
    difficulty = 1
    play_as()
    return

def stredni():#medium difficulty
    global diff_easy, diff_medium, diff_hard, difficulty
    difficulty = 2
    play_as()
    return

def tezka():#hard difficulty
    global diff_easy, diff_medium, diff_hard, difficulty
    difficulty = 3
    play_as()
    return

def play_hard():
    num = minimax.idk_yet(game_board, player, opponent)
    match num:
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
    return

def check_win(game_board):#MAKE IT BETTER FIX IT!!!!! checks if player won or not
    # line check
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] is not None:
            if game_board[row][0] == game_board[row][1] == game_board[row][2]:
                disable_play_field_buttons()
                return True
    # col check
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] is not None:
            if game_board[0][col] == game_board[1][col] == game_board[2][col]:
                disable_play_field_buttons()
                return True
    # diagonal
    if game_board[0][0] == game_board[1][1] == game_board[2][2] is not None:
        if game_board[0][0] == game_board[1][1] == game_board[2][2]:
            disable_play_field_buttons()
            return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] is not None:
        if game_board[0][2] == game_board[1][1] == game_board[2][0]:
            disable_play_field_buttons()
            return True
    # draw
    if all(game_board[row][col] is not None for row in range(3) for col in range(3)):
        return "Draw"
    #if no one made draw or won
    return False

def winner(game_board):#winner screen used to create menu after someone wins. (player) won, play again and main menu
    result = check_win(game_board)
    position = y_res//2
    spacing= 10+(position//10)
    if result is True:
        if player_turn ==1:
            player_win = "Crosses"
        elif player_turn == 0:
            player_win= "Circles"
        winner = tk.StringVar(value=f"{player_win} won")
        winner_label = tk.Label(root, textvariable=winner, font=("DejaVu Sans", 25, "normal"))
        winner_label.place(x=position,y=position-spacing-spacing-20)
        play_again = tk.Button(root,font=main_font,bg='black', fg='white', text="Play again", command=play)
        go_to_menu = tk.Button(root,font=main_font, bg='black',fg='white', text="Main menu", command=main_menu_fun)
        play_again.place(x=position,y=position-spacing)
        go_to_menu.place(x=position,y=position)
    elif result == "Draw":
        winner = tk.StringVar(value=f"That's a draw")
        winner_label = tk.Label(root, textvariable=winner, font=("DejaVu Sans", 20, "normal"))
    return

def chceck_progress():#used to recreate the game_board after unpause
    global game_board
    if game_progress == 1:
        play_field(y_res)
    else:
        game_board = [[None, None, None],
        [None, None, None],
        [None, None, None]]
        play_field(y_res)
    return

def play_field(y_res):#create play field 
    #do not delete parameter it wont work without it 
    global canvas, canvas_size,game_board
    canvas_size = y_res-10
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")#creates canvas aka play field
    canvas.place(relx=0.5, rely=0.5, anchor='center')

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
        return

def play_field_buttons(y_res):#SOMETHING IS LOOKING WRONG FIX IT!!!!!creates buttons in canvas
    global turn, bot_turns
    y_res1 = y_res -20
    btn_size = y_res1 //3 - 2

    #btn_row_colum
    global btn_1_1 ,btn_1_2 , btn_1_3, btn_2_1, btn_2_2, btn_2_3, btn_3_1, btn_3_2, btn_3_3
    btn_1_1 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_1_1,1))
    btn_1_2 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_1_2,2))
    btn_1_3 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_1_3,3))
    btn_2_1 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_2_1,4))
    btn_2_2 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_2_2,5))
    btn_2_3 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_2_3,6))
    btn_3_1 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_3_1,7))
    btn_3_2 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_3_2,8))
    btn_3_3 = SquareButton(canvas, size=btn_size, bg='black' ,command=lambda:place_x_or_o(btn_3_3,9))
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
    if difficulty == 1:
        whos_playing()
    return

def ez_bot_play():#TRY NOT TO USE PLAYER FIX IT!!! easy difficulty. it generates ints 1-9(counting starts from top left)
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
                return
            else:
                continue
def whos_playing():# try to fix it or implement it better
    match difficulty:
        case 1:
            if turn != player:
                ez_bot_play()
            elif turn == player:
                pass
        case 2:
            pass
        case 3:
            play_hard()


def place_x_or_o(position, witch_btn):
    global turn, player_turn
    match turn:
        case 0:
            turn = 1
            player_turn = 1
            replace_button_with_image(position)
            position['state'] = tk.DISABLED
            match witch_btn:
                case 1:
                    game_board[0][0]=0
                    bot_turns.append(1)
                case 2:
                    game_board[0][1]=0
                    bot_turns.append(2)
                case 3:
                    game_board[0][2]=0
                    bot_turns.append(4)
                case 4:
                    game_board[1][0]=0
                    bot_turns.append(4)
                case 5:
                    game_board[1][1]=0
                    bot_turns.append(5)
                case 6:
                    game_board[1][2]=0
                    bot_turns.append(6)
                case 7:
                    game_board[2][0]=0
                    bot_turns.append(7)
                case 8:
                    game_board[2][1]=0
                    bot_turns.append(8)
                case 9:
                    game_board[2][2]=0
                    bot_turns.append(9)
        case 1:
            turn = 0
            player_turn = 0
            replace_button_with_image(position)
            position['state'] = tk.DISABLED
            match witch_btn:
                case 1:
                    game_board[0][0]=1
                    bot_turns.append(1)
                case 2:
                    game_board[0][1]=1
                    bot_turns.append(2)
                case 3:
                    game_board[0][2]=1
                    bot_turns.append(4)
                case 4:
                    game_board[1][0]=1
                    bot_turns.append(4)
                case 5:
                    game_board[1][1]=1
                    bot_turns.append(5)
                case 6:
                    game_board[1][2]=1
                    bot_turns.append(6)
                case 7:
                    game_board[2][0]=1
                    bot_turns.append(7)
                case 8:
                    game_board[2][1]=1
                    bot_turns.append(8)
                case 9:
                    game_board[2][2]=1
                    bot_turns.append(9)
    whos_playing()
    winner(game_board)
    return



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
#add music https://www.geeksforgeeks.org/how-to-play-sounds-in-python-with-tkinter/

#doesnt work
#minimax.idk_yet(game_board, player, opponent)
