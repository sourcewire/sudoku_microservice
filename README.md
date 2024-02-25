Communication contract:

A.How to request data: To request data first set up a websocket instance with the same port number as the server. The set up the event handler for when the connection is established. In the event handler perform the conversion from 2d array to json. Then send the json to the server with websocket.send() so that it can evaluate it and return pass/fail.

    //websocket server uri
    const uri = "ws://localhost:8765";

    //create websocket instance
    const websocket = new WebSocket(uri);

    //event handler for when the connection is open
    websocket.on('open', () => {

               //convert sudoku attempt to json here


        websocket.send(attempt);
    });

B.How to recieve data: To recieve data, setup a event handler to reciver data from server. Once data has been recieved, use the data to tell the user if theur solution passed or failed. Then close the connection. Remember to call client() at the bottom of the file to initialize the websocket communication. 


    //event handler for message from server
    websocket.on('message', (result) => {
        
	//get result from server and console.log pass/fail


       // close websocket connection after receiving the result
        websocket.close();
    });
}

//call client to init websocket communication
client();


C.UML sequence diagram:

![UML diagram](https://github.com/sourcewire/sudoku_microservice/blob/main/sudoku_ms(1).png?raw=true)
