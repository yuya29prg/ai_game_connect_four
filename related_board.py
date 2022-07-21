def init_board_array():
    return {1:1,2:0,3:0,4:0,5:0,6:0,       #コネクトフォーの盤面
            7:1,8:0,9:0,10:0,11:0,12:0,    #1が一番左下．
            13:1,14:0,15:0,16:0,17:0,18:0, #42が一番右上
            19:1,20:0,21:0,22:0,23:0,24:0, #バリュー0が何もないとこ
            25:1,26:0,27:0,28:0,29:0,30:0, #バリュー1が空所
            31:1,32:0,33:0,34:0,35:0,36:0, #バリュー2は☓
            37:1,38:0,39:0,40:0,41:0,42:0} 
    
def show_board(board_array): 
    j = 0
    for i in range(6,0,-1):
        print(f"|{convert_to_board(board_array.get(i))}|",end="")
        print(f"{convert_to_board(board_array.get(i*2+j))}|",end="")
        print(f"{convert_to_board(board_array.get(i*3+j*2))}|",end="")
        print(f"{convert_to_board(board_array.get(i*4+j*3))}|",end="")
        print(f"{convert_to_board(board_array.get(i*5+j*4))}|",end="")
        print(f"{convert_to_board(board_array.get(i*6+j*5))}|",end="")
        print(f"{convert_to_board(board_array.get(i*7+j*6))}|")
        j = j + 1
    print(" 1 2 3 4 5 6 7")
    #print("-----------------------------------\n↑結果")
    
def show_board_for_debag(board_array): 
    j = 0
    for i in range(6,0,-1):
        print(f"|{board_array.get(i)}|",end="")
        print(f"{board_array.get(i*2+j)}|",end="")
        print(f"{board_array.get(i*3+j*2)}|",end="")
        print(f"{board_array.get(i*4+j*3)}|",end="")
        print(f"{board_array.get(i*5+j*4)}|",end="")
        print(f"{board_array.get(i*6+j*5)}|",end="")
        print(f"{board_array.get(i*7+j*6)}|")
        j = j + 1
    print("↑デバッグ用\n-----------------------------------")  

def convert_to_board(board_value):
    if board_value == 0:
        return " "
    elif board_value == 1:
        return " "
    elif board_value == 2:
        return "☓"
    elif board_value == 3:
        return "○"
    else: 
        return " "
    
def change_board(input_number,board_array,turn):
    for k,v in board_array.items():
        if v == 1 and ((input_number-1)*6 < k and k < (input_number*6+1)):
            if turn == 2:
                board_array[k] = 2
                if k % 6 == 0:
                    break
                else:
                    board_array[k+1] = 1
                    break
            else:
                board_array[k] = 3
                if k % 6 == 0:
                    break
                else:
                    board_array[k+1] = 1
                    break