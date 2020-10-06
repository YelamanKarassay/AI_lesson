# method checks solvability of 8-puzzle
def isSolvable(array):
    counter = 0

    for i in range(8):
        for j in range(i + 1, 9):
            if array[j] and array[i] > array[j]:
                counter += 1

    return counter % 2 == 0



# 0(zero) is empty slot

# figure 1 from Home work example, which is solvable
figure1 = [1, 8, 2,
           0, 4, 3,
           7, 6, 5]
# figure 2 from Home work example, which is not solvable
figure2 = [8, 1, 2,
           0, 4, 3,
           7, 6, 5]
# figure 3, randomly written puzzle by myself
figure3 = [1, 4, 5,
           0, 6, 7,
           2, 8, 3]

print(isSolvable(figure1))

print(isSolvable(figure2))

print(isSolvable(figure3))
