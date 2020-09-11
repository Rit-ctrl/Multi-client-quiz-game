from socket import AF_INET, socket, SOCK_STREAM
from timeit import default_timer as timer
from threading import Thread
import sys, select, tkinter

HOST='';PORT=33001
BUFFERSIZE=1024

HOST=input('Enter host: ')
PORT=input('Enter port: ')

ADDR=(HOST,int(PORT))
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)



top=tkinter.Tk();
top.title("Messenger")

messages_frame=tkinter.Frame(top)
my_msg=tkinter.StringVar()
my_msg.set("Type your message here")
scrollbar=tkinter.Scrollbar(messages_frame)

msg_list=tkinter.Listbox(messages_frame,height=15,width=50,yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
msg_list.pack()

msg_list.insert(tkinter.END,"hi there")
msg_list.insert(tkinter.END,"Whats up")

messages_frame.pack()



def start_game():

	print("Enter name : ",end="")
	name=input()
	client_socket.send(bytes(name,"utf8"))
	client_socket.recv(1024).decode("utf8")
	client_socket.recv(1024).decode("utf8")

	while(1):
		
		question=client_socket.recv(1024).decode("utf8")

		if question=="END_OF_QUIZ" :
			break

		msg_list.insert(tkinter.END,question)
		# print("You have 60 seconds to answer!")
		msg_list.insert(tkinter.END,"You have 60 seconds to answer!")
		start_time=timer()
		i, o, e = select.select( [sys.stdin], [], [], 60 )
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
		# print("ans sent")
		client_socket.send(bytes(str(time),"utf8"))
		# print("time sent")

		flag=client_socket.recv(1).decode("utf8")

		if(int(flag)):
			print("Correct answer")
		else:
			print("Better luck next time")
			client_socket.close()
			break
			# exit(0)

	button = tkinter.Button(
	    text="QUIT !",
	    width=25,
	    height=5,
	    bg="blue",
	    fg="yellow",
		command=quit_app
	)
	button.pack()
	
<<<<<<< HEAD
=======
	ADDR=(HOST,int(PORT))
	client_socket=socket(AF_INET,SOCK_STREAM)
	client_socket.connect(ADDR)

	start_game()
	result=client_socket.recv(1024).decode("utf8")
	print(result)
	# receive_thread=Thread(target=start_game)
	# receive_thread.start()
	# tkinter.mainloop()
>>>>>>> 21aa2a358d75a7a10708efeff6445b1706effd52

def quit_app ():
	exit(0)

receive_thread=Thread(target=start_game)
receive_thread.start()
tkinter.mainloop()