s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
x = 1
y = 1
while x != 1001:
    x += 1
    while y != 1001:
        y +=1
        if (x + y == s) and (x * y == p):
            print (x , y)