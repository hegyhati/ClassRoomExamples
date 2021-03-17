from tkinter import *

def button_clicked():
    print("click")
    Label(frame,text="inserted by click on button").pack(side="bottom")

window = Tk()
window.title('Demo GUI application')

frame = Frame(window, bg="green")
frame.pack(side="top")

button=Button(frame,text="This is an example button",command=button_clicked)
button.pack()

for i in range(3):
    Label(window,text="[{}]".format(i+3), fg="red", bg="blue", font=('Arial',24)).pack(side="left" if i%2 else "right", padx=5, pady=40)

window.mainloop()






