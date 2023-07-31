### 리스트 메소드 복습

numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

fruit = ['apple', 'orange', 'grape']
fruit.insert(1, 'banana')
print(fruit)

numbers = [1, 2, 3, 4, 5]
remove_number = numbers.pop()
print(remove_number)
print(numbers)
