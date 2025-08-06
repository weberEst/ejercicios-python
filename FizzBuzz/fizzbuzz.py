




for x in range(1,101):
    if x % 3 == 0 and  x % 5 == 0:
        x = "fizzbuzz" 
        print(x)
    elif x % 3 == 0:
        x = "fizz"
        print(x)
    elif x % 5 == 0:
        x = "buzz"
        print(x)
    else:
        print (x)