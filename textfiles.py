# myfile = open("fruits.txt")
# print(myfile.read())
#
# myfile.close()

with open("files/fruits.txt") as myfile: ###this only opens the file for this operation.
    content = myfile.read()

###read write
with open("files/vegetables.txt", "w") as myfile: #open with no file there just writes it
    myfile.write("Tomato\nCucumber\nOnion\n") ###don't forget to \n for a new line or it will just append
    myfile.write("Garlic")
