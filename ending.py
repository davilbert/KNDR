import numpy as np
import matplotlib
from matplotlib import pylab,mlab,pyplot,cm
plt = pyplot
from mpl_toolkits.mplot3d import Axes3D
from math import exp,sin,cos
from pylab import *
from tkinter import*


root=Tk()

root.title(u'Секвенатор наглядно')
root.geometry('410x300+1000+200')
root.resizable( False, False)
root["bg"] = "white"


wd = Tk()
wd.geometry('300x580+500+200')
wd.resizable( False, False)
wd.title(u'Секвенатор наглядно')
wd["bg"] = "white"

#def ggwp(k):
  #a=0
  # if(k=='A'):
   #     a=1
  # elif(k=='T'):
  #      a=2
  # elif(k=='G'):
  #      a=3
  # elif(k=='C'):
  #      a=4
  # print(a)






variable = StringVar()
var0 = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

var01 = StringVar()
var11 = StringVar()
var21 = StringVar()
var31 = StringVar()

var02 = StringVar()
var12 = StringVar()
var22 = StringVar()
var32 = StringVar()

var03 = StringVar()
var13 = StringVar()
var23 = StringVar()
var33 = StringVar()

var04 = StringVar()
var14 = StringVar()
var24 = StringVar()
var34 = StringVar()

var05 = StringVar()
var15 = StringVar()
var25 = StringVar()
var35 = StringVar()

var06 = StringVar()
var16 = StringVar()
var26 = StringVar()
var36 = StringVar()

var07 = StringVar()
var17 = StringVar()
var27 = StringVar()
var37 = StringVar()

var08 = StringVar()
var18 = StringVar()
var28 = StringVar()
var38 = StringVar()

ch0 = Checkbutton(root, text="ADENINE", variable=var0,
                 onvalue="A - T", offvalue="    -     ", font='arial', fg='red',bg='white')
ch1 = Checkbutton(root, text="THYMINE", variable=var1,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch2 = Checkbutton(root, text="GUANINE", variable=var2,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch3 = Checkbutton(root, text="CYTOSINE", variable=var3,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch01 = Checkbutton(root, text="ADENINE", variable=var01,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch11 = Checkbutton(root, text="THYMINE", variable=var11,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch21 = Checkbutton(root, text="GUANINE", variable=var21,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch31 = Checkbutton(root, text="CYTOSINE", variable=var31,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch02 = Checkbutton(root, text="ADENINE", variable=var02,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch12 = Checkbutton(root, text="THYMINE", variable=var12,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch22 = Checkbutton(root, text="GUANINE", variable=var22,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch32 = Checkbutton(root, text="CYTOSINE", variable=var32,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch03 = Checkbutton(root, text="ADENINE", variable=var03,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch13 = Checkbutton(root, text="THYMINE", variable=var13,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch23 = Checkbutton(root, text="GUANINE", variable=var23,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch33 = Checkbutton(root, text="CYTOSINE", variable=var33,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch04 = Checkbutton(root, text="ADENINE", variable=var04,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch14 = Checkbutton(root, text="THYMINE", variable=var14,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch24 = Checkbutton(root, text="GUANINE", variable=var24,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch34 = Checkbutton(root, text="CYTOSINE", variable=var34,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch05 = Checkbutton(root, text="ADENINE", variable=var05,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch15 = Checkbutton(root, text="THYMINE", variable=var15,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch25 = Checkbutton(root, text="GUANINE", variable=var25,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch35 = Checkbutton(root, text="CYTOSINE", variable=var35,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch06 = Checkbutton(root, text="ADENINE", variable=var06,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch16 = Checkbutton(root, text="THYMINE", variable=var16,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch26 = Checkbutton(root, text="GUANINE", variable=var26,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch36 = Checkbutton(root, text="CYTOSINE", variable=var36,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch07 = Checkbutton(root, text="ADENINE", variable=var07,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch17 = Checkbutton(root, text="THYMINE", variable=var17,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch27 = Checkbutton(root, text="GUANINE", variable=var27,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch37 = Checkbutton(root, text="CYTOSINE", variable=var37,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')
ch08 = Checkbutton(root, text="ADENINE", variable=var08,
                 onvalue="A - T", offvalue="    -     ",font='arial',fg='red',bg='white')
ch18 = Checkbutton(root, text="THYMINE", variable=var18,
                 onvalue="T - A", offvalue="    -     ",font='arial',fg='blue',bg='white')
ch28 = Checkbutton(root, text="GUANINE", variable=var28,
                 onvalue="G - C", offvalue="    -     ",font='arial',fg='green',bg='white')
ch38 = Checkbutton(root, text="CYTOSINE", variable=var38,
                 onvalue="C - G", offvalue="    -     ",font='arial',fg='yellow',bg='white')


lis = Listbox(wd, height=36)

def results(event):
   v0 = var0.get()
   v1 = var1.get()
   v2 = var2.get()
   v3 = var3.get()
   v01 = var01.get()
   v11 = var11.get()
   v21 = var21.get()
   v31 = var31.get()
   v02 = var02.get()
   v12 = var12.get()
   v22 = var22.get()
   v32 = var32.get()
   v03 = var03.get()
   v13 = var13.get()
   v23 = var23.get()
   v33 = var33.get()
   v04 = var04.get()
   v14 = var14.get()
   v24 = var24.get()
   v34 = var34.get()
   v05 = var05.get()
   v15 = var15.get()
   v25 = var25.get()
   v35 = var35.get()
   v06 = var06.get()
   v16 = var16.get()
   v26 = var26.get()
   v36 = var36.get()
   v07 = var07.get()
   v17 = var17.get()
   v27 = var27.get()
   v37 = var37.get()
   v08 = var08.get()
   v18 = var18.get()
   v28 = var28.get()
   v38 = var38.get()
   l = [v0, v1, v2, v3,v01, v11, v21, v31, v02, v12, v22, v32, v03, v13, v23, v33, v04, v14, v24, v34, v05, v15, v25, v35, v06, v16, v26, v36, v07, v17, v27, v37, v08, v18, v28, v38]
   a=0
   l1=[]
   n=36
   for i in range(n):
        l1.append(0)
   if(v0=='A - T'):
        a=1
   elif(v0=='T - A'):
        a=2
   elif(v0=='G - C'):
        a=3
   elif(v0=='C - G'):
        a=4
   print(a)
   if(a!=0):
       l1.append(a)
   b=0
   if(v1=='A - T'):
        b=1
   elif(v1=='T - A'):
        b=2
   elif(v1=='G - C'):
        b=3
   elif(v1=='C - G'):
        b=4
   print(b)
   if(b!=0):
       l1.append(b)
   c=0
   if(v2=='A - T'):
        c=1
   elif(v2=='T - A'):
        c=2
   elif(v2=='G - C'):
        c=3
   elif(v2=='C - G'):
        c=4
   print(c)
   if(c!=0):
       l1.append(c)
   d=0
   if(v3=='A - T'):
        d=1
   elif(v3=='T - A'):
        d=2
   elif(v3=='G - C'):
        d=3
   elif(v3=='C - G'):
        d=4
   print(d)
   if(d!=0):
       l1.append(d)
   e=0
   if(v01=='A - T'):
        e=1
   elif(v01=='T - A'):
        e=2
   elif(v01=='G - C'):
        e=3
   elif(v01=='C - G'):
        e=4
   print(e)
   if(e!=0):
       l1.append(e)
   f=0
   if(v11=='A - T'):
        f=1
   elif(v11=='T - A'):
        f=2
   elif(v11=='G - C'):
        f=3
   elif(v11=='C - G'):
        f=4
   print(f)
   if(f!=0):
       l1.append(f)
   g=0
   if(v21=='A - T'):
        g=1
   elif(v21=='T - A'):
        g=2
   elif(v21=='G - C'):
        g=3
   elif(v21=='C - G'):
        g=4
   print(g)
   if(g!=0):
       l1.append(g)
   h=0
   if(v31=='A - T'):
        h=1
   elif(v31=='T - A'):
        h=2
   elif(v31=='G - C'):
        h=3
   elif(v31=='C - G'):
        h=4
   print(h)
   if(h!=0):
       l1.append(h)
   k=0
   if(v02=='A - T'):
        k=1
   elif(v02=='T - A'):
        k=2
   elif(v02=='G - C'):
        k=3
   elif(v02=='C - G'):
        k=4
   print(k)
   if(k!=0):
       l1.append(k)
   a1=0
   if(v12=='A - T'):
        a1=1
   elif(v12=='T - A'):
        a1=2
   elif(v12=='G - C'):
        a1=3
   elif(v12=='C - G'):
        a1=4
   print(a1)
   if(a1!=0):
       l1.append(a1)
   b1=0
   if(v22=='A - T'):
        b1=1
   elif(v22=='T - A'):
        b1=2
   elif(v22=='G - C'):
        b1=3
   elif(v22=='C - G'):
        b1=4
   print(b1)
   if(b1!=0):
       l1.append(b1)
   c1=0
   if(v32=='A - T'):
        c1=1
   elif(v32=='T - A'):
        c1=2
   elif(v32=='G - C'):
        c1=3
   elif(v32=='C - G'):
        c1=4
   print(c1)
   if(c1!=0):
       l1.append(c1)
   d1=0
   if(v03=='A - T'):
        d1=1
   elif(v03=='T - A'):
        d1=2
   elif(v03=='G - C'):
        d1=3
   elif(v03=='C - G'):
        d1=4
   print(d1)
   if(d1!=0):
       l1.append(d1)
   e1=0
   if(v13=='A - T'):
        e1=1
   elif(v13=='T - A'):
        e1=2
   elif(v13=='G - C'):
        e1=3
   elif(v13=='C - G'):
        e1=4
   print(e1)
   if(e1!=0):
       l1.append(e1)
   f1=0
   if(v23=='A - T'):
        f1=1
   elif(v23=='T - A'):
        f1=2
   elif(v23=='G - C'):
        f1=3
   elif(v23=='C - G'):
        f1=4
   print(f1)
   if(f1!=0):
       l1.append(f1)
   g1=0
   if(v33=='A - T'):
        g1=1
   elif(v33=='T - A'):
        g1=2
   elif(v33=='G - C'):
        g1=3
   elif(v33=='C - G'):
        g1=4
   print(g1)
   if(g1!=0):
       l1.append(g1)
   h1=0
   if(v04=='A - T'):
        h1=1
   elif(v04=='T - A'):
        h1=2
   elif(v04=='G - C'):
        h1=3
   elif(v04=='C - G'):
        h1=4
   print(h1)
   if(h1!=0):
       l1.append(h1)
   k1=0
   if(v14=='A - T'):
        k1=1
   elif(v14=='T - A'):
        k1=2
   elif(v14=='G - C'):
        k1=3
   elif(v14=='C - G'):
        k1=4
   print(k1)
   if(k1!=0):
       l1.append(k1)
   a2=0
   if(v24=='A - T'):
        a2=1
   elif(v24=='T - A'):
        a2=2
   elif(v24=='G - C'):
        a2=3
   elif(v24=='C - G'):
        a2=4
   print(a2)
   if(a2!=0):
       l1.append(a2)
   b2=0
   if(v34=='A - T'):
        b2=1
   elif(v34=='T - A'):
        b2=2
   elif(v34=='G - C'):
        b2=3
   elif(v34=='C - G'):
        b2=4
   print(b2)
   if(b2!=0):
       l1.append(b2)
   c2=0
   if(v05=='A - T'):
        c2=1
   elif(v05=='T - A'):
        c2=2
   elif(v05=='G - C'):
        c2=3
   elif(v05=='C - G'):
        c2=4
   print(c2)
   if(c2!=0):
       l1.append(c2)
   d2=0
   if(v15=='A - T'):
        d2=1
   elif(v15=='T - A'):
        d2=2
   elif(v15=='G - C'):
        d2=3
   elif(v15=='C - G'):
        d2=4
   print(d2)
   if(d2!=0):
       l1.append(d2)
   e2=0
   if(v25=='A - T'):
        e2=1
   elif(v25=='T - A'):
        e2=2
   elif(v25=='G - C'):
        e2=3
   elif(v25=='C - G'):
        e2=4
   print(e2)
   if(e2!=0):
       l1.append(e2)
   f2=0
   if(v35=='A - T'):
        f2=1
   elif(v35=='T - A'):
        f2=2
   elif(v35=='G - C'):
        f2=3
   elif(v35=='C - G'):
        f2=4
   print(f2)
   if(f2!=0):
       l1.append(f2)
   g2=0
   if(v06=='A - T'):
        g2=1
   elif(v06=='T - A'):
        g2=2
   elif(v06=='G - C'):
        g2=3
   elif(v06=='C - G'):
        g2=4
   print(g2)
   if(g2!=0):
       l1.append(g2)
   h2=0
   if(v16=='A - T'):
        h2=1
   elif(v16=='T - T'):
        h2=2
   elif(v16=='G - C'):
        h2=3
   elif(v16=='C - G'):
        h2=4
   print(h2)
   if(h2!=0):
       l1.append(h2)
   k2=0
   if(v26=='A - T'):
        k2=1
   elif(v26=='T - A'):
        k2=2
   elif(v26=='G - C'):
        k2=3
   elif(v26=='C - G'):
        k2=4
   print(k2)
   if(k2!=0):
       l1.append(k2)
   a3=0
   if(v36=='A - T'):
        a3=1
   elif(v36=='T - A'):
        a3=2
   elif(v36=='G - C'):
        a3=3
   elif(v36=='C - G'):
        a3=4
   print(a3)
   if(a3!=0):
       l1.append(a3)
   b3=0
   if(v07=='A - T'):
        b3=1
   elif(v07=='T - A'):
        b3=2
   elif(v07=='G - C'):
        b3=3
   elif(v07=='C - G'):
        b3=4
   print(b3)
   if(b3!=0):
       l1.append(b3)
   c3=0
   if(v17=='A - T'):
        c3=1
   elif(v17=='T - A'):
        c3=2
   elif(v17=='G - C'):
        c3=3
   elif(v17=='C - G'):
        c3=4
   print(c3)
   if(c3!=0):
       l1.append(c3)
   d3=0
   if(v27=='A - T'):
        d3=1
   elif(v27=='T - A'):
        d3=2
   elif(v27=='G - C'):
        d3=3
   elif(v27=='C - G'):
        d3=4
   print(d3)
   if(d3!=0):
       l1.append(d3)
   e3=0
   if(v37=='A - T'):
        e3=1
   elif(v37=='T - A'):
        e3=2
   elif(v37=='G - C'):
        e3=3
   elif(v37=='C - G'):
        e3=4
   print(e3)
   if(e3!=0):
       l1.append(e3)
   f3=0
   if(v08=='A - T'):
        f3=1
   elif(v08=='T - A'):
        f3=2
   elif(v08=='G - C'):
        f3=3
   elif(v08=='C - G'):
        f3=4
   print(f3)
   if(f3!=0):
       l1.append(f3)
   g3=0
   if(v18=='A - T'):
        g3=1
   elif(v18=='T - A'):
        g3=2
   elif(v18=='G - C'):
        g3=3
   elif(v18=='C - G'):
        g3=4
   print(g3)
   if(g3!=0):
       l1.append(g3)
   h3=0
   if(v28=='A - T'):
        h3=1
   elif(v28=='T - A'):
        h3=2
   elif(v28=='G - C'):
        h3=3
   elif(v28=='C - G'):
        h3=4
   print(h3)
   if(h3!=0):
       l1.append(h3)
   k3=0
   if(v38=='A - T'):
        k3=1
   elif(v38=='T - A'):
        k3=2
   elif(v38=='G - C'):
        k3=3
   elif(v38=='C - G'):
        k3=4
   print(k3)
   if(k!=0):
       l1.append(k3)
   lis.delete(0, 36)
   for v in l:
       lis.insert(END, v)
   y=[]
   for i in range(n):
       y.append(0)
   for i in range(n):
       y.append(l1[i])
   print(y)
   #l3 = []
   #n=9
   #print('Add a nucleotids, please')
   #for i in range(n):
   #    l.append(input())
      # print(l)
  #def trans(l):
     #   l2=[]
     #   for i in range(n):
         #   if l[i]== 'A':
           #     l2.append('T')
      #      if l[i]== 'T':
        #        l2.append('A')
          #  if l[i]== 'G':
         #       l2.append('C')
         #   if l[i]== 'C':
              #  l2.append('G')
     #   return l2
  # print(trans(l))

   IMAGE = plt.figure()
   ax = IMAGE.add_subplot(111, projection='3d')
   caption = plt.title(u'Секвенатор наглядно')

   a=0.05
   b=0.10
   z = np.linspace(-16, 20, 100)
   theta = np.linspace(0,50, 100)
   ##r = 1
   y = a*exp(b*theta)*cos(theta)                                                                                                                         ##- r * np.cos(theta) ## np.linspace(-1, 1, 100)##
   x = (a*exp(b*theta)*sin(theta))**1.5                                                                                                                     #- (1 - x**2)**0.5 + 1##x * np.sin(theta) ##
   THETA = np.linspace(50, 0, 100)
   Z = np.linspace(20, -16, 100)
##R = 1
   Y =  - (a*exp(b*THETA)*cos(THETA))**1.5                                                                                                                     ##np.linspace(1, -1, 100) ##
   X =  - a*exp(b*THETA)*sin(THETA)                                                                                                                    ##R X *  np.sin(theta) ##
   if (v0=='A - T'):
       z1 = np.linspace(-16, -12, 100)
       ax.scatter(x,y,z1,c='red',s=1)
       ax.text(0.75, 1, -16, "ADENINE", color='red')
       Z1 = np.linspace(-16, -12, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, -16, "THYMINE", color='blue')
       z14 = np.linspace(-16, -12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(-16, -12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v1=='T - A'):
       z1 = np.linspace(-16, -12, 100)
       ax.scatter(x,y,z1,c='blue',s=1)
       ax.text(0.75, 1, -16, "THYMINE", color='blue')
       Z1 = np.linspace(-16, -12, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, -16, "ADENINE", color='red')
       z14 = np.linspace(-16, -12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(-16, -12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v2=='G - C'):
       z1 = np.linspace(-16, -12, 100)
       ax.scatter(x,y,z1,c='green',s=1)
       ax.text(0.75, 1, -16, "GUANINE", color='green')
       Z1 = np.linspace(-16, -12, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, -16, "CYTOSINE", color='yellow')
       z14 = np.linspace(-16, -12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(-16, -12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v3=='C - G'):
       z1 = np.linspace(-16, -12, 100)
       ax.scatter(x,y,z1,c='yellow',s=1)
       ax.text(0.75, 1, -16, "CYTOSINE", color='yellow')
       Z1 = np.linspace(-16, -12, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, -16,  "GUANINE", color='green')
       z14 = np.linspace(-16, -12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(-16, -12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v01=='A - T'):
       z1 = np.linspace(-12, -8, 100)
       ax.scatter(x,y,z1,c='red',s=1)
       ax.text(0.75, 1, -12, "ADENINE", color='red')
       Z1 = np.linspace(-12, -8, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, -12,  "THYMINE", color='blue')
       z14 = np.linspace(-12, -8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(-12, -8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v11=='T - A'):
       z2 = np.linspace(-12, -8, 100)
       ax.scatter(x,y,z2,c='blue',s=1)
       ax.text(0.75, 1, -12, "THYMINE", color='blue')
       Z1 = np.linspace(-12, -8, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, -12, "ADENINE", color='red')
       z14 = np.linspace(-12, -8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(-12, -8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v21=='G - C'):
       z2 = np.linspace(-12, -8, 100)
       ax.scatter(x,y,z2,c='green',s=1)
       ax.text(0.75, 1, -12, "GUANINE", color='green')
       Z1 = np.linspace(-12, -8, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, -12, "CYTOSINE", color='yellow')
       z14 = np.linspace(-12, -8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(-12, -8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v31=='C - G'):
       z2 = np.linspace(-12, -8, 100)
       ax.scatter(x,y,z2,c='yellow',s=1)
       ax.text(0.75, 1, -12, "CYTOSINE", color='yellow')
       Z1 = np.linspace(-12, -8, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, -12, "GUANINE", color='green')
       z14 = np.linspace(-12, -8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(-12, -8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v02=='A - T'):
       z2 = np.linspace(-8, -4, 100)
       ax.scatter(x,y,z2,c='red',s=1)
       ax.text(0.75, 1, -8, "ADENINE", color='red')
       Z1 = np.linspace(-8, -4, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, -8, "THYMINE", color='blue')
       z14 = np.linspace(-8, -4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(-8, -4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v12=='T - A'):
       z3 = np.linspace(-8, -4, 100)
       ax.scatter(x,y,z3,c='blue',s=1)
       ax.text(0.75, 1, -8, "THYMINE", color='blue')
       Z1 = np.linspace(-8, -4, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, -8, "ADENINE", color='red')
       z14 = np.linspace(-8, -4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(-8, -4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v22=='G - C'):
       z3 = np.linspace(-8, -4, 100)
       ax.scatter(x,y,z3,c='green',s=1)
       ax.text(0.75, 1, -8, "GUANINE", color='green')
       Z1 = np.linspace(-8, -4, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, -8, "CYTOSINE", color='yellow')
       z14 = np.linspace(-8, -4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(-8, -4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v32=='C - G'):
       z3 = np.linspace(-8, -4, 100)
       ax.scatter(x,y,z3,c='yellow',s=1)
       ax.text(0.75, 1, -8, "CYTOSINE", color='yellow')
       Z1 = np.linspace(-8, -4, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, -8, "GUANINE", color='green')
       z14 = np.linspace(-8, -4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(-8, -4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v03=='A - T'):
       z3 = np.linspace(-4, 0, 100)
       ax.scatter(x,y,z3,c='red',s=1)
       ax.text(0.75, 1, -4, "ADENINE", color='red')
       Z1 = np.linspace(-4, 0, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, -4, "THYMINE", color='blue')
       z14 = np.linspace(-4, 0, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(-4, 0, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v13=='T - A'):
       z4 = np.linspace(-4, 0, 100)
       ax.scatter(x,y,z4,c='blue',s=1)
       ax.text(0.75, 1, -4, "THYMANE", color='blue')
       Z1 = np.linspace(-4, 0, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, -4, "ADENINE", color='red')
       z14 = np.linspace(-4, 0, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(-4, 0, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v23=='G - C'):
       z4 = np.linspace(-4, 0, 100)
       ax.scatter(x,y,z4,c='green',s=1)
       ax.text(0.75, 1, -4, "GUANINE", color='green')
       Z1 = np.linspace(-4, 0, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, -4, "CYTOSINE", color='yellow')
       z14 = np.linspace(-4, 0, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(-4, 0, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v33=='C - G'):
       z4 = np.linspace(-4, 0, 100)
       ax.scatter(x,y,z4,c='yellow',s=1)
       ax.text(0.75, 1, -4, "CYTOSINE", color='yellow')
       Z1 = np.linspace(-4, 0, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, -4, "GUANINE", color='green')
       z14 = np.linspace(-4, 0, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(-4, 0, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v04=='A - T'):
       z4 = np.linspace(0, 4, 100)
       ax.scatter(x,y,z4,c='red',s=1)
       ax.text(0.75, 1, 0, "ADENINE", color='red')
       Z1 = np.linspace(0, 4, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, 0, "THYMINE", color='blue')
       z14 = np.linspace(0, 4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(0, 4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v14=='T - A'):
       z5 = np.linspace(0, 4, 100)
       ax.scatter(x,y,z5,c='blue',s=1)
       ax.text(0.75, 1, 0, "THYMINE", color='blue')
       Z1 = np.linspace(0, 4, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, 0, "ADENINE", color='red')
       z14 = np.linspace(0, 4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(0, 4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v24=='G - C'):
       z5 = np.linspace(0, 4, 100)
       ax.scatter(x,y,z5,c='green',s=1)
       ax.text(0.75, 1, 0, "GUANINE", color='green')
       Z1 = np.linspace(0, 4, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, 0, "CYTOSINE", color='yellow')
       z14 = np.linspace(0, 4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(0, 4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v34=='C - G'):
       z5 = np.linspace(0, 4, 100)
       ax.scatter(x,y,z5,c='yellow',s=1)
       ax.text(0.75, 1, 0, "CYTOSINE", color='yellow')
       Z1 = np.linspace(0, 4, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, 0, "GUANINE", color='green')
       z14 = np.linspace(0, 4, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(0, 4, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v05=='A - T'):
       z5 = np.linspace(4, 8, 100)
       ax.scatter(x,y,z5,c='red',s=1)
       ax.text(0.75, 1, 4, "ADENINE", color='red')
       Z1 = np.linspace(4, 8, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, 4, "THYMINE", color='blue')
       z14 = np.linspace(4, 8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(4, 8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v15=='T - A'):
       z6 = np.linspace(4, 8, 100)
       ax.scatter(x,y,z6,c='blue',s=1)
       ax.text(0.75, 1, 4, "THYMINE", color='blue')
       Z1 = np.linspace(4, 8, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, 4, "ADENINE", color='red')
       z14 = np.linspace(4, 8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(4, 8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v25=='G - C'):
       z6 = np.linspace(4, 8, 100)
       ax.scatter(x,y,z6,c='green',s=1)
       ax.text(0.75, 1, 4, "GUANINE", color='green')
       Z1 = np.linspace(4, 8, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, 4, "CYTOSINE", color='yellow')
       z14 = np.linspace(4, 8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(4, 8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v35=='C - G'):
       z6 = np.linspace(4, 8, 100)
       ax.scatter(x,y,z6,c='yellow',s=1)
       ax.text(0.75, 1, 4, "CYTOSINE", color='yellow')
       Z1 = np.linspace(4, 8, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, 4, "GUANINE", color='green')
       z14 = np.linspace(4, 8, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(4, 8, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v06=='A - T'):
       z6 = np.linspace(8, 12,100)
       ax.scatter(x,y,z6,c='red',s=1)
       ax.text(0.75, 1, 8, "ADENINE", color='red')
       Z1 = np.linspace(8, 12, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, 8, "THYMINE", color='blue')
       z14 = np.linspace(8, 12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(8, 12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v16=='T - A'):
       z7 = np.linspace(8, 12, 100)
       ax.scatter(x,y,z7,c='blue',s=1)
       ax.text(0.75, 1, 8, "THYMINE", color='blue')
       Z1 = np.linspace(8, 12, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, 8, "ADENINE", color='red')
       z14 = np.linspace(8,12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(8, 12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v26=='G - C'):
       z7 = np.linspace(8, 12, 100)
       ax.scatter(x,y,z7,c='green',s=1)
       ax.text(0.75, 1, 8, "GUANINE", color='green')
       Z1 = np.linspace(8, 12, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, 8, "CYTOSINE", color='yellow')
       z14 = np.linspace(8,12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(8, 12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v36=='C - G'):
       z7 = np.linspace(8, 12, 100)
       ax.scatter(x,y,z7,c='yellow',s=1)
       ax.text(0.75, 1, 8, "CYTOSINE", color='yellow')
       Z1 = np.linspace(8, 12, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, 8, "GUANINE", color='green')
       z14 = np.linspace(8,12, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(8, 12, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v07=='A - T'):
       z7 = np.linspace(12, 16, 100)
       ax.scatter(x,y,z7,c='red',s=1)
       ax.text(0.75, 1, 12, "ADENINE", color='red')
       Z1 = np.linspace(12, 16, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, 12, "THYMINE", color='blue')
       z14 = np.linspace(12,16, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(12, 16, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v17=='T - A'):
       z8 = np.linspace(12, 16, 100)
       ax.scatter(x,y,z8,c='blue',s=1)
       ax.text(0.75, 1, 12, "THYMINE", color='blue')
       Z1 = np.linspace(12, 16, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, 12, "ADENINE", color='red')
       z14 = np.linspace(12,16, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(12, 16, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v27=='G - C'):
       z8 = np.linspace(12, 16, 100)
       ax.scatter(x,y,z8,c='green',s=1)
       ax.text(0.75, 1, 12, "GUANINE", color='green')
       Z1 = np.linspace(12, 16, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, 12, "CYTOSINE", color='yellow')
       z14 = np.linspace(12,16, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(12, 16, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v37=='C - G'):
       z8 = np.linspace(12, 16, 100)
       ax.scatter(x,y,z8,c='yellow',s=1)
       ax.text(0.75, 1, 12, "CYTOSINE", color='yellow')
       Z1 = np.linspace(12, 16, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, 12, "GUANINE", color='green')
       z14 = np.linspace(12,16, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(12, 16, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)
   if (v08=='A - T'):
       z8 = np.linspace(16, 20, 100)
       ax.scatter(x,y,z8,c='red',s=1)
       ax.text(0.75, 1, 16, "ADENINE", color='red')
       Z1 = np.linspace(16, 16, 100)
       ax.scatter(X,Y,Z1,c='blue',s=1)
       ax.text(-5, -5, 16, "THYMINE", color='blue')
       z14 = np.linspace(16,20, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='red',s=1)
       z122 = np.linspace(16, 20, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='blue',s=1)
   if (v18=='T - A'):
       z8 = np.linspace(16, 20, 100)
       ax.scatter(x,y,z8,c='blue',s=1)
       ax.text(0.75, 1, 16, "THYMINE", color='blue')
       Z1 = np.linspace(16, 20, 100)
       ax.scatter(X,Y,Z1,c='red',s=1)
       ax.text(-5, -5, 16, "ADENINE", color='red')
       z14 = np.linspace(16,20, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='blue',s=1)
       z122 = np.linspace(16, 20, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='red',s=1)
   if (v28=='G - C'):
       z8 = np.linspace(16, 20, 100)
       ax.scatter(x,y,z8,c='green',s=1)
       ax.text(0.75, 1, 16, "GUANINE", color='green')
       Z1 = np.linspace(16, 20, 100)
       ax.scatter(X,Y,Z1,c='yellow',s=1)
       ax.text(-5, -5, 16, "CYTOSINE", color='yellow')
       z14 = np.linspace(16,20, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='green',s=1)
       z122 = np.linspace(16, 20, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='yellow',s=1)
   if (v38=='C - G'):
       z8 = np.linspace(16, 20, 100)
       ax.scatter(x,y,z8,c='yellow',s=1)
       ax.text(0.75, 1, 16, "CYTOSINE", color='yellow')
       Z1 = np.linspace(16, 20, 100)
       ax.scatter(X,Y,Z1,c='green',s=1)
       ax.text(-5, -5, 16, "GUANINE", color='green')
       z14 = np.linspace(16,20, 100)
       x14=cos(z14)/4
       y14=sin(z14)/4
       ax.scatter(x14,y14,z14,c='yellow',s=1)
       z122 = np.linspace(16, 20, 100)
       x122=-cos(z122)/4
       y122=-sin(z122)/4
       ax.scatter(x122,y122,z122,c='green',s=1)


   plt.show()









ch0.deselect()
ch1.deselect()
ch2.deselect()
ch3.deselect()
ch01.deselect()
ch11.deselect()
ch21.deselect()
ch31.deselect()
ch02.deselect()
ch12.deselect()
ch22.deselect()
ch32.deselect()
ch03.deselect()
ch13.deselect()
ch23.deselect()
ch33.deselect()
ch04.deselect()
ch14.deselect()
ch24.deselect()
ch34.deselect()
ch05.deselect()
ch15.deselect()
ch25.deselect()
ch35.deselect()
ch06.deselect()
ch16.deselect()
ch26.deselect()
ch36.deselect()
ch07.deselect()
ch17.deselect()
ch27.deselect()
ch37.deselect()
ch08.deselect()
ch18.deselect()
ch28.deselect()
ch38.deselect()

ch0.grid(row=0, column=0)
ch1.grid(row=0, column=1)
ch2.grid(row=0, column=2)
ch3.grid(row=0, column=3)
ch01.grid(row=1, column=0)
ch11.grid(row=1, column=1)
ch21.grid(row=1, column=2)
ch31.grid(row=1, column=3)
ch02.grid(row=2, column=0)
ch12.grid(row=2, column=1)
ch22.grid(row=2, column=2)
ch32.grid(row=2, column=3)
ch03.grid(row=3, column=0)
ch13.grid(row=3, column=1)
ch23.grid(row=3, column=2)
ch33.grid(row=3, column=3)
ch04.grid(row=4, column=0)
ch14.grid(row=4, column=1)
ch24.grid(row=4, column=2)
ch34.grid(row=4, column=3)
ch05.grid(row=5, column=0)
ch15.grid(row=5, column=1)
ch25.grid(row=5, column=2)
ch35.grid(row=5, column=3)
ch06.grid(row=6, column=0)
ch16.grid(row=6, column=1)
ch26.grid(row=6, column=2)
ch36.grid(row=6, column=3)
ch07.grid(row=7, column=0)
ch17.grid(row=7, column=1)
ch27.grid(row=7, column=2)
ch37.grid(row=7, column=3)
ch08.grid(row=8, column=0)
ch18.grid(row=8, column=1)
ch28.grid(row=8, column=2)
ch38.grid(row=8, column=3)




but = Button(wd, text="Получить значения:",font='arial',bg='white', fg='orange')
but.bind('<Button-1>', results)


but.grid(row=9, rowspan=2, column=0)
lis.grid(row=10, rowspan=2, column=1)






mainloop()
