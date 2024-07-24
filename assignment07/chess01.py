import time

judit = 0.1
opponent_time = 0.5
opponent = 3
move_pairs =  30

def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        
        time.sleep(judit)
        print(f"board-{x} {i+1} judit made a move")
        
        time.sleep(opponent_time)
        print(f"board-{x} {i+1} opponent made a move")
        
    print (f'Board {x} ->>>>>>>>>>>>>>>>>> finish moving {round(time.perf_counter() - board_start_time)}sec\n')
    return round(time.perf_counter() - board_start_time)

if __name__ == "__main__":
    start_time = time.perf_counter()
    board_time = 0
    for board in range(opponent):
        board_time += game(board)
    
    print(f'Board finish {board_time} sec')
    print(f'Finish at {round(time.perf_counter() - start_time)}')