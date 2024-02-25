import json, asyncio, websockets


def sudoku_verifier(sudoku_grid):
    #creates lists of 9 empty sets
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    #loop over grid
    for i in range(9):
        for j in range(9):
            #get num in current cell
            num = sudoku_grid[i][j]
            if num == 0:
                continue
            
            #calculate the index of the 3x3 subgrid where the current cell is located
            subgrid_index = (i // 3) * 3 + j // 3
            
            #if current num is already in the grid, return false
            if num in rows[i] or num in cols[j] or num in subgrids[subgrid_index]:
                return 0

            #add the num
            rows[i].add(num)
            cols[j].add(num)
            subgrids[subgrid_index].add(num)

    return 1



#recieve json array and return 1 for pass and 0 for fail
async def sudoku_reply(websocket):

    #get json array from client
    json_attempt = await websocket.recv()

    #convery json to python list
    attempt_list = json.loads(json_attempt)

    print("Checking solution...")

    #call python list on sudoku_verifier to solve
    if sudoku_verifier(attempt_list):
        await websocket.send('1')#if it solves the puzzle, return 1
    else:
        await websocket.send('0')#else return 0



#set up websocket server
async def main():
    async with websockets.serve(sudoku_reply, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())

























