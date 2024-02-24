import asyncio, websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:

        grid = '[[5, 3, 0, 0, 7, 0, 0, 0, 0],[6, 0, 0, 1, 9, 5, 0, 0, 0],[0, 9, 8, 0, 0, 0, 0, 6, 0],[8, 0, 0, 0, 6, 0, 0, 0, 3],[4, 0, 0, 8, 0, 3, 0, 0, 1],[7, 0, 0, 0, 2, 0, 0, 0, 6],[0,         6, 0, 0, 0, 0, 2, 8, 0],[0, 0, 0, 4, 1, 9, 0, 0, 5],[0, 0, 0, 0, 8, 0, 0, 7, 9]]'

        await websocket.send(grid)

        result = await websocket.recv()

        if result == '1':
            print('Sudoku solved!')
        else:
            print('Try again')
        
if __name__ == "__main__":
    asyncio.run(hello())
