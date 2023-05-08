
import tkinter as tk
from ctypes import windll
import tkinter.font as font
import minimax
import random
from PIL import ImageTk, Image




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

def replace_button_with_image_continue(button,player_con):#used to replace images when you pause and come back. replaces 1 or 0 with "x" or "o"
    match player_con:
        case "X":
            image = Image.open('assets/img/krizek.png')#img path for 1th player
        case "O":
            image = Image.open('assets/img/kolecko.png')#img path for 2nd player
        case None:
            return
    img_size = canvas_size//3
    image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(image)
    button.configure(image=image, bg='white')
    button.image = image
    return
def replace_button_with_image(button):#used to play the game cuz it changes the blank images buttons to "X" or "O"
    y_res1 = y_res -20
    img_size = y_res1 //3 - 2
    if turn == 0:
        if player_1 == "O":
            image= Image.open('assets/img/krizek.png')#img path for 1th player
        elif player_1 == "X":
            image= Image.open('assets/img/kolecko.png')#img path for 2nd player
        image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        button.configure(image=image, bg='white')
        button.image = image
        return
    elif turn == 1:
        if opponent_1 == "O":
            image= Image.open('assets/img/krizek.png')#img path for 1th player
        elif opponent_1 == "X":
            image= Image.open('assets/img/kolecko.png')#img path for 2nd player
        image = image.resize((img_size,img_size), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        button.configure(image=image, bg='white')
        button.image = image
        return

def menu_button_fun():#creates pause menu in top left of the window and creates play field
    global menu_button
    clearwin()
    menu_button = tk.Button(root,bg='black', font=main_font,fg='white', text="pause", command=menu)
    menu_button.place(x= 5,y=5)
    #play_field(y_res)#do not delete parameter it wont work without it(idk why)
    return

def menu():#this will show up when you click the pause button
    global menu_button
    position = y_res//2
    spacing= 10+(position//10)
    clearwin()
    end = tk.Button(root,bg='black', fg='white', text="Quit", command=konec)
    main_menu = tk.Button(root,bg='black',fg='white', text="Main menu", command=main_menu_fun)
    settings = tk.Button(root, bg="black", fg="white",text="Settings", command=nastaveni)
    back = tk.Button(root,bg='black',fg='white', text="Continue", command=back_fun)
    back.place(x=position,y=position- spacing- spacing-spacing)
    settings.place(x=position, y=position- spacing-spacing)
    main_menu.place(x=position, y=position- spacing)
    end.place(x=position, y=position)
    settings["font"]=main_font 
    back['font'] = main_font
    main_menu['font'] = main_font
    end['font'] = main_font
    return

def play_as():# this will create a selection menu. play as "X" or "O" 
    global turn, antiturn
    clearwin()
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
    turn = random.randint(0,1)#generates who starts firts 0 for player, 1 for opponent
    
    
    def player_is_circle():
        global player_1, turn, opponent_1, player
        player_1 = "O"
        opponent_1 = "X"
        load_difficulty_gamemod()
        return
    def player_is_cross():
        global player_1, turn, opponent_1, player
        player_1 = "X"
        opponent_1 = "O"
        load_difficulty_gamemod()
        return
    return
def load_difficulty_gamemod():
    global easy_bot_turns_list
    chceck_progress()
    match difficulty:
        case 0:
            easy_bot_turns_list = []
            menu_button_fun()
            play_field(y_res)
            return
        case 1:
            menu_button_fun()
            play_field(y_res)
            return
        case 2:
            menu_button_fun()
            play_field(y_res)
            return
        case 3:
            menu_button_fun()
            play_field(y_res)
            return

def continue_game():#this will recreate images in a playfield from matrix 
    button_count = 0
    for o in range(3):
            for k in range(3):
                button_count += 1
                if game_board[o][k] == opponent_1:
                    unpause_buttons_after_pause(button_count, opponent_1)
                elif game_board[o][k] == player_1:
                    unpause_buttons_after_pause(button_count, player_1)
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
    load_difficulty_gamemod()
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
    global volume, music
    clearwin()
    if full_scr == False:
        root.geometry("{}x{}".format(x_res, y_res))
        root.attributes('-fullscreen',False)
    elif full_scr ==True:
        root.attributes('-fullscreen',True)
    center(root)
    position = y_res//2
    spacing= 10+(position//10)
    music_options = ["Default","meme"]
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
    global diff_easy, diff_medium, diff_hard, game_progress, easy_bot_turns_list
    easy_bot_turns_list = []
    clearwin()
    game_progress = 0
    position = y_res//2
    spacing= 10+(position//10)
    root.configure(bg="black") #test duvody
    play_with_friend = tk.Button(root,font=main_font, bg='black',fg='white',text="Local play with friend", command=play_w_friend)
    diff_easy = tk.Button(root,font=main_font,bg='black',fg='white', text="Easy", command=lehka)
    #diff_medium = tk.Button(root,font=main_font,bg='black',fg='white', text="Normal",)#command = stredni
    diff_hard = tk.Button(root,font=main_font,bg='black', fg='white',text="Normal", command=tezka)

    play_with_friend.place(x=position,y=position- spacing- spacing- spacing)#top to bottom positions
    diff_easy.place(x=position,y= position - spacing- spacing)
    #diff_medium.place(x=position,y= position- spacing)
    diff_hard.place(x=position,y=position-spacing)
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
    num = minimax.idk_yet(game_board, player_1, opponent_1)
    if winner(game_board,opponent_1) == None or winner(game_board,player_1) == None:
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
    else:
        return

def check_win(board, player_win):#MAKE IT BETTER FIX IT!!!!! checks if player won or not
    for row in range(3) :     
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2] == player_win) :        
            return player_win
  
    # Checking for Columns for X or O victory. 
    for col in range(3) :
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] == player_win) :
            return player_win
  
    # Checking for Diagonals for X or O victory. 
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] == player_win) :
        return player_win

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] == player_win):
        return player_win
    # draw
    if all(board[row][col] is not None for row in range(3) for col in range(3)):
        return "Draw"
    #if no one made draw or won
    return None

def winner(game_board, player_win):#winner screen used to create menu after someone wins. (player) won, play again and main menu
    result = check_win(game_board, player_win)
    position = y_res//2
    if result == "X":
        disable_play_field_buttons()
        player_win= "Crosses won"
        winner_write(player_win)
        return
    elif result == "O":
        disable_play_field_buttons()
        player_win= "Circles won"
        winner_write(player_win)
        return
    elif result == "Draw":
        disable_play_field_buttons()
        winner_write(result)
        return
    elif result == None:
        return None
    print(game_board)

def winner_write(player_win):
    menu_button.destroy()
    position = y_res//2
    spacing= 10+(position//10)
    winner = tk.StringVar(value=f"{player_win}")
    winner_label = tk.Label(root, textvariable=winner, font=("DejaVu Sans", 25, "normal"))
    winner_label.place(x=position,y=position-spacing-spacing-20)
    play_again = tk.Button(root,font=main_font,bg='black', fg='white', text="Play again", command=play)
    go_to_menu = tk.Button(root,font=main_font, bg='black',fg='white', text="Main menu", command=main_menu_fun)
    play_again.place(x=position,y=position-spacing)
    go_to_menu.place(x=position,y=position)

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

def play_field_buttons(y_res):#creates buttons in canvas
    global turn
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
    whos_playing()
    return

def ez_bot_play():#TRY NOT TO USE PLAYER FIX IT!!! easy difficulty. it generates ints 1-9(counting starts from top left)
    global easy_bot_turns_list
    if len(easy_bot_turns_list) >= 9:
        return
    while True:
        easy_bot_turn_gen = random.randint(1,9)
        print(easy_bot_turns_list)
        if easy_bot_turn_gen not in easy_bot_turns_list:
            match easy_bot_turn_gen:
                case 1:
                    btn_1_1.invoke()
                    return
                case 2:
                    btn_1_2.invoke()
                    return
                case 3:
                    btn_1_3.invoke()
                    return
                case 4:
                    btn_2_1.invoke()
                    return
                case 5:
                    btn_2_2.invoke()
                    return
                case 6:
                    btn_2_3.invoke()
                    return
                case 7:
                    btn_3_1.invoke()
                    return
                case 8:
                    btn_3_2.invoke()
                    return
                case 9:
                    btn_3_3.invoke()
                    return
        else:
            continue
def whos_playing():# try to fix it or implement it better
    match difficulty:
        case 0:
            pass
            return
        case 1:
            if turn == 1:
                print(turn)
                ez_bot_play()
                return
            elif turn == 0:
                return
        case 2:
            pass
            return
        case 3:
            if turn == 1:
                play_hard()
                return
            elif turn == 0:
                return
            return


def place_x_or_o(position, witch_btn):
    global turn, easy_bot_turns_list
    match turn:
        case 0:
            turn = 1
            winner(game_board, player_1)
            replace_button_with_image(position)
            position['state'] = tk.DISABLED
            match witch_btn:
                case 1:#player section
                    game_board[0][0]=player_1
                case 2:
                    game_board[0][1]=player_1
                case 3:
                    game_board[0][2]=player_1
                case 4:
                    game_board[1][0]=player_1
                case 5:
                    game_board[1][1]=player_1
                case 6:
                    game_board[1][2]=player_1
                case 7:
                    game_board[2][0]=player_1
                case 8:
                    game_board[2][1]=player_1
                case 9:
                    game_board[2][2]=player_1
            if difficulty == 1:
                easy_bot_turns_list.append(witch_btn)
            whos_playing()
            winner(game_board, player_1)
            return
        case 1:#opponent section
            turn = 0
            winner(game_board, opponent_1)
            replace_button_with_image(position)
            position['state'] = tk.DISABLED
            match witch_btn:
                case 1:
                    game_board[0][0]=opponent_1
                case 2:
                    game_board[0][1]=opponent_1
                case 3:
                    game_board[0][2]=opponent_1
                case 4:
                    game_board[1][0]=opponent_1
                case 5:
                    game_board[1][1]=opponent_1
                case 6:
                    game_board[1][2]=opponent_1
                case 7:
                    game_board[2][0]=opponent_1
                case 8:
                    game_board[2][1]=opponent_1
                case 9:
                    game_board[2][2]=opponent_1
            if difficulty == 1:
                easy_bot_turns_list.append(witch_btn)
            winner(game_board, opponent_1)
            return


easy_bot_turns_list = []
antiturn = 0
player = None
player_1, opponent_1 = None,None
volume = 100
#makes windows stupid and useful zoom not work on this

windll.shcore.SetProcessDpiAwareness(1)
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

