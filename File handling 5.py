# PHYTHON FILE HANDLING - CRUD(create,update,delete,read)
# "r" = read
# "a" = append
# "w" = write
# "x" = create
# "t" = text
# "b" = binary - image mood

# to open a file

F = open("demo.txt",'r')
print(F.read())

"""to read any file, make sure to put the file format behind like py for python, doc for word, pdf for pdfs,
csv for a csv file, xls for an excel file"""

# if you want the first 5 letters to show
F = open("demo.txt","r")
print(F.read(5))

# to print just the first line
F = open("demo.txt","r")
print(F.readline())

# to add words to a file, a= append and that adds to the end of the file, w= overide everything
# x.close is optional
x = open('demo.txt','a')
x.write('Python is amazing')
x.close

# to write
x = open('demo.txt','w')
x.write('Python is amazing')
x.close

# To create a file

x = open('Newfile.py','x')



