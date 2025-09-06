while True:
    keyline = input().split()
    if keyline == ["0"]:
        break
    n = int(keyline[0])
    keylist = keyline[1:]
    message = input()

    remainder = len(message) % n
    if remainder != 0:
        message += " " * (n -remainder)
    
    i = 0
    encrypted = ""
    while i < len(message):
        submessage = message[i:i+n]
        for j in range(n):
            newchar = submessage[int(keylist[j])-1]
            encrypted += newchar
        i+=n
    print("\'" + encrypted + "\'")



