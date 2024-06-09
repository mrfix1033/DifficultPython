# RU: Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).
# EN: A list of numbers is given [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# You need to write out only positive numbers from this list until you meet a negative one or the list ends (going abroad).

# A simple solution
array = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(array):
    element = array[i]
    i += 1
    if element < 0:
        break
    elif element == 0:
        continue
    print(element)

# A difficult solution (yes, it's slower)
print(*[elem for elem in array[:(array + [-1]).index(([i for i in array + [-1] if i < 0])[0])] if elem != 0], sep='\n')
