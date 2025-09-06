#timebomb

d0 = ["***", "* *", "* *", "* *", "***"]
d1 = ["  *"]* 5
d2 = ["***", "  *", "***", "*  ", "***"]
d3 = ["***", "  *", "***", "  *", "***"]
d4 = ["* *", "* *", "***", "  *", "  *"]
d5 = ["***", "*  ", "***", "  *", "***"]
d6 = ["***", "*  ", "***", "* *", "***"]
d7 = ["***", "  *","  *","  *","  *"]
d8 = ["***","* *","***","* *", "***"]
d9 = ["***","* *","***","  *", "***"]

lines = []
for i in range(5):
    lines.append(input())


N = len(lines[0])
i = 0
bad = 0
number_string = ""
while (i < N):
    digit = []
    for line in lines:
        digit.append(line[i:i+3])
    if digit == d0:
        number_string = number_string + "0"
    elif digit == d1:
        number_string = number_string + "1"
    elif digit == d2:
        number_string = number_string + "2"
    elif digit == d3:
        number_string = number_string + "3"
    elif digit == d4:
        number_string = number_string + "4"
    elif digit == d5:
        number_string = number_string + "5"    
    elif digit == d6:
        number_string = number_string + "6"    
    elif digit == d7:
        number_string = number_string + "7"    
    elif digit == d8:
        number_string = number_string + "8"    
    elif digit == d9:
        number_string = number_string + "9"    
    else: 
        bad = 1
    i = i+4

if bad == 1:
    print("BOOM!!")
else:
    if (int(number_string) % 6 == 0):
        print("BEER!!")
    else:
        print("BOOM!!")


    

        
    

        


