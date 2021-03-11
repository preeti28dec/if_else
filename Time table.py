time=int(input("enter your time "))
x=str(input("enter the am or pm "))
if time>=6 and time<=7:
    if x=="am":
        print("excise")
elif time>=8 and time<=12:
    if x=="am":
        print("first half ka coding time ")
elif time >=1 and time<=2:
    if x=="pm":
        print("lunch")
elif time>=2 and time<=5:
    if x=="pm":
        print("seconf half ka coding time ")
elif time>=5 and time<=6:
    if x=="pm":
        print("milk break")
elif time>=6 and time<=7:
    if x=="pm":
        print("english ectivity time ")
elif time>=7 and time<=8:
    if x=="pm":
        print("reciretion ectivity time ")
else:
    print("what ever you want to do ")