def selection_sort(data):
  for i in range(len(data) - 1):
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j]['First Name'] < data[min_index]['First Name'] or (data[j]['First Name'] == data[min_index]['First Name'] and data[j]['Last Name'] < data[min_index]['Last Name']):
        min_index = j
    data[i], data[min_index] = data[min_index], data[i]
  return data