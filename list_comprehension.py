#Task 4.1

A = int(input())
B = int(input())

list_AB = range(A, B)

list_new = [num for num in list_AB ]
print(list_new, 'количество цифр от A до В:', len(list_new))