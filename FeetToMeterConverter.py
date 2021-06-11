from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()  # help to create application window ,Window contains application container.Tk is a class which create window
window.title("Feet to Meter  Conversion App")  # using title function
window.configure(background="light green")  # By using configure fuction we can give bg color
window.geometry("320x220")  # geometry helps to set width and height
window.resizable(width=False, height=False)  # with this the idth and height can not be changed by user


def convert():
    value = float(ft_entry.get())  # get() function took the number which is given in ft_entry
    meter = value * 0.3048  # 1 feet=0.3048 meter
    mt_value.set("%.4f" % meter)  #set for 4 decimal points...set the value of mt_value

def clear():
    ft_value.set("")
    mt_value.set("")



ft_lbl = Label(window, text="Feet", bg="brown", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15,
            pady=15)  # pady means verticle distance,padx horizantally...Grid works like a table so the positions are based as a table

ft_value = DoubleVar()  # DouvleVar() helps to enter data type....decimal,float everything
ft_entry = Entry(window, textvariable=ft_value,
                 width=14)  # textvariable contains ft_value which uses data type by DoubleVar()
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, "end")  # Delete anything from 0 when the application launches first time

mt_lbl = Label(window, text="Meter", bg="Green", fg="white", width=14)
mt_lbl.grid(column=0, row=1,
            pady=30)  # pady means verticle distance,padx horizantally...Grid works like a table so the positions are based as a table

mt_value = DoubleVar()  # DouvleVar() helps to enter data type....decimal,float everything
mt_entry = Entry(window, textvariable=mt_value,
                 width=14)  # textvariable contains ft_value which uses data type by DoubleVar()
mt_entry.grid(column=1, row=1)
mt_entry.delete(0, "end")  # Delete anything from 0 when the application launches first time

convert_btn = Button(window, text="Convert", bg="purple", fg="white", width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

clear_btn = Button(window, text="Clear", bg="black", fg="white", width=14, command=clear) # command helps to run/calculate the fuction
clear_btn.grid(column=1, row=3, padx=15)

window.mainloop()  # mainloop function hich runs the application
