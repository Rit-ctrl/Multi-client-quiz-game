from socket import AF_INET, socket, SOCK_STREAM
import tkinter

def start_game():
    print("Enter name : ",end="")
    name=input()
    client_socket.send(bytes(name,"utf8"))
    while(1):
        question=client_socket.recv(1024)
        print(question)


if __name__ == "__main__":
    # HOST=input('Enter host: ')
    # PORT=input('Enter port: ')
    HOST='';PORT=33000
    BUFFERSIZE=1024
    ADDR=(HOST,PORT)
    client_socket=socket(AF_INET,SOCK_STREAM)
    client_socket.connect(ADDR)

    start_game()
    # receive_thread=Thread(target=start_game)
    # receive_thread.start()
    # tkinter.mainloop()


