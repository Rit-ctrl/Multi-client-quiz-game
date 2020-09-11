from socket import AF_INET, socket, SOCK_STREAM
from timeit import default_timer as timer
import sys, select, tkinter

HOST='';PORT=33000
BUFFERSIZE=1024

def start_game():

	print("Enter name : ",end="")
	name=input()
	client_socket.send(bytes(name,"utf8"))
	client_socket.recv(1024).decode("utf8")
	client_socket.recv(1024).decode("utf8")

	while(1):
		
		question=client_socket.recv(1024).decode("utf8")

		if question=="END_OF_QUIZ" :
			return

		print(question)
		# print the question in proper format
		print("You have 60 seconds to answer!")
		start_time=timer()
		i, o, e = select.select( [sys.stdin], [], [], 10 )
		time = 0
		if (i):
			ans=sys.stdin.readline().strip()
			end_time=timer()
			time=end_time-start_time
			print("You said", ans)
		else:
			ans='e'
			end_time=timer()
			print("Times up!")
			time=end_time-start_time

		client_socket.send(bytes(str(ans),"utf8"))
		print("ans sent")
		client_socket.send(bytes(str(time),"utf8"))
		print("time sent")

		flag=client_socket.recv(1).decode("utf8")

		if(int(flag)):
			print("Correct answer")
		else:
			print("Better luck next time")
			client_socket.close()
			return
		


if __name__ == "__main__":

	HOST=input('Enter host: ')
	PORT=input('Enter port: ')
	
	ADDR=(HOST,int(PORT))
	client_socket=socket(AF_INET,SOCK_STREAM)
	client_socket.connect(ADDR)

	start_game()
	# receive_thread=Thread(target=start_game)
	# receive_thread.start()
	# tkinter.mainloop()


