from tkinter import *
from speedtest import Speedtest

def update_text():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps") 


root = Tk()
root.title("Check Internet Speed_test")
root.configure(bg = 'green')
root.geometry('300x250')
button = Button(root, text="Get Speed", width=30, command=update_text, bg = 'black', fg = 'white')
button.pack()
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()

root.mainloop()