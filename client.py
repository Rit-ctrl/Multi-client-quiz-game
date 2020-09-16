from socket import AF_INET, socket, SOCK_STREAM
from timeit import default_timer as timer
from threading import Thread
import sys, select, tkinter, time

HOST='';PORT=33000
BUFFERSIZE=1024

HOST=input('Enter host: ')
PORT=input('Enter port: ')

ADDR=(HOST,int(PORT))
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)
start_time=0.0
sent = 0

def send_ans(ans):
	# end_time=timer()
	# time=end_time-start_time
	# print(time)
	# if time<=60:
	# 	client_socket.send(bytes(str(ans),"utf8"))
	# else:
	# 	client_socket.send(bytes(str("e"),"utf8"))
	# t_out = Thread(target=timeout).start()
	client_socket.send(bytes(str(ans),"utf8"))
	global sent
	sent = 1

def timeout():

	start_time = timer()
	global sent
	# print("tout cell")
	while(1):
		if (timer() - start_time > 60):
			client_socket.send(bytes(str("e"),"utf8"))
			client_socket.send(bytes(str(timer() - start_time),"utf8"))
			break
		else:
			if sent:
				# print("answer sent")
				client_socket.send(bytes(str(timer() - start_time),"utf8"))
				sent = 0
				return
			else:
				continue

def send_name(name):
	if(name!=''):
		client_socket.send(bytes(str(name),"utf8"))
		entry_field.destroy()
		send_button.destroy()

def quit_app ():
	exit(0)

top=tkinter.Tk();
top.title("Multiplayer Quiz")

messages_frame=tkinter.Frame(top)
scrollbar=tkinter.Scrollbar(messages_frame)

msg_list=tkinter.Listbox(messages_frame,height=15,width=50,yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

my_msg=tkinter.StringVar()
entry_field=tkinter.Entry(top,textvariable=my_msg)
entry_field.bind("<Return>", lambda x:send_name(my_msg.get()))
entry_field.pack()
send_button=tkinter.Button(top,text="Send",command=lambda:send_name(my_msg.get()))
send_button.pack()

option_a = tkinter.StringVar()
option_b = tkinter.StringVar()
option_c = tkinter.StringVar()
option_d = tkinter.StringVar()

button_a = tkinter.Button(
	    textvariable=option_a,
	    width=25,
	    height=3,
	    bg="blue",
	    fg="yellow",
		command=lambda: send_ans("a")
	)
button_b = tkinter.Button(
	textvariable=option_b,
	width=25,
	height=3,
	bg="blue",
	fg="yellow",
	command=lambda: send_ans("b")
)
button_c = tkinter.Button(
	textvariable=option_c,
	width=25,
	height=3,
	bg="blue",
	fg="yellow",
	command=lambda: send_ans("c")
)
button_d = tkinter.Button(
	textvariable=option_d,
	width=25,
	height=3,
	bg="blue",
	fg="yellow",
	command=lambda: send_ans("d")
)
quit_button = tkinter.Button(
	    text="QUIT !",
	    width=25,
	    height=5,
	    bg="blue",
	    fg="yellow",
		command=quit_app
	)

def start_game():

	# print("Enter name : ",end="")
	# name=input()
	# client_socket.send(bytes(name,"utf8"))
	global start_time
	## msg_list.insert(tkinter.END,"Welcome")
	msg_list.insert(tkinter.END,"Please enter your name and press send")

	# x=client_socket.recv(1024).decode("utf8")
	# msg_list.insert(tkinter.END,x)
	# print(x)
	x=client_socket.recv(1024).decode("utf8")
	msg_list.insert(tkinter.END,x)
	# print(x)
	client_socket.recv(6)
	button_a.pack()
	button_b.pack()
	button_c.pack()
	button_d.pack()
	while(1):

		question=client_socket.recv(1024).decode("utf8")

		if question=="END_OF_QUIZ" :
			break

		question=question.split(',')
		msg_list.delete(0,1)
		msg_list.insert(tkinter.END,question[0]+") "+question[1])
		msg_list.insert(tkinter.END,"You have 60 seconds to answer!")
		
		option_a.set("(A) "+question[2])
		option_b.set("(B) "+question[3])
		option_c.set("(C) "+question[4])
		option_d.set("(D) "+question[5])
		
		Thread(target=timeout).start()
			
			# else if (sent):
			# 		break
			# 	else:
			# 		continue

		# print("You have 60 seconds to answer!")
		# msg_list.insert(tkinter.END,"You have 60 seconds to answer!")
		# start_time=timer()
		# i, o, e = select.select( [sys.stdin], [], [], 60 )
		# time = 0
		# if (i):
			# ans=sys.stdin.readline().strip()
			# end_time=timer()
			# time=end_time-start_time
			# print("You said", ans)
		# else:
			# ans='e'
			# end_time=timer()
			# print("Times up!")
			# time=end_time-start_time

		# client_socket.send(bytes(str(ans),"utf8"))
		# print("ans sent")
		# client_socket.send(bytes(str(time),"utf8"))
		# print("time sent")

		flag=client_socket.recv(1).decode("utf8")

		if(int(flag)):
			pass
		else:
			msg_list.delete(0,1)
			msg=client_socket.recv(1024).decode("utf8")
			msg_list.insert(tkinter.END,msg)
			msg_list.insert(tkinter.END,"Better luck next time")
			client_socket.close()
			button_a.destroy()
			button_b.destroy()
			button_c.destroy()
			button_d.destroy()
			quit_button.pack()
			return
			# exit(0)

		# time.sleep(1)

	msg_list.delete(0,1)
	msg_list.insert(tkinter.END,"Waiting for other clients to complete")

	button_a.destroy()
	button_b.destroy()
	button_c.destroy()
	button_d.destroy()

	result=client_socket.recv(1024).decode("utf8")
	msg_list.delete(0)
	msg_list.insert(tkinter.END,"Leaderboard")
	x=1
	for player in result.split(";"):
		player_info=player.split(",")
		msg=str(x)+"   "+player_info[0]+"   "+str(round(float(player_info[1]),3))+"s"
		msg_list.insert(tkinter.END,msg)
		x=x+1
	msg_list.insert(tkinter.END,"Thank you!")

	quit_button.pack()
	

receive_thread=Thread(target=start_game)
receive_thread.start()
tkinter.mainloop()
client_socket.close()