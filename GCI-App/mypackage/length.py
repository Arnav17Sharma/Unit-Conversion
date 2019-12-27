def length_conversion():
    '''
    **********CONVERSION TABLE**********
    1 centimeter = 10 milimeter
    1 meter = 100 centimeter
    1 kilometer = 1000 meter
    1 inch = 2.54 centimeter
    1 feet = 30.48 centimeter
    1 yard = 91.44 centimeter
    1 mile = 160934.4 centimeter
    1 nautical mile = 185200 centimeter
    '''
    print("**********LENGTH CONVERSION TABLE**********")
    a=input("Enter : ")
    l=list(a.split(" "))
    if 'to' in l:
        del l[l.index('to')]
    else:
        print("Invalid Input")
    d={
    'milimeter':1,
    'centimeter':10,
    'meter':1000,
    'kilometer':1000000,
    'inch':25.4,
    'feet':304.8,
    'yard':914.4,
    'mile':1609344,
    }
    print(int(l[0])*(d[l[1]]/d[l[2]]),l[2])

