str1 = "Hi"
str2 = "Prite"

str3 = str1 + ", " + str2

# print(f"Concat Data1: {str3}")


# string length
str = "Hello, World"

data_length = len(str)
# print(data_length)

# lowercase and uppercase
low = str3.lower()
up = str3.upper()

# print(low, up)


abb = "Python is very easy to learn language"
alter = abb.replace("very", "very very")

# print(alter)

strArr = abb.split(" ")

# print(strArr)

text = "   Hi, Prite   "
stripedText = text.strip();

print(stripedText)


# Substring
if "python" in abb.lower():
    print("Hurrah! I found it")
else:
    print("Alas! I didn't find it")
    

