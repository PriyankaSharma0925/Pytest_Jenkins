from os import write

file = open(r"..\Data\Log.txt", "r")
for line in file:
    print(line.strip())
file.seek(0)

print(file.readline())


while file.readline() != "":
    print(file.readline().strip())

file.close()


with open(r"..\Data\Hello.txt", "w") as writer:
    writer.write("Hi World!!")
