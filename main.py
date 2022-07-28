from copy import deepcopy
import victory_hantei as victory
import related_board as board
import player 
import for_ai as ai

def main():
    print("コネクトフォー")
    board_array = board.init_board_array()
    my_turn = player.which_turn()
    turn_flag = 0  #何ターン目か教えてくれる
    if my_turn == 0:
        my_koma_number = 2
        ai_koma_number =3
        my_koma = "☓"
        ai_koma = "○"
    else:
        my_koma_number = 3
        ai_koma_number =2
        my_koma = "○"
        ai_koma = "☓"
    
    victory_flag = 0 
    board.show_board(board_array)
    # board.show_board_for_debag(board_array)
    while victory_flag == 0:
        if turn_flag != 42:
            if turn_flag % 2 == my_turn:
                print(f"{turn_flag+1}手目")
                print(f"あなたの番です({my_koma})")
                input_number =  player.which_input_number(board_array)
                board.change_board(input_number,board_array,my_koma_number)
                board.show_board(board_array)
                # board.show_board_for_debag(board_array)
                if victory.check_victory_all(board_array,my_koma_number) == True:
                    print("あなたの勝ちです")
                    victory_flag = 1
                else:
                    turn_flag = turn_flag + 1
                    print("-------------------------------------")
            else :
                print(f"{turn_flag + 1}手目")
                print(f"aiの番です({ai_koma})")
                #input_number =  which_input_number(board_array)
                #change_board(input_number,board_array,ai_koma_number)
                board_array_for_ai = deepcopy(board_array)
                if turn_flag == 0:
                    board.change_board(4,board_array,ai_koma_number)
                    board.show_board(board_array)
                    # board.show_board_for_debag(board_array)
                    turn_flag = turn_flag + 1
                else:   
                    # if ai.reach_check(board_array_for_ai,ai_koma_number) != 0:
                    #     board.change_board(ai.reach_check(board_array_for_ai,ai_koma_number),board_array,ai_koma_number) 
                    #     board.show_board(board_array)
                    #     board.show_board_for_debag(board_array)
                    #     if victory.check_victory_all(board_array,ai_koma_number) == True:
                    #         print("aiのかちです")
                    #         victory_flag = 1
                    #     else:
                    #         turn_flag = turn_flag + 1
                    
                    # if ai.reach_check(board_array_for_ai,my_koma_number) != 0:
                    #     board.change_board(ai.reach_check(board_array_for_ai,my_koma_number),board_array,ai_koma_number) 
                    #     board.show_board(board_array)
                    #     # board.show_board_for_debag(board_array)
                    #     if victory.check_victory_all(board_array,ai_koma_number) == True:
                    #         print("aiのかちです")
                    #         victory_flag = 1
                    #     else:
                    #         turn_flag = turn_flag + 1
                    board.change_board(ai.ai(board_array_for_ai,turn_flag),board_array,ai_koma_number)
                
                    board.show_board(board_array)
                    # board.show_board_for_debag(board_array)
                    if victory.check_victory_all(board_array,ai_koma_number) == True:
                        print("aiのかちです")
                        victory_flag = 1
                    else:
                        turn_flag = turn_flag + 1
                        print("----------------------------------------")
        else:
            print("これ以上詰めないので引き分け")
            break
    
if __name__ == '__main__':
    main()