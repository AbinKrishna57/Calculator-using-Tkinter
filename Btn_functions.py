from tkinter import END

def set_entry(entry_widget):
  global ent
  ent = entry_widget

def btn_num(num):
  current=ent.get()
  ent.delete(0, END)
  ent.insert(0, str(current) + str(num))

def delete_all():
  ent.delete(0, END)

def clear_1():
  a=ent.get()
  ent.delete(len(a)-1, END)

def add():
  first_number=ent.get()
  global f_num
  global math
  math="addition"
  f_num=float(first_number)
  ent.delete(0, END)

def sub():
  first_number=ent.get()
  global f_num
  global math
  math="subtraction"
  f_num=float(first_number)
  ent.delete(0, END)

def divide():
  first_number=ent.get()
  global f_num
  global math
  math="divition"
  f_num=float(first_number)
  ent.delete(0, END)

def multiply():
  first_number=ent.get()
  global f_num
  global math
  math="multiplication"
  f_num=float(first_number)
  ent.delete(0, END)

def equal():
  second_number=float(ent.get())
  ent.delete(0, END)

  if math == "addition":
    ent.insert(0, f_num+float(second_number))

  elif math == "subtraction":
    ent.insert(0, f_num-(float(second_number)))

  elif math == "divition":
    ent.insert(0, f_num/float(second_number))

  elif math == "multiplication":
    ent.insert(0, f_num*float(second_number))

# By Pressing Enter this Works

def equal_ent(a):
  equal()

