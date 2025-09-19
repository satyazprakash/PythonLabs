# This Program will provide instruction to open a file, if the file is not found then it will create teh file.

file = open ('/Users/satya/Desktop/New Tech Stack/python/newsamplefile.txt', "w")
file.write("My name is John. This is some sample text that needs to be writtten to the opened file in write mode, I am running htis file again.. ")
file.close()


file = open ('/Users/satya/Desktop/New Tech Stack/python/newsamplefile_append.txt', "a")
file.write("This is code block to append text in the file, observer that via option a  ")
file.close()
