N = int(input())
busses = input().split()
busses = [int(bus) for bus in busses]
busses = sorted(busses)
i = 0
prev = -1
count = 1
mystring = ""


while i < N:
    bus = busses[i]
    j = 1
    count = 1
    while True and (j + i < N):
        nextbus = busses[i+j]
        if nextbus == bus + j:
            count +=1
            j +=1
        else:
            break
    if count == 1:
        mystring+=str(bus) + " "
    elif count == 2:
        mystring+=str(busses[i]) + " " + str( busses[i+1]) + " "
    else:
        mystring+=(str(busses[i]) + "-" + str(busses[i+j-1]) + " ") 
    i += count
        


print(mystring)