
def which_turn(): 
    turn = input("先行(☓)→0|後行(○))→1\n")
    try:
        turn = int(turn)
    except ValueError:
        print("0,1以外の数字を入力しないでください")
        return which_turn()
    except TypeError:
        print("0,1以外の数字を入力しないでください")
        return which_turn()
    if turn < 0 or turn > 1:
        print("0,1以外の数字を入力しないでください")
        return which_turn()
    else:
        return turn
    
def which_input_number(board_array): 
    input_number = input("左から何番目に入れますか？(1〜7)\n")
    try:
        input_number = int(input_number)
    except ValueError:
        print("1〜7以外の数字を入力しないでください")
        return which_input_number(board_array)
    except TypeError:
        print("1〜7以外の数字を入力しないでください")
        return which_input_number(board_array)
    if input_number > 7 or input_number < 1:
        print("1〜7以外の数字を入力しないでください")
        return which_input_number(board_array)
    elif check_board(input_number,board_array):
        print("ここにはもうこれ以上積めません")
        return which_input_number(board_array)
    else:
        return input_number
    
def check_board(input_number,board_array):  
    if (board_array.get(input_number * 6) != 2) and (board_array.get(input_number * 6) != 3):
        return False
    else: 
        return True