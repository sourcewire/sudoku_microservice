const WebSocket = require('ws');

async function client() {
	
    //websocket server uri
    const uri = "ws://localhost:8765";

    //create websocket instance
    const websocket = new WebSocket(uri);

    //event handler for when the connection is open
    websocket.on('open', () => {
	//2d array grid converted to json
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
	//send grid
        websocket.send(grid);
    });

    //event handler for message from server
    websocket.on('message', (result) => {
        if (result) {
            console.log('Sudoku solved!');
        } else {
            console.log('Try again');
        }

        // close websocket connection after receiving the result
        websocket.close();
    });
}
//call client to init websocket communication
client();

