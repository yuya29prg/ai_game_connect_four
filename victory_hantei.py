def check_victory_all(board_array,my_koma_number):
    if victory_column(board_array,my_koma_number):
        return True
    elif victory_row(board_array,my_koma_number):
        return True
    elif victory_slash(board_array,my_koma_number):
        return True
    else: 
        return False
    
def victory_column(board_array,my_koma_number):
    for i in range(0,37,6):
        count = 0
        for j in range(1,7,1):
            if board_array.get(j+i) == my_koma_number:
                count = count + 1  
                if count == 4:
                    return True
            else:
                count = 0        
    return False   

def victory_row(board_array,my_koma_number):
    for i in range(6,0,-1):
        count = 0
        for j in range(0,7,1):
            if board_array.get(i+j*6) == my_koma_number:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def victory_slash(board_array,my_koma_number):
    for i in range(4,7,1):
        count = 0
        for j in range(0,i,1):
            if board_array.get(i+j*5) == my_koma_number:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
    for i in range(12,30,6):
        count = 0
        for j in range(0,6,1):
            if board_array.get(i+j*5) == my_koma_number:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
    for i in range(3,0,-1):
        count = 0
        for j in range(0,7-i,1):
            if board_array.get(i+j*7) == my_koma_number:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0
    
    for i in range(7,25,6):
        count = 0
        for j in range(0,6,1):
            if board_array.get(i+j*7) == my_koma_number:
                count = count + 1
                if count == 4:
                    return True
            else:
                count = 0