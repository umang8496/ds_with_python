filename="writefile.txt"

myfile=open(filename,'w')
myfile.write("Written with Python\n")

myfile.close()
print("file has been created")


##Flag	Action
##r	Open file for reading
##w	Open file for writing (will truncate file)
##b	binary mode
##r+	open file for reading and writing
##a+	open file for reading and writing (appends to end)
##w+	open file for reading and writing (truncates files)
