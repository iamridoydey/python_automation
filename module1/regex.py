import re

match = re.findall(r".i", "Hi, Prite")
# print(match)

match2 = re.findall(r"\br([a-zA-Z]+)(\d+)\b", "rkprite9 ridoydey pritedey09 rkp21")
# print(match2)

text = "red t-shirt, red car"
regex = r"red"
replacement = "brown"
modifiedText = re.sub(regex, replacement, text)
# print("Modified text: ", modifiedText)


csvText = "red,brown,black,blue,purple"
pattern = r","
arr = re.split(pattern, csvText)
print("Csv text to arr: ", arr)