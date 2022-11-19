# import random as r

# m = [[r.randint(-20, 10) for x in range(3)]for y in range(3)]
# count = 0
# for i in m:
#     for x in i:
#         print(x, end='\t\t')
#         if x < 0:
#             count +=1
#     print()
# print(f'Количество отрицательный элементов = {count}')


# m = [[r.randint(0, 4) for x in range(3)]for y in range(3)]
# count = 1
# for i in m:
#     for x in i:
#         print(x, end='\t\t')
#         if x != 0:
#             count = count * x
#     print()
# print(f'Произведение ненулевых элементов = {count}')