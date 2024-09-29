numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x+y,numbers1, numbers2)
print("Addition of two lists")
print(list(result))

num = [7, 8, 9, 10, 11, 12]
def square(n):
    return n * n
sq = list(map(square, num))
print("Square of numbers in the list :" )
print(sq)