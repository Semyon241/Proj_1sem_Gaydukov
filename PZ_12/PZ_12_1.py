from tkinter import *
from tkinter import ttk

root = Tk()
root.title('registration')
root.geometry('500x510+700+200')
root.resizable(0, 0)
root['bg'] = 'white'

style = ttk.Style()

var = IntVar()

title = Label(text='Форма регистрации пользователя',
              font='Arial 12 bold',
              fg='#525252',
              bg='white')
title.place(x=113, y=10)

frame = Frame(width=440, height=450,
              highlightbackground='#808080',
              highlightthickness=3,
              bg='white')
frame.place(x=30, y=40)

name_label = Label(text='Ваше имя:', font='Arial 11', fg='#525252', bg='white')
name_label.place(x=40, y=49)
name_entry = Entry(bg='#C5C5C5', bd=0)
name_entry.place(x=170, y=48, height=27, width=280)

pass_label = Label(text='Пароль:', font='Arial 11', fg='#525252', bg='white')
pass_label.place(x=40, y=85)
pass_entry = Entry(bg='#C5C5C5', bd=0)
pass_entry.place(x=170, y=84, width=280, height=27)

age_label = Label(text='Возраст:', font='Arial 11', fg='#525252', bg='white')
age_label.place(x=40, y=121)
age_entry = Entry(bg='#C5C5C5', bd=0)
age_entry.place(x=170, y=120, width=280, height=27)

pol_label = Label(text='Пол:', font='Arial 11', fg='#525252', bg='white')
pol_label.place(x=40, y=156)
male_label = Label(text='Мужской', font='Arial 11', fg='#525252', bg='white')
male_label.place(x=167, y=155)
male_radiobutton = Radiobutton(variable=var, value=1)
male_radiobutton.place(x=230, y=155)
female_label = Label(text='Женский', font='Arial 11', fg='#525252', bg='white')
female_label.place(x=360, y=155)
female_radiobutton = Radiobutton(variable=var, value=0)
female_radiobutton.place(x=425, y=155)

hobbies_label = Label(text='Ваши увлечения:', font='Arial 11', fg='#525252', bg='white')
hobbies_label.place(x=40, y=188)

music_label = Label(text='Музыка', font='Arial 11', fg='#525252', bg='white')
music_label.place(x=167, y=188)
music_checkbutton = Checkbutton()
music_checkbutton.place(x=223, y=188)

video_label = Label(text='Видео', font='Arial 11', fg='#525252', bg='white')
video_label.place(x=265, y=188)
video_checkbutton = Checkbutton()
video_checkbutton.place(x=313, y=188)

draw_label = Label(text='Рисование', font='Arial 11', fg='#525252', bg='white')
draw_label.place(x=350, y=188)
draw_checkbutton = Checkbutton()
draw_checkbutton.place(x=428, y=188)

country_label = Label(text='Ваша страна:', font='Arial 11', fg='#525252', bg='white')
country_label.place(x=40, y=224)
country_combobox = ttk.Combobox()
country_combobox.place(x=167, y=224, height=27, width=285)

city_label = Label(text='Ваш город:', font='Arial 11', fg='#525252', bg='white')
city_label.place(x=40, y=258)
city_combobox = ttk.Combobox()
city_combobox.place(x=167, y=258, height=27, width=285)

about_label = Label(text='Кратко о себе:', font='Arial 11', fg='#525252', bg='white')
about_label.place(x=40, y=295)
about_text = Text(bg='#C5C5C5')
about_text.place(x=167, y=295, height=60, width=285)

task_label = Label(text='Решите пример, запишите результат в поле ниже',
                   font='Arial 11', fg='#525252', bg='white')
task_label.place(x=40, y=370)
task_entry = Entry(bg='#C5C5C5', bd=0)
task_entry.place(x=167, y=415, height=27, width=285)

button_in = Button(text='Отменить ввод', bg='#C5C5C5',
                   font='Arial 11', fg='#3B3B3B', bd=0)
button_in.place(x=167, y=450, height=25, width=120)
button_accept = Button(text='Данные подтверждаю', bg='#C5C5C5',
                       font='Arial 11', fg='#3B3B3B', bd=0)
button_accept.place(x=295, y=450, width=158, height=25)


root.mainloop()
