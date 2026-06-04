my_list = [1, 2, 3, "a", "b", "c"]
my_list.insert(3, 0)
my_list.extend(["d", "e", "f"])

slice_items = my_list[:]

print("Sliced items: ", slice_items)
print("All items: ", my_list)