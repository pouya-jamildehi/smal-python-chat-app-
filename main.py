import socket
import threading
from tkinter.ttk import *
from tkinter import *


x=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x.bind(('127.0.0.1',14300))
x.listen(1)
client, spec = x.accept()
print("recive from", spec)
root = Tk()
def se():
    message = get_text.get()
    client.send(message.encode())
    labal = Label(root, text="send : " + message, fg="black")
    labal.pack(fill=X, side=TOP)
    get_text.delete(0, END)

def re():
    while True:
        data = client.recv(1024)
        label = Label(root, text="recive : "+data.decode(), fg="black")
        label.pack(fill=X, side=TOP)
        print("recived:" + data.decode())


get_text = Entry(root)
button = Button(root , text="Send" , command=se)

get_text = Entry(root)
button.pack(fill=X , side=BOTTOM)
get_text.pack(fill=X , side=BOTTOM)
root.geometry("400x600")
root.title("server")
root.resizable(width=False, height=False)



while True:
    threading.Thread(target=re).start()
    se()
    root.mainloop()

#client.close()




