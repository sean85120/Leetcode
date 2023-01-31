# enumerate
values = ['a', 'b', 'c']

index = 0

# for value in values:
#     print(index, value)
#     index += 1

for index, value in enumerate(values):
    print(index, value)


# pass array into function
def test_array(a):
    for i in a:
        i = 2*i

    return a

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(test_array(x))

