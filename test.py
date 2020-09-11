import tkinter

# window = tk.Tk()

# test = "Hello, Tkinter"
# label = tk.Label(
#     text=test,
#     foreground="white",  # Set the text color to white
#     background="black",  # Set the background color to black
# 		width=100,
#     height=10
# )

# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# label.pack()
# button.pack()

# msg_list=tk.Listbox(messages_frame,height=15,width=50,yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
# msg_list.pack(side=tk.LEFT,fill=tk.BOTH)
# msg_list.pack()

# window.mainloop()

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

# entry_field=tkinter.Entry(top,textvariable=my_msg)
# entry_field.bind("<Return>",send)
# entry_field.pack()
# send_button=tkinter.Button(top,text="Send",command=send)
# send_button.pack()

# top.protocol("WM_DELETE_WINDOW",on_closing)

top.mainloop()