my_tuple = (1, 2, "a", "b")

a, b, c, d = my_tuple

print(a, b, c, d)

sec_tuple = (3, 4, "c", "d")

concat_tuple = my_tuple + sec_tuple

print(concat_tuple)


my_slice = my_tuple[3:]
print(my_slice)

etc_tuple = ("r", "i", "t", "u")
print(etc_tuple)
del etc_tuple


try:
    etc_tuple
except NameError:
    print("Etc tuple being deleted")
    
if "a" in my_tuple:
    print("Yeah! a does exist!")