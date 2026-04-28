"d" #!\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\     
'''
import math 
r = float(input("radius: "))
h = float(input("height: "))
v = math.pi * math.pow(r, 2) * h 
print(f"silindirdin kolemi: {v:.2f}")
'''





#!\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\CALCULATOR\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import tkinter as tk # grafik ayna ushin kerekli kitapxana
from tkinter import messagebox # shiqqan qateliklerdi aynada shigariw ushin kerekli kitapxana
import math # matematika ammelerdi qollaniw ushin kerekli kitapxana 

# algaritm bolimi (funkciyalar bolimi)
def calculate():
    # ten degen knopkani basqanda kiritilgen sanlardi esaplaw ushin kerekli knopka ham funkciya
    try:
        #paydalaniwshi esaplaw kerek bolgan magliwmatlardi aliw ushin 
        expression = entry.get() # kiritilgen ifodani aliw
        result = eval(expression) #kiritilgen ifodani esaplaw
        entry.delete(0, tk.END) # kiritilgen magliwmat qate bolsa oshiriw
        entry.insert(tk.END, str(result)) # esaplangan magluwmatti ekranda shigariw ui yamasa displayga shigariw
    except Exception :
        messagebox.showerror("qate" )        
def sqrt_calc():
