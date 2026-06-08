my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['city']
my_dict['city'] = "Zurich"
print(f"Hi I am {my_dict['name']}, I am from {my_dict['city']}")

print(my_dict)