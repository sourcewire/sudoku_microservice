const WebSocket = require('ws');

async function client() {
    const uri = "ws://localhost:8765";
    const websocket = new WebSocket(uri);

    websocket.on('open', () => {
        const grid = JSON.stringify([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]);

        websocket.send(grid);
    });

    websocket.on('message', (result) => {
        if (result) {
            console.log('Sudoku solved!');
        } else {
            console.log('Try again');
        }

        // Close the WebSocket connection after receiving the result
        websocket.close();
    });
}

client();

