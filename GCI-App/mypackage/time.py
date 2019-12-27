def time_conversion():
    '''
    **********TIME CONVERSION TABLE**********
    second = 1
    minute = 60
    hour = 60*60
    day = 24*60*60
    week = 7*24*60*60
    year = 365*24*60*60
    '''
    print("**********TIME CONVERSION TABLE**********")
    a=input("Enter : ")
    l=list(a.split(" "))
    if 'to' in l:
        del l[l.index('to')]
    else:
        print("Invalid Input")
    d={'second':1,"minute":60,"hour":60*60,"day":24*60*60,"week":7*24*60*60,"year":365*24*60*60}
    print(int(l[0])*(d[l[1]]/d[l[2]]),l[2])
