import random
num = [random.randint(-50, 50) for i in range(25)]
count_positive = 0
count_negative  = 0
count_zero = 0
print(num)
for i in num:
    if i > 0:
        count_positive += 1
    elif i == 0:
       count_zero += 1
    else:
        count_negative += 1
print(f"Положительных чисел {count_positive}, их процент от общего количества равен {count_positive/25 *100}%" )
print(f"Положительных чисел {count_negative}, их процент от общего количества равен {count_negative/25 *100}%" )
print(f"Положительных чисел {count_zero}, их процент от общего количества равен {count_zero/25 *100}%" )
print(f"Максимальное значение: {max(num)}")
print(f"Минимальное значение: {min(num)}")