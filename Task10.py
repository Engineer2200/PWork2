n = int(input("Введите количество монет: "))
count1 = 0
count2 = 0
for i in range(n):
    coin = int(input())
    if coin == 1:
        count1 += 1
    else:
        count2 += 1
if count2 < count1:
    print(f'Результат {count2}')
else:
    print(f'Результат {count1}')
