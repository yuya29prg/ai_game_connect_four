import related_board as board
from copy import deepcopy

def get_keys_empty(board_array): #空所リストの番号取り出し
    keys = [k for k, v in board_array.items() if v == 1 ]
    return keys

def reach_check(board_array,my_koma_number):
    if victory_column(board_array,my_koma_number) != 0:
        return to_hand(victory_column(board_array,my_koma_number))
    elif victory_row(board_array,my_koma_number):
        return to_hand(victory_row(board_array,my_koma_number))
    else: 
        return 0
    
def victory_column(board_array,my_koma_number):
    for i in range(0,37,6):
        count = 0
        for j in range(1,7,1):
            if board_array.get(j+i) == my_koma_number:
                count = count + 1  
                if count == 3:
                    if board_array.get(j+i+1) == 1:
                        return j+i+1
            else:
                count = 0        
    return 0

def victory_row(board_array,my_koma_number):
    for i in range(6,0,-1):
        count = 0
        for j in range(0,7,1):
            if board_array.get(i+j*6) == my_koma_number:
                count = count + 1
                if count == 3:
                    if board_array.get(i+(j*6)+6) == 1:
                        return i+(j*6)+6
                    elif board_array.get(i+(8*j)-18) == 1:
                        return  (i+(8*j)-18)
            else:
                count = 0
    return 0
    
def ai(board_array,turn_flag):
    the_best_score = 0
    the_best_hand = 1
    score = 0
    hand = 0
    
    if turn_flag % 2 == 1:#aiが後手
        ai_turn_2 = 3    #
        ai_turn_3 = 7
        ai_turn_4 = 10000
        opposit_turn_2 = -4
        opposit_turn_3 = -9
        opposit_turn_4 = -10000
        ai_koma_number = 3
        my_koma_number = 2
    else: 
        ai_turn_2 = 4 #aiが先手
        ai_turn_3 = 8
        ai_turn_4 = 10000
        opposit_turn_2 = -5
        opposit_turn_3 = -9
        opposit_turn_4 = -10000
        ai_koma_number = 2
        my_koma_number = 3
    for i in range(len(get_keys_empty(board_array))): #5回分繰り返してる，再帰とかに変更できたらベストかも
            score = 0
            dammy_board = deepcopy(board_array)
            board.change_board(to_hand(get_keys_empty(dammy_board)[i]),dammy_board,ai_koma_number) #1回
            #print(get_keys_empty(dammy_board)[i])
            #show_board(dammy_board)
            hand = get_keys_empty(dammy_board)[i]
            score = check_score(dammy_board,turn_flag,True)
            for j in range(len(get_keys_empty(dammy_board))):
                middle_score = 0
                dammy_board2 = deepcopy(dammy_board)
                board.change_board(to_hand(get_keys_empty(dammy_board2)[j]),dammy_board2,my_koma_number) #2回
                middle_score = score + check_score(dammy_board2,turn_flag,False)
                
                for l in range(len(get_keys_empty(dammy_board2))):
                    layer_score = 0
                    dammy_board3 = deepcopy(dammy_board2)
                    board.change_board(to_hand(get_keys_empty(dammy_board3)[l]),dammy_board3,ai_koma_number) #3回
                    layer_score = middle_score + check_score(dammy_board3,turn_flag,True)
                    
                    for m in range(len(get_keys_empty(dammy_board3))):
                        middle_score = 0
                        dammy_board4 = deepcopy(dammy_board3)
                        board.change_board(to_hand(get_keys_empty(dammy_board4)[m]),dammy_board4,my_koma_number) #4回
                        middle_1_score = layer_score + check_score(dammy_board4,turn_flag,False)
                        
                        for n in range(len(get_keys_empty(dammy_board4))):
                            layer_score = 0
                            dammy_board5 = deepcopy(dammy_board4)
                            board.change_board(to_hand(get_keys_empty(dammy_board5)[n]),dammy_board5,ai_koma_number) #5回
                            layer_1_score = middle_1_score + check_score(dammy_board5,turn_flag,True)
                    
                            if the_best_score < layer_1_score: #一番点数高いやつにいれかえ
                                the_best_score = layer_1_score
                                the_best_hand = hand #ここのhandは0~41だから，入力の1~7に変更するために下でto_hand使ってる
                        
            #print(the_best_hand)     
    print(f"{to_hand(the_best_hand)}に入れました．")      
    return to_hand(the_best_hand)       
    
def to_hand(hand):
    if hand > 0 and 7 > hand:
        return 1
    elif hand > 6 and 13 > hand:
        return 2
    elif hand > 12 and 19 > hand:
        return 3
    elif hand > 18 and 25 > hand:
        return 4
    elif hand > 24 and 31 > hand:
        return 5
    elif hand > 30 and 37 > hand:
        return 6
    elif hand > 36 and 43 > hand:
        return 7
 
def check_score(board_array,turn_flag,true_or_false):#trueだったらaiのターン
    count = 0
    if turn_flag % 2 == 1:#aiが後手
        #ai_turn_2 = 2
        #ai_turn_3 = 6
        #ai_turn_4 = 1000
        opposit_turn_2 = -3
        opposit_turn_3 = -7
        opposit_turn_4 = -1000
        ai_koma_number = 3
        my_koma_number = 2
    else: 
        #ai_turn_2 = 3 #aiが先手
        #ai_turn_3 = 7
        #ai_turn_4 = 1000
        #opposit_turn_2 = -2
        #opposit_turn_3 = -6
        #opposit_turn_4 = -1000
        ai_koma_number = 2
        my_koma_number = 3 
    check_list1 =[  [board_array[1],board_array[2],board_array[3],board_array[4]],#縦探索スタート
                    [board_array[2],board_array[3],board_array[4],board_array[5]],
                    [board_array[3],board_array[4],board_array[5],board_array[6]],
                    [board_array[7],board_array[8],board_array[9],board_array[10]],
                    [board_array[8],board_array[9],board_array[10],board_array[11]],
                    [board_array[9],board_array[10],board_array[11],board_array[12]],
                    [board_array[13],board_array[14],board_array[15],board_array[16]],
                    [board_array[14],board_array[15],board_array[16],board_array[17]],
                    [board_array[15],board_array[16],board_array[17],board_array[18]],
                    [board_array[19],board_array[20],board_array[21],board_array[22]],
                    [board_array[20],board_array[21],board_array[22],board_array[23]],
                    [board_array[21],board_array[22],board_array[23],board_array[24]],
                    [board_array[25],board_array[26],board_array[27],board_array[28]],
                    [board_array[26],board_array[27],board_array[28],board_array[29]],
                    [board_array[27],board_array[28],board_array[29],board_array[30]],
                    [board_array[31],board_array[32],board_array[33],board_array[34]],
                    [board_array[32],board_array[33],board_array[34],board_array[35]],
                    [board_array[33],board_array[34],board_array[35],board_array[36]],
                    [board_array[37],board_array[38],board_array[39],board_array[40]],
                    [board_array[38],board_array[39],board_array[40],board_array[41]],
                    [board_array[39],board_array[40],board_array[41],board_array[42]] ,#縦探索終了
                    [board_array[1],board_array[7],board_array[13],board_array[19]] ,#横探索スタート
                    [board_array[7],board_array[13],board_array[19],board_array[25]],
                    [board_array[13],board_array[19],board_array[25],board_array[31]],
                    [board_array[19],board_array[25],board_array[31],board_array[37]],
                    [board_array[2],board_array[8],board_array[14],board_array[20]],
                    [board_array[8],board_array[14],board_array[20],board_array[26]],
                    [board_array[14],board_array[20],board_array[26],board_array[32]],
                    [board_array[20],board_array[26],board_array[32],board_array[38]],
                    [board_array[3],board_array[9],board_array[15],board_array[21]],
                    [board_array[9],board_array[15],board_array[21],board_array[27]],
                    [board_array[15],board_array[21],board_array[27],board_array[33]],
                    [board_array[21],board_array[27],board_array[33],board_array[39]],
                    [board_array[4],board_array[10],board_array[16],board_array[22]] ,
                    [board_array[10],board_array[16],board_array[22],board_array[28]],
                    [board_array[16],board_array[22],board_array[28],board_array[34]],
                    [board_array[22],board_array[28],board_array[34],board_array[40]],
                    [board_array[5],board_array[11],board_array[17],board_array[23]],
                    [board_array[11],board_array[17],board_array[23],board_array[29]],
                    [board_array[17],board_array[23],board_array[29],board_array[35]],
                    [board_array[23],board_array[29],board_array[35],board_array[41]],
                    [board_array[6],board_array[12],board_array[18],board_array[24]],
                    [board_array[12],board_array[18],board_array[24],board_array[30]],
                    [board_array[18],board_array[24],board_array[30],board_array[36]],
                    [board_array[24],board_array[30],board_array[36],board_array[42]],#横探索終了
                    [board_array[4],board_array[9],board_array[14],board_array[19]], #右,斜め探索開始
                    [board_array[5],board_array[10],board_array[15],board_array[20]] ,
                    [board_array[10],board_array[15],board_array[20],board_array[25]] , 
                    [board_array[6],board_array[11],board_array[16],board_array[21]],
                    [board_array[11],board_array[16],board_array[21],board_array[26]],
                    [board_array[16],board_array[21],board_array[26],board_array[31]],
                    [board_array[12],board_array[17],board_array[22],board_array[27]] ,
                    [board_array[17],board_array[22],board_array[27],board_array[32]],
                    [board_array[22],board_array[27],board_array[32],board_array[37]],
                    [board_array[18],board_array[23],board_array[28],board_array[33]],
                    [board_array[23],board_array[28],board_array[33],board_array[38]],
                    [board_array[24],board_array[29],board_array[34],board_array[39]],#右斜め下探査終了
                    [board_array[3],board_array[10],board_array[17],board_array[24]], #右斜上探索スタート
                    [board_array[2],board_array[9],board_array[16],board_array[23]],
                    [board_array[9],board_array[16],board_array[23],board_array[30]],
                    [board_array[1],board_array[8],board_array[15],board_array[22]],
                    [board_array[8],board_array[15],board_array[22],board_array[29]],
                    [board_array[15],board_array[22],board_array[29],board_array[36]],
                    [board_array[7],board_array[14],board_array[21],board_array[28]] ,
                    [board_array[14],board_array[21],board_array[28],board_array[35]] ,
                    [board_array[21],board_array[28],board_array[35],board_array[42]],
                    [board_array[13],board_array[20],board_array[27],board_array[34]],
                    [board_array[20],board_array[27],board_array[34],board_array[41]],
                    [board_array[19],board_array[26],board_array[33],board_array[40]]]#右斜め下探索終了
    if true_or_false:
        if ai_koma_number == 3:#aiが後手のとき
            for i in range(0,68,1):
                if check_list1[i].count(ai_koma_number) == 2 and check_list1[i].count(my_koma_number)  == 0: #4つの中に3が2個かつ2が0個
                        count =  count + 2
                elif check_list1[i].count(ai_koma_number) == 3 and check_list1[i].count(my_koma_number)  == 0:
                        count = count + 6
                elif check_list1[i].count(ai_koma_number) == 4:
                        count = count + 1000
        elif ai_koma_number == 2:
            for i in range(0,68,1):
                if check_list1[i].count(ai_koma_number) == 2 and check_list1[i].count(my_koma_number)  == 0:
                        count =  count + 3
                elif check_list1[i].count(ai_koma_number) == 3 and check_list1[i].count(my_koma_number)  == 0:
                        count = count + 10
                elif check_list1[i].count(ai_koma_number) == 4 :
                        count = count + 1000
    else:
        if ai_koma_number == 3:
            for i in range(0,68,1):
                if check_list1[i].count(my_koma_number) == 2 and check_list1[i].count(ai_koma_number)  == 0:
                        count =  count - 4
                elif check_list1[i].count(my_koma_number) == 3 and check_list1[i].count(my_koma_number)  == 0:
                        count = count - 8
                elif check_list1[i].count(my_koma_number) == 4 :
                        count = count - 1000
        elif ai_koma_number == 2:
            for i in range(0,68,1):
                if check_list1[i].count(my_koma_number) == 2 and check_list1[i].count(my_koma_number)  == 0:
                        count =  count - 5
                elif check_list1[i].count(my_koma_number) == 3 and check_list1[i].count(my_koma_number)  == 0:
                        count = count - 12
                elif check_list1[i].count(my_koma_number) == 4 :
                        count = count - 1000
            
    return count