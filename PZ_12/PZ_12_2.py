root=Tk()
root.title("register")
root.geometry('400x300')
root.configure(bg='green')
root.resizable(height="false", width="false")

lb1= Label(root, text="Введите первое число",fg="white", bg="green", pady=10, width=100, font=('Arial', '12', 'bold'), anchor='w')
lb1.place(x=25,y=50)
ent1 = Entry()
ent1.place(x=250, y=63)
lb2= Label(root, text="Введите второе число",fg="white", bg="green", pady=10, width=100, font=('Arial', '12', 'bold'), anchor='w')
lb2.place(x=25,y=100)
ent2 = Entry()
ent2.place(x=250, y=113)
butt = Button(root, text="Отправить", fg="white", bg="#284b63")
butt.bind('<Button-1>', zadacha)
butt.place(x=160, y=153)

root.mainloop()