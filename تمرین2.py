from operator import itemgetter
def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if (data[j]['First Name'], data[j]['Last Name']) < (data[min_index]['First Name'], data[min_index]['Last Name']):
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
data = [
    {'First Name': 'Amir', 'Last Name': 'Jab'},
    {'First Name': 'Ali', 'Last Name': 'Rahmani'},
    {'First Name': 'Armaan', 'Last Name': 'Vahadi'},
    {'First Name': 'Mohamad', 'Last Name': 'Hodian'}
]
selection_sort(data)
print(data)