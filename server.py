from socket import AF_INET,socket,SOCK_STREAM
from threading import Thread

clients = {}
addresses= {}

HOST =''
PORT = 33000
BUFFERSIZE=1024
ADDR=(HOST,PORT)
SERVER=socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

all_times = []

def accept_in_connections():

	while len(clients) <=4:
		client,client_addr=SERVER.accept()
		print("%s:%s has joined fellows."%client_addr)
		client.send(bytes("greetings from ritzz!"+"now enter your name and press enter","utf8"))
		addresses[client]=client_addr
		Thread(target=handle_client,args=(client,)).start()


def handle_client(client):

	name=client.recv(BUFFERSIZE).decode("utf8")
	welcome='Welcome %s! If you want to quit,you hit {quit} to exit.' %name
	client.send(bytes(welcome,"utf8"))
	msg='%s has joined the chat XD' %name
	print(welcome, msg)

	if (len(clients) == 4):
		start_game()

def start_game(name):
	
	q_file = open("question.csv", "r")
	line = q_file.readline()
	line = q_file.readline()

	time = 0

	while(line != ''):

		line = line.split(sep=',')
		
		send_q = line[0:5]
		ans = line[6]

		# recv (answer, time) from client, compare with ans, add time
		# if answer is 'e' timeout, terminate thread

		print(q_no + ". " + question)
		line = q_file.readline()

	# time = time / 5
	times.append({
        "name" : name,
        "time" : 10
    })

if __name__ == "__main__":
	
	# start_game()
	ACCEPT_THREAD=Thread(target=accept_in_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()

	all_times = sorted(all_times, key=lambda x: x["time"])

	# broadcast all_times to all clients