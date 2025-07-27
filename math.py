import math


#1. abs() return the absolute value
# eg
# print(abs(-98))

# a real implatation


print("we have to find the root for a quadratic equation")
print("ax^2+bx+c")
print("give input with sign eg;+6,-8")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
print("the eqation as per your choice is",a,"x^2",b,"x",c)
D=b**2-4*a*c
if(D>0):
    print("THIS EQ HAVE 2 REAL AND DISTINCT ROOTS")
    r1=(-b+math.sqrt(D))/(2*a)
    r2=(-b-math.sqrt(D))/(2*a)
    print("THE ROOTS FOR THIS EQ IS EQUAL TO",r1,",",r2)
elif(D==0):
    print("THIS EQ HAVE 1 REAL ROOT")
    r=-b/(2*a)
    print("THE ROOTS FOR THIS EQ IS EQUAL TO",r)
elif(D<0):
    print("THIS EQ HAVR 2 DISTINCT IMAGINARY ROOTS")
    real_pt=-b/(2*a)
    img_pt=math.sqrt(abs(D))/(2*a)
    img1=real_pt+img_pt
    img2=real_pt-img_pt
    print("THE ROOTS FOR THIS EQ IS EQUAL TO ",img1,"i"," and ",img2,"i")
else:
    print("INVALID")




# 2.ceil()---->the great or equal integre of the input
# eg
# print(math.ceil(9.7864))

# a real implantation

print("THIS IS A BILLING MANAGEMET")
item1=str(input("ENTER THE NAME OF THE ITEM = "))
item2=str(input("ENTER THE NAME OF THE ITEM = "))
item3=str(input("ENTER THE NAME OF THE ITEM = "))
cost1=float(input("cost per qty = "))
cost2=float(input("cost per qty = "))
cost3=float(input("cost per qty = "))
qty1=int(input("qty = "))
qty2=int(input("qty = "))
qty3=int(input("qty = "))
net1=qty1*cost1
net2=qty2*cost2
net3=qty3*cost3
total=net1+net2+net3
print("total = ",total)
print("to pay = ",math.ceil(total))


# # 3.copysign(x,y)
# # print(math.copysign(-9.57,0.56))

# # changing direction of velocty
print("this is a python program to chnge the direction of velocity")
x=float(input("enter the magnitude of velocity in x direction = "))
y=float(input("enter the magnitude of velocity in y direction = "))
z=float(input("enter the magnitude of velocity in z direction = "))
dir_X=int(input("enter -1 for -X and +1 for +X = "))
dir_Y=int(input("enter -1 for -Y and +1 for +Y = "))
dir_Z=int(input("enter -1 for -Z and +1 for +Z = "))


print("old velocity",x,"i+",y,"j+",z,"k")   
print("new velocity",math.copysign(x,dir_X),"i+",math.copysign(y,dir_Y),"j+",math.copysign(z,dir_Z),"k") 


# 4.fabs(x)
# print(math.fabs(-19.54))

# a real implantation 

print("THIS IS A DISTANCE EVALUATER")
x=float(input("ENETR THE X AXIS DISTANCE WITH SIGN = "))
y=float(input("ENETR THE Y AXIS DISTANCE WITH SIGN = "))
z=float(input("ENETR THE Z AXIS DISTANCE WIH SIGN = "))

print("DISTANCE IN X = ",math.fabs(x))
print("DISTANCE IN Y = ",math.fabs(y))
print("DISTANCE IN Z = ",math.fabs(z))

print("THE DISPLACMENT = ",x,"i",y,"j",z,"k")
print("THE DISTANCE  = ",math.sqrt(x**2+y**2+z**2))

# 5.factorial
# print(math.factorial(5))

#  a real implantation

print("THIS IS A PERMUTATION AND COMBINATION CALCULATOR")
print("SECELT FROM THE FOLLOWING-\n1.nCr,\n2.nPr")
option=int(input("enetr the prefrence = "))
if(option==1):
    print("YOU CHOOSE TO CALCULATE nCr")
    n=int(input("enter the value of n = "))
    r=int(input("enter the value of r = "))
    if((n>0)and(r>=0)and(0<=r<=n)):
        nCr=math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
        print("nCr = ",n,"C",r," = ",nCr)
    else:
        print("invalid command")
elif(option==2):
    print("YOU CHOOSE TO CALCULATE nPr")
    n=int(input("enter the value of n = "))
    r=int(input("enter the value of r = "))
    if((n>0)and(r>=0)and(0<=r<=n)):
        nPr=math.factorial(n)/(math.factorial(n-r))
        print("nPr = ",n,"P",r," = ",nPr)
    else:
        print("invalid command")
else:
    print("INVALID COMMAND")


# 6. floor x
# print(math.floor(5.6))

# a real life implantiation
print("THIS IS A  PACKING THE BOX PROGRAM")
print("IN THIS YOU HAVR TO ENTER NO OF BOX AND THE NUMBER OFD ITEM IN IT AND THIS PROGRAM WILL CALCULATE THE MINIMUM NO OF ITEM PER BOX FOR A PUTTING SOME OF THE ITEM IN EVERY BOX")
itemqty=float(input("enter the ammount of qty for the box"))
boxes=int(input("ENTER THE NUMBER OF BOXES"))
if((itemqty<=0)):
    print("INVALID QTY")
elif(boxes<=0):
    print("INVALID BOX")
else:    
    item_per_box=float(itemqty/boxes)
    print("THE MINIMUM QTY OF TEM PER BOX IS EQUAL TO = ",math.floor(item_per_box))


# 7.fmod(x,y)
# print(math.fmod(52,9))

# a real implantation

print("THIS IS A ANGLE CALCULATER ON THE BASISI OF 360 DEGREE AND THE CONCEPT OF NEGATIVE ANGLES ")
ANGLE=float(input("ENTER THE ANGLE WITH DIRECTION = "))
NORMALIZE=math.fmod(ANGLE,360)
print("THE NORMALISE ANGLE WILL BE = ",NORMALIZE)


# 8.frexp(x)--->metincaa and exponent retrun karta hai yemeans(x=m*2^e)--->return (m,e)
# print(math.frexp(33))
# if user want only 2^e wala e so we have to do this at the end os the fn math.frexp(33)[1] and if want m then replce 0 with 1 
#  because it return teh tuple

# a real implantation

print("this is a unit suggester")
print("in this py program a user gives the input for the files data in bytes")
data=float(input("ENTER THE DATA IN BYTES = "))
e=math.frexp(data)[1]
if(e<10):
    unit="Bytes"
elif(e<20):
    unit="KB"
elif(e<30):
    unit="MB"
elif(e<40):
    unit="GB"
else:
    unit="TB"
print("SUGGESTED UNIT = ",unit)


# 9.fsum(x)
# data=[1.234,5.8141,2.7842]
# print(math.fsum(data))

# a real implantation

print("this is the accurate accurate calclator")
n=int(input("enter the number of transiction = "))
transactions=[]
for i in range(n):
    value=float(input("enter the value of product = "))
    transactions.append(value)
total=math.fsum(transactions)
print("total = ",total)

# 10. gcd or hcf
# this is what here in py math library ands this is how we use that
# math.gcd(9,15)
# and for the more then 2 numbers 
# math.gcd(math.gcd(x,y),z)

# x,y,z=1,5,9
# print(math.gcd(math.gcd(x,y),z))

# a real implantation

print("this is a length calculate ")
print("""this is how it work
we have 3 ropes and we want to cut them in equal length and with a cindition of that saying
the length no of pecies and the cut peciee all must be integer""")
rope_a=int(input("ENETR THE LENGTH OF ROPE A(in m)"))
rope_b=int(input("ENETR THE LENGTH OF ROPE B(in m)"))
rope_c=int(input("ENETR THE LENGTH OF ROPE C(in m)"))
cut_in=math.gcd(math.gcd(rope_a,rope_b),rope_c)
print("the equal length that the cut pices of rop have = ",cut_in,"m")

# 11.isclose(x,y)
# it cheak tha  wheather a and y are approximatliy equal or not
# print(math.isclose(2,1.9999,rel_tol=1e-2))
# a real implantation

print("this is a distance approximater")
real_lat = 28.6139
user_lat = 28.61389999
if math.isclose(real_lat, user_lat, rel_tol=1e-6):
    print("correct location.")
else:
    print("not at the right location.")


# 12.isfinite(x)---->cheak that is a number if valid or not 
# means it cheak that if a number if nan or infinite or not

# print(math.isfinite(120))

# a real implantation

print("this is a program to cheak that is the reading for a thermameter is valid or not")
n=int(input("enter the number of reading = "))
valid_reading=[]
for i in range(n):
    try:
        val=float(input(f"enter reading {i+1}:"))
        if math.isfinite(val):
            valid_reading.append(val)
        else:
            print("enter the valid reading")
    except ValueError:
        print("invalid")
if valid_reading:
    print("the average temp is= ",sum(valid_reading)/len(valid_reading))
else:
    print("ENTER THE VALID VALUES")


# 13.isinf(x)----->> cheak if a number if infinte or not
# print(math.isinf(float('-inf')))

# a real importance


print("this is a physics voltage detacter")

reading = float(input("Enter voltage reading: "))
if math.isinf(reading):
    print(" Invalid reading: infinite value detected!")
else:
    print(" Valid reading:", reading)



# 14.isnan(x)--->>cheak if a number is valid or not a number (nan)
# print(math.isnan(float('nan')))

print("this is a physics voltage detacter")

reading = float(input("Enter voltage reading: "))
if math.isnan(reading):
    print("Invalid reading: nan value detected!")
else:
    print("Valid reading:", reading)





# 15.ldexp(m,e)----->> reverse of frexp-->>
# like how we do this enter x and get m and e in this the reverse is happening we enter the 
# value of m and e and te result give us the value of x

# print(math.ldexp(2,2))

# a real impplantation

print("this is a exponent discount calcuatre")
print("this is the dicount meter for special discount whcih increase exponential ")
total_bill=float(input("enter the total bill : "))
m=total_bill
e=int(input("enter the value of power for payment after dicsount = "))
net=math.ldexp(m,-e)
print("total to pay",net)