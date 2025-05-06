file = open(r"..\Data\Log.txt")
for line in file:
    print(line.strip())
file.seek(0)


print("888888888888888888")

while file.readline() != "":
    print(file.readline().strip())
