Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Q.1 welcome message
>>> print("welcome to python programing")
welcome to python programing
>>> #Q.2 address with escape characters
>>> print("rajesh kumar\nflat no.101,\tsunshine apartments\nMG road, sector 15\trajkot\tpincode : 360004\tindia.")
rajesh kumar
flat no.101,	sunshine apartments
MG road, sector 15	rajkot	pincode : 360004	india.
>>> a=150
>>> b=120.50
>>> print("addition=",a+b)
addition= 270.5
>>> print("subtraction=",a-b)
subtraction= 29.5
>>> print("multiplication=",a*b)
multiplication= 18075.0
>>> print("division=",a/b)
division= 1.2448132780082988
>>> #Q.4 calculate area and circumference of a circle
>>> radius=float(input("enter radius:"))
enter radius:12
>>> area=3.14*radius*radius
>>> circumference=2*3.14*radius
>>> print("area of circle=",area)
area of circle= 452.15999999999997
>>> print("circumference of circle=",circumference)
circumference of circle= 75.36
>>> #Q.5 calculate simple interest
>>> p=float(input("enter principal amount:"))
enter principal amount:12
>>> r=float(input("enter rate of interest:"))
enter rate of interest:10
>>> t=float(input("enter time (in year):"))
enter time (in year):15
>>> si=(p*r*t)/ 100
>>> print("simple interest=",si)
simple interest= 18.0
>>> #Q.6 calculate perimeter pf a rectangle
>>> length=float(input("enter length:"))
enter length:54
>>> width=float(input("enter width:"))
enter width:12
>>> perimeter=2*(length+width)
>>> print("perimeter of ractangle=",perimeter)
perimeter of ractangle= 132.0
>>> #Q.7 calculate area and perimeter of a rectangle
>>> length= float(input("enter length:"))
enter length:17
>>> width=float(input("enter width:"))
enter width:34
>>> area=length*width
>>> perimeter=2*(length+width)
>>> print("area of rectangle=",area)
area of rectangle= 578.0
>>> print("perimeter of rectangle=",perimeter)
perimeter of rectangle= 102.0
>>> #Q.8 calculate perimeter of a triangle
>>> a=float(input("enter side a:"))
enter side a:13
>>> b=float(input("enter side b:"))
enter side b:25
>>> c=float(input("enter side c:"))
enter side c:24
>>> perimeter=a+b+c
>>> print("perimeter of triangle=",perimeter)
perimeter of triangle= 62.0
>>> #Q.9 calculate area and perimeter of square
>>> side=float(input("enter side of square:"))
enter side of square:24
>>> area=side*side
>>> perimeter=4*side
>>> print("area of square=",area)
area of square= 576.0
>>> print("perimeter of square=",perimeter)
perimeter of square= 96.0
>>> #Q.10 calculate perimeter of square
>>> side=float(input("enter side of square:"))
enter side of square:45
>>> perimeter=4*side
>>> print("perimeter of square=",perimeter)
perimeter of square= 180.0
>>> 