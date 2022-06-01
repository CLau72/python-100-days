# FileNotFound
try:
    with open("a_file.txt") as file: 
        output = file.read()
except FileNotFoundError:
    with open("./a_file.txt", mode="w") as file:
        file.write("Start File")
else:
    print(output)
finally:
    print("operation complete")
#KeyError
# dictionary = {"key": "value"}
# value = dictionary["other_key"]

#
