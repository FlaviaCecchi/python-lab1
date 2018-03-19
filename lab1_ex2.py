str = input("Insert a string ")

if len(str) < 3:
    print("The string is not valid")
else:
    newstr = str[0] + str[1] + str[len(str)-2] + str[len(str)-1]
    print(newstr)