from tkinter import *
from tkinter import messagebox
from customtkinter import CTkFrame
from PIL import ImageTk, Image 
#import win32gui, win32con

cal=Tk()
cal.title("Calculator")
cal.resizable(0,0)
cal.iconbitmap("Assets/Icon.ico")
cal.geometry(""+"+0+345")

main_color="#5e6ca1"
sel_color="#7e8cb7"

cal.config(bg=main_color)

def ent_txt(e):
  ent.delete(0, END)

c_frame=Frame(cal, bg=main_color)
c_frame.pack()

ent=Entry(c_frame, width=10, bg=main_color, font=('Arial', 35), bd=0, justify=RIGHT)
ent.insert(0, "0")
ent.bind("<FocusIn>", ent_txt)
ent.grid(row=1, column=0, columnspan=4, padx=10, pady=30)

options=ImageTk.PhotoImage(Image.open("Assets/OptionsLight.png"))
OptionsDark=ImageTk.PhotoImage(Image.open("Assets/OptionsDark.png"))

menu=Menubutton(cal, image=options, bg=main_color, activebackground=sel_color, bd=0)
menu.place(x=3, y=3)

home_menu=Menu(menu, bg=main_color, tearoff=0, activeborderwidth=0, activebackground=sel_color, activeforeground="black")
menu.config(menu=home_menu)

Themes=Menu(home_menu, bg=main_color, tearoff=0, activebackground=sel_color, activeforeground="black")
modes=Menu(home_menu, bg=main_color, tearoff=0, activebackground=sel_color, activeforeground="black")

# Button Function
from Btn_functions import *
set_entry(ent)
ent.bind("<Return>", equal_ent)

# Buttons def
btn_bg="white"

def enter1(a):
  btn_1.config(bg=sel_color)
def leave1(a):
  btn_1.config(bg=btn_bg)

def enter2(a):
  btn_2.config(bg=sel_color)
def leave2(a):
  btn_2.config(bg=btn_bg)

def enter3(a):
  btn_3.config(bg=sel_color)
def leave3(a):
  btn_3.config(bg=btn_bg)

def enter4(a):
  btn_4.config(bg=sel_color)
def leave4(a):
  btn_4.config(bg=btn_bg)

def enter5(a):
  btn_5.config(bg=sel_color)
def leave5(a):
  btn_5.config(bg=btn_bg)

def enter6(a):
  btn_6.config(bg=sel_color)
def leave6(a):
  btn_6.config(bg=btn_bg)

def enter7(a):
  btn_7.config(bg=sel_color)
def leave7(a):
  btn_7.config(bg=btn_bg)

def enter8(a):
  btn_8.config(bg=sel_color)
def leave8(a):
  btn_8.config(bg=btn_bg)

def enter9(a):
  btn_9.config(bg=sel_color)
def leave9(a):
  btn_9.config(bg=btn_bg)

def enter0(a):
  btn_0.config(bg=sel_color)
def leave0(a):
  btn_0.config(bg=btn_bg)

def enterpoint(a):
  btn_point.config(bg=sel_color)
def leavepoint(a):
  btn_point.config(bg=btn_bg)

def enterclear(a):
  btn_clear.config(bg=sel_color)
def leaveclear(a):
  btn_clear.config(bg=btn_bg)

# Buttons

activebg_btns="#2f343d"
activefg_btns="#b6e3ff"

btn_font=("Secular One", 17)

btn_1=Button(c_frame, text="1", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(1))
btn_1.bind("<Enter>", enter1)
btn_1.bind("<Leave>", leave1)

btn_2=Button(c_frame, text="2", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(2))
btn_2.bind("<Enter>", enter2)
btn_2.bind("<Leave>", leave2)

btn_3=Button(c_frame, text="3", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(3))
btn_3.bind("<Enter>", enter3)
btn_3.bind("<Leave>", leave3)

btn_4=Button(c_frame, text="4", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(4))
btn_4.bind("<Enter>", enter4)
btn_4.bind("<Leave>", leave4)

btn_5=Button(c_frame, text="5", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(5))
btn_5.bind("<Enter>", enter5)
btn_5.bind("<Leave>", leave5)

btn_6=Button(c_frame, text="6", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(6))
btn_6.bind("<Enter>", enter6)
btn_6.bind("<Leave>", leave6)

btn_7=Button(c_frame, text="7", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(7))
btn_7.bind("<Enter>", enter7)
btn_7.bind("<Leave>", leave7)

btn_8=Button(c_frame, text="8", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(8))
btn_8.bind("<Enter>", enter8)
btn_8.bind("<Leave>", leave8)

btn_9=Button(c_frame, text="9", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(9))
btn_9.bind("<Enter>", enter9)
btn_9.bind("<Leave>", leave9)

btn_0=Button(c_frame, text="0", font=btn_font, bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=22, pady=0.25, command=lambda: btn_num(0))
btn_0.bind("<Enter>", enter0)
btn_0.bind("<Leave>", leave0)

# def for operators

bgcolor=sel_color
opfont="GothamBlack"

operator_ent="white"

abgop="#004a77"
afgop="#b6e3ff"

def enterplus(b):
  btn_plus["background"]=operator_ent
def leaveplus(b):
  btn_plus["background"]=bgcolor

def enterminus(b):
  btn_minus["background"]=operator_ent
def leaveminus(b):
  btn_minus["background"]=bgcolor

def entermultiply(b):
  btn_multiply["background"]=operator_ent
def leavemultiply(b):
  btn_multiply["background"]=bgcolor

def enterdivide(b):
  btn_divide["background"]=operator_ent
def leavedivide(b):
  btn_divide["background"]=bgcolor

def enternegp(b):
  btn_negp["background"]=operator_ent
def leavenegp(b):
  btn_negp["background"]=bgcolor

def enterclose(b):
  btn_close["background"]=operator_ent
def leaveclose(b):
  btn_close["background"]=bgcolor

Backspace=ImageTk.PhotoImage(Image.open("Assets/Backspace.png"), height=36)
BackspaceDark=ImageTk.PhotoImage(Image.open("Assets/BackspaceDark.png"), height=36)

btn_plus=Button(c_frame, text="+", bg=bgcolor, activebackground=abgop, activeforeground=afgop, font=(opfont, 15), padx=20, pady=2.5, command=add)
btn_plus.bind("<Enter>", enterplus)
btn_plus.bind("<Leave>", leaveplus)

btn_minus=Button(c_frame, text="-", bg=bgcolor, activebackground=abgop, activeforeground=afgop, font=(opfont, 18),padx=20, pady=0.25, command=sub)
btn_minus.bind("<Enter>", enterminus)
btn_minus.bind("<Leave>", leaveminus)

btn_divide=Button(c_frame, text="÷", bg=bgcolor, activebackground=abgop, activeforeground=afgop, font=(opfont, 17),padx=18, pady=0.025, command=divide)
btn_divide.bind("<Enter>", enterdivide)
btn_divide.bind("<Leave>", leavedivide)

btn_multiply=Button(c_frame, text="×", bg=bgcolor, activebackground=abgop, activeforeground=afgop, font=(opfont, 18), padx=17, pady=0.25, command=multiply)
btn_multiply.bind("<Enter>", entermultiply)
btn_multiply.bind("<Leave>", leavemultiply)

btn_point=Button(c_frame, text="·", font=("GoogleSans", 15, 'bold'), bg=btn_bg, activebackground=activebg_btns, activeforeground=activefg_btns, padx=26, pady=2, command=lambda: btn_num("."))
btn_point.bind("<Enter>", enterpoint)
btn_point.bind("<Leave>", leavepoint)

btn_clear=Button(c_frame, text="                      ", image=Backspace, activebackground=activebg_btns, cursor="hand2", compound=CENTER, bg=btn_bg, command=clear_1)
btn_clear.bind("<Enter>", enterclear)
btn_clear.bind("<Leave>", leaveclear)

Exit=ImageTk.PhotoImage(Image.open("Assets/Exit1.png"), height=36)
ExitDM=ImageTk.PhotoImage(Image.open("Assets/ExitDM.png"), height=36)

btn_close=Button(c_frame, text="                      ", image=Exit, bg=bgcolor, activebackground=abgop, compound=CENTER, command=cal.destroy)
btn_close.bind("<Enter>", enterclose)
btn_close.bind("<Leave>", leaveclose)

btn_negp=Button(c_frame, text="+/-", bg=bgcolor, font=("GoogleSans", 16),  activebackground=abgop, activeforeground=afgop, padx=17, pady=2, command=lambda: btn_num("-"))
btn_negp.bind("<Enter>", enternegp)
btn_negp.bind("<Leave>", leavenegp)

# def for "AC" and "Equal"

funcFont = ("Oswald", 15, "bold")

def enterac(c):
  btn_Allclear["background"]="orange"
def leaveac(c):
  btn_Allclear["background"]="#00FF7F"

def entereq(c):
  btn_equ["background"]="grey"
def leaveeq(c):
  btn_equ["background"]="#323336"

btn_Allclear=Button(c_frame, text="AC", bg="#00FF7F", activebackground="orange", font=funcFont, cursor="hand2", padx=16, pady=2, command=delete_all)
btn_Allclear.bind("<Enter>", enterac)
btn_Allclear.bind("<Leave>", leaveac)

# Equals button has opfont "REMEMBER!!"

btn_equ=Button(c_frame, text="=", fg="white", bg="#323336", activebackground="grey", font=(opfont, 15), cursor="hand2", padx=19.5, pady=2.5, command=equal)
btn_equ.bind("<Enter>", entereq)
btn_equ.bind("<Leave>", leaveeq)

# Dark Mode Enter

ColorDark="#2f343d"
ColorDarkL="black"

def enterd1(f):
  btn_1["background"]=ColorDark
def leaved1(f):
  btn_1["background"]=ColorDarkL

def enterd2(f):
  btn_2["background"]=ColorDark
def leaved2(f):
  btn_2["background"]=ColorDarkL

def enterd3(f):
  btn_3["background"]=ColorDark
def leaved3(f):
  btn_3["background"]=ColorDarkL

def enterd4(f):
  btn_4["background"]=ColorDark
def leaved4(f):
  btn_4["background"]=ColorDarkL

def enterd5(f):
  btn_5["background"]=ColorDark
def leaved5(f):
  btn_5["background"]=ColorDarkL

def enterd6(f):
  btn_6["background"]=ColorDark
def leaved6(f):
  btn_6["background"]=ColorDarkL

def enterd7(f):
  btn_7["background"]=ColorDark
def leaved7(f):
  btn_7["background"]=ColorDarkL

def enterd8(f):
  btn_8["background"]=ColorDark
def leaved8(f):
  btn_8["background"]=ColorDarkL

def enterd9(f):
  btn_9["background"]=ColorDark
def leaved9(f):
  btn_9["background"]=ColorDarkL

def enterd0(f):
  btn_0["background"]=ColorDark
def leaved0(f):
  btn_0["background"]=ColorDarkL

def enterdpoint(f):
  btn_point["background"]=ColorDark
def leavedpoint(f):
  btn_point["background"]=ColorDarkL

def enterdclear(f):
  btn_clear["background"]=ColorDark
def leavedclear(f):
  btn_clear["background"]=ColorDarkL

def enterdeq(f):
  btn_equ["background"]="#ffeec0"
def leavedeq(f):
  btn_equ["background"]="white"

ColorDarkop="#40667d"
ColorDarkLop="#004a77"

def enterdplus(f):
  btn_plus["background"]=ColorDarkop
def leavedplus(f):
  btn_plus["background"]=ColorDarkLop

def enterdminus(f):
  btn_minus["background"]=ColorDarkop
def leavedminus(f):
  btn_minus["background"]=ColorDarkLop

def enterdmultiply(f):
  btn_multiply["background"]=ColorDarkop
def leavedmultiply(f):
  btn_multiply["background"]=ColorDarkLop

def enterddivide(f):
  btn_divide["background"]=ColorDarkop
def leaveddivide(f):
  btn_divide["background"]=ColorDarkLop

def enterdclose(f):
  btn_close["background"]=ColorDarkop
def leavedclose(f):
  btn_close["background"]=ColorDarkLop

def enterdnegp(f):
  btn_negp["background"]=ColorDarkop
def leavednegp(f):
  btn_negp["background"]=ColorDarkLop


# Dark Mode and Light Mode

def DarkMode():
  btnabg="#2f343d"
  btnafg="white"

  abg="grey"
  afg="black"

  menu.config(border=0, activebackground="#2f343d", activeforeground="white")
  Themes.config(bg="#2f343d", fg="white", activebackground=abg, activeforeground=afg)
  home_menu.config(bg="#2f343d", fg="white", activebackground=abg, activeforeground=afg)
  modes.config(bg="#2f343d", fg="white", activebackground=abg, activeforeground=afg)

  forg="#b6e3ff"
  bacg="black"
  operatorbg="#004a77"
  operatorfg="#b6e3ff"

  cal.config(bg="#37393c")

  btn_1.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_1.bind("<Enter>", enterd1)
  btn_1.bind("<Leave>", leaved1)

  btn_2.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_2.bind("<Enter>", enterd2)
  btn_2.bind("<Leave>", leaved2)

  btn_3.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_3.bind("<Enter>", enterd3)
  btn_3.bind("<Leave>", leaved3)

  btn_4.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_4.bind("<Enter>", enterd4)
  btn_4.bind("<Leave>", leaved4)
  
  btn_5.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_5.bind("<Enter>", enterd5)
  btn_5.bind("<Leave>", leaved5)
  
  btn_6.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_6.bind("<Enter>", enterd6)
  btn_6.bind("<Leave>", leaved6)
  
  btn_7.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_7.bind("<Enter>", enterd7)
  btn_7.bind("<Leave>", leaved7)
  
  btn_8.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_8.bind("<Enter>", enterd8)
  btn_8.bind("<Leave>", leaved8)
  
  btn_9.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_9.bind("<Enter>", enterd9)
  btn_9.bind("<Leave>", leaved9)
  
  btn_0.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_0.bind("<Enter>", enterd0)
  btn_0.bind("<Leave>", leaved0)

  btn_point.config(fg=forg, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_point.bind("<Enter>", enterdpoint)
  btn_point.bind("<Leave>", leavedpoint)

  btn_clear.config(image=BackspaceDark, bg=bacg, activebackground=btnabg, activeforeground=btnafg)
  btn_clear.bind("<Enter>", enterdclear)
  btn_clear.bind("<Leave>", leavedclear)

  btn_equ.config(bg="white", fg="black", activebackground="#ffeec0", activeforeground="black")
  btn_equ.bind("<Enter>", enterdeq)
  btn_equ.bind("<Leave>", leavedeq)

  abgdop="#004a77"
  afgdop="white"

  btn_plus.config(bg=operatorbg, fg=operatorfg, activebackground=abgdop, activeforeground=afgdop)
  btn_plus.bind("<Enter>", enterdplus)
  btn_plus.bind("<Leave>", leavedplus)

  btn_minus.config(bg=operatorbg, fg=operatorfg, activebackground=abgdop, activeforeground=afgdop)
  btn_minus.bind("<Enter>", enterdminus)
  btn_minus.bind("<Leave>", leavedminus)

  btn_divide.config(bg=operatorbg, fg=operatorfg, activebackground=abgdop, activeforeground=afgdop)
  btn_divide.bind("<Enter>", enterddivide)
  btn_divide.bind("<Leave>", leaveddivide)

  btn_multiply.config(bg=operatorbg, fg=operatorfg, activebackground=abgdop, activeforeground=afgdop)
  btn_multiply.bind("<Enter>", enterdmultiply)
  btn_multiply.bind("<Leave>", leavedmultiply)

  btn_close.config(image=ExitDM, bg=operatorbg, activebackground=abgdop)
  btn_close.bind("<Enter>", enterdclose)
  btn_close.bind("<Leave>", leavedclose)

  btn_negp.config(bg=operatorbg, fg=operatorfg, activebackground=abgdop, activeforeground=afgdop)
  btn_negp.bind("<Enter>", enterdnegp)
  btn_negp.bind("<Leave>", leavednegp)


def LightMode():
  bglm="white"
  fglm="black"
  btnafgD="#b6e3ff"
  btnabgD="#2f343d"

  menu.config(image=options, bg=main_color, activebackground=sel_color, border=0)
  cal.config(bg=main_color)
  ent.config(bg=main_color, fg="black", insertbackground="black")

  home_menu.config(bg=main_color, fg="black", activebackground=sel_color, activeforeground="black")
  Themes.config(bg=main_color, fg="black", activebackground=sel_color, activeforeground="black")
  modes.config(bg=main_color, fg="black", activebackground=sel_color, activeforeground="black")

  btn_1.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_1.bind("<Enter>", enter1)
  btn_1.bind("<Leave>", leave1)

  btn_2.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_2.bind("<Enter>", enter2)
  btn_2.bind("<Leave>", leave2)

  btn_3.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_3.bind("<Enter>", enter3)
  btn_3.bind("<Leave>", leave3)
  
  btn_4.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_4.bind("<Enter>", enter4)
  btn_4.bind("<Leave>", leave4)
  
  btn_5.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_5.bind("<Enter>", enter5)
  btn_5.bind("<Leave>", leave5)
  
  btn_6.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_6.bind("<Enter>", enter6)
  btn_6.bind("<Leave>", leave6)
  
  btn_7.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_7.bind("<Enter>", enter7)
  btn_7.bind("<Leave>", leave7)
  
  btn_8.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_8.bind("<Enter>", enter8)
  btn_8.bind("<Leave>", leave8)
  
  btn_9.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_9.bind("<Enter>", enter9)
  btn_9.bind("<Leave>", leave9)
  
  btn_0.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_0.bind("<Enter>", enter0)
  btn_0.bind("<Leave>", leave0)

  btn_point.config(bg=bglm, fg=fglm, activebackground=btnabgD, activeforeground=btnafgD)
  btn_point.bind("<Enter>", enterpoint)
  btn_point.bind("<Leave>", leavepoint)

  btn_clear.config(image=Backspace, bg=bglm, activebackground=btnabgD)
  btn_clear.bind("<Enter>", enterclear)
  btn_clear.bind("<Leave>", leaveclear)

  btn_plus.config(bg=bgcolor, fg=fglm, activebackground=abgop, activeforeground=afgop)
  btn_plus.bind("<Enter>", enterplus)
  btn_plus.bind("<Leave>", leaveplus)

  btn_minus.config(bg=bgcolor, fg=fglm, activebackground=abgop, activeforeground=afgop)
  btn_minus.bind("<Enter>", enterminus)
  btn_minus.bind("<Leave>", leaveminus)

  btn_divide.config(bg=bgcolor, fg=fglm, activebackground=abgop, activeforeground=afgop)
  btn_divide.bind("<Enter>", enterdivide)
  btn_divide.bind("<Leave>", leavedivide)

  btn_multiply.config(bg=bgcolor, fg=fglm, activebackground=abgop, activeforeground=afgop)
  btn_multiply.bind("<Enter>", entermultiply)
  btn_multiply.bind("<Leave>", leavemultiply)

  btn_close.config(image=Exit, bg=bgcolor, fg=fglm, activebackground=abgop)
  btn_close.bind("<Enter>", enterclose)
  btn_close.bind("<Leave>", leaveclose)

  btn_negp.config(bg=bgcolor, fg=fglm, activebackground=abgop, activeforeground=afgop)
  btn_negp.bind("<Enter>", enternegp)
  btn_negp.bind("<Leave>", leavenegp)

  btn_equ.config(bg="#323336", fg=bglm)
  btn_equ.bind("<Enter>", entereq)
  btn_equ.bind("<Leave>", leaveeq)

# GST Calculator

def gst_calc():
  global gf
  
  # btn disable
  ent.config(state=DISABLED)
  btn_1.config(state=DISABLED)
  btn_2.config(state=DISABLED)
  btn_3.config(state=DISABLED)
  btn_4.config(state=DISABLED)
  btn_5.config(state=DISABLED)
  btn_6.config(state=DISABLED)
  btn_7.config(state=DISABLED)
  btn_8.config(state=DISABLED)
  btn_9.config(state=DISABLED)
  btn_0.config(state=DISABLED)
  btn_point.config(state=DISABLED)
  btn_equ.config(state=DISABLED)
  btn_plus.config(state=DISABLED)
  btn_minus.config(state=DISABLED)
  btn_divide.config(state=DISABLED)
  btn_multiply.config(state=DISABLED)
  btn_negp.config(state=DISABLED)
  btn_Allclear.config(state=DISABLED)
  btn_clear.config(state=DISABLED)
  menu.config(state=DISABLED)

  def gst_d():
    gst_b_btn.destroy()
    gf.destroy()

    # btn normal
    ent.config(state=NORMAL)
    btn_1.config(state=NORMAL)
    btn_2.config(state=NORMAL)
    btn_3.config(state=NORMAL)
    btn_4.config(state=NORMAL)
    btn_5.config(state=NORMAL)
    btn_6.config(state=NORMAL)
    btn_7.config(state=NORMAL)
    btn_8.config(state=NORMAL)
    btn_9.config(state=NORMAL)
    btn_0.config(state=NORMAL)
    btn_point.config(state=NORMAL)
    btn_equ.config(state=NORMAL)
    btn_plus.config(state=NORMAL)
    btn_minus.config(state=NORMAL)
    btn_divide.config(state=NORMAL)
    btn_multiply.config(state=NORMAL)
    btn_negp.config(state=NORMAL)
    btn_Allclear.config(state=NORMAL)
    btn_clear.config(state=NORMAL)
    menu.config(state=NORMAL)

  def b_en(a):
    gst_b_btn.config(bg=sel_color)
  def b_le(a):
    gst_b_btn.config(bg=main_color)

  gst_b_btn=Button(cal, image=back, width=20, height=20, bg=main_color, bd=0, command=gst_d)
  gst_b_btn.bind("<Enter>", b_en)
  gst_b_btn.bind("<Leave>", b_le)
  gst_b_btn.place(x=3, y=3)

  gf=CTkFrame(c_frame, fg_color="#ffccd9", bg_color="transparent", border_width=2, border_color="black", corner_radius=20)
  gf.place(x=4, y=28)

  orilbl=Label(gf, text="Enter the Original Price", font=("Arial", 14, "bold"), bg="#ffccd9")
  orilbl.pack(pady=(10, 5))

  def gst():
    try:
      gstamt=float(netp.get())-float(orip.get())
      gstp=str(int(gstamt*100/float(orip.get())))
      glbl.config(text=(gstp + "%" + " GST"))
    except ValueError:
      messagebox.showinfo("Information", "Type Something")

  def gst_ent(e):
    gst()

  orip=Entry(gf, width=15, bg=main_color, font=("Arial", 25), bd=3)
  orip.bind("<Return>", gst_ent)
  orip.pack(padx=3)

  netlbl=Label(gf, text="Enter the Net Price", font=("Arial", 14, "bold"), bg="#ffccd9")
  netlbl.pack(pady=(8, 5))

  netp=Entry(gf, width=15, bg=main_color, font=("Arial", 25), bd=3)
  netp.bind("<Return>", gst_ent)
  netp.pack(padx=3)

  gbtn=Button(gf, text="Click for Answer", font=("Arial", 13, "bold"), bg="#eaeff9", command=gst)
  gbtn.pack(pady=(7, 10))

  glbl=Label(gf, text="", font=("Arial", 13, "bold"), bg="#ffccd9")
  glbl.pack(pady=(0, 5))

# Bytes Converter

back=ImageTk.PhotoImage(Image.open("Assets/Backarrow2.png"))

def bycal():
  global byf

  # btn disable
  ent.config(state=DISABLED)
  btn_1.config(state=DISABLED)
  btn_2.config(state=DISABLED)
  btn_3.config(state=DISABLED)
  btn_4.config(state=DISABLED)
  btn_5.config(state=DISABLED)
  btn_6.config(state=DISABLED)
  btn_7.config(state=DISABLED)
  btn_8.config(state=DISABLED)
  btn_9.config(state=DISABLED)
  btn_0.config(state=DISABLED)
  btn_point.config(state=DISABLED)
  btn_equ.config(state=DISABLED)
  btn_plus.config(state=DISABLED)
  btn_minus.config(state=DISABLED)
  btn_divide.config(state=DISABLED)
  btn_multiply.config(state=DISABLED)
  btn_negp.config(state=DISABLED)
  btn_Allclear.config(state=DISABLED)
  btn_clear.config(state=DISABLED)
  menu.config(state=DISABLED)

  byf=CTkFrame(c_frame, fg_color="#ffccd9", border_width=2, border_color="black", corner_radius=20)
  byf.place(x=5, y=28)

  def byd():
    by_b_btn.destroy()
    byf.destroy()

    # btn normal
    ent.config(state=NORMAL)
    btn_1.config(state=NORMAL)
    btn_2.config(state=NORMAL)
    btn_3.config(state=NORMAL)
    btn_4.config(state=NORMAL)
    btn_5.config(state=NORMAL)
    btn_6.config(state=NORMAL)
    btn_7.config(state=NORMAL)
    btn_8.config(state=NORMAL)
    btn_9.config(state=NORMAL)
    btn_0.config(state=NORMAL)
    btn_point.config(state=NORMAL)
    btn_equ.config(state=NORMAL)
    btn_plus.config(state=NORMAL)
    btn_minus.config(state=NORMAL)
    btn_divide.config(state=NORMAL)
    btn_multiply.config(state=NORMAL)
    btn_negp.config(state=NORMAL)
    btn_Allclear.config(state=NORMAL)
    btn_clear.config(state=NORMAL)
    menu.config(state=NORMAL)

  def b_en(a):
    by_b_btn.config(bg=sel_color)
  def b_le(a):
    by_b_btn.config(bg=main_color)

  by_b_btn=Button(cal, image=back, width=20, height=20, bg=main_color, bd=0, command=byd)
  by_b_btn.bind("<Enter>", b_en)
  by_b_btn.bind("<Leave>", b_le)
  by_b_btn.place(x=3, y=3)

  gblbl=Label(byf, text="Enter the Giga Byte", font=("Arial", 16, "bold"), bg="#ffccd9")
  gblbl.pack(pady=(10, 5))

  def gtb(): 
    try:
      b=float(gb.get())*(2**10)**3
      glbl.config(text=(float(gb.get()), "is", b, "Byte"))
    except ValueError:
      messagebox.showinfo("Information", "Type Something")

  def gb_ent(e):
    gtb()

  gb=Entry(byf, width=15, bg=main_color, font=("Arial", 25), bd=2)
  gb.bind("<Return>", gb_ent)
  gb.pack(padx=3)

  gbtn=Button(byf, text="Click for Answer", font=("Arial", 13, "bold"), bg="#eaeff9", command=gtb)
  gbtn.pack(pady=10)

  glbl=Label(byf, text="", bg="#ffccd9", font=("Arial", 13, "bold"))
  glbl.pack(pady=(0, 5))

# Menu

home_menu.add_cascade(label="Themes", menu=Themes)
home_menu.add_cascade(label="Modes", menu=modes)

Themes.add_command(label="Dark Theme", command=DarkMode)
Themes.add_command(label="Light Theme", command=LightMode)

modes.add_cascade(label="GST Calculator", command=gst_calc)
modes.add_cascade(label="Bytes Converter", command=bycal)

# Positions

otth=7
ffis=6
sen=5

btn_1.grid(row=otth, column=0)
btn_2.grid(row=otth, column=1)
btn_3.grid(row=otth, column=2)

btn_4.grid(row=ffis, column=0)
btn_5.grid(row=ffis, column=1)
btn_6.grid(row=ffis, column=2)

btn_7.grid(row=sen, column=0)
btn_8.grid(row=sen, column=1)
btn_9.grid(row=sen, column=2)

btn_0.grid(row=8, column=0)

btn_Allclear.grid(row=4, column=0)
btn_clear.grid(row=8, column=2)
btn_close.grid(row=4, column=1)
btn_negp.grid(row=4, column=2)

btn_divide.grid(row=4, column=3)
btn_multiply.grid(row=5, column=3)
btn_minus.grid(row=6, column=3)
btn_plus.grid(row=7, column=3)
btn_equ.grid(row=8, column=3)
btn_point.grid(row=8, column=1)


#hide=win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide, win32con.SW_HIDE)


cal.mainloop()