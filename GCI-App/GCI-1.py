from mypackage import length,time
print("Enter : ")
print("FOR LENGTH CONVERSION : 1")
print("FOR TIME CONVERSION : 2")
inp=int(input("Enter your choice : "))
if inp==1:
    length.length_conversion()
elif inp==2:
    time.time_conversion()
else:
    print("Sorry")
