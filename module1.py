#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SyntaxShreya
#
# Created:     27-10-2023
# Copyright:   (c) SyntaxShreya 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def findlen(x):
    print(len(x))

def search(x, y):
    if y in x:
        print("Yes, present from", x.find(y))
    else:
        ("not present")

def reverse(x):
    print(x[::-1])

def swapstr(x,y):
    x,y = y,x
    print("Main string is:", x)
    print("New string is:", y)

string = input("Enter string: ")
print("Length of string is:")
findlen(string)
print()
substring = input("Enter substring you want to search: ")
search(string,substring)
print()
print("Reverse is:")
reverse(string)
print()
newstring=input("Enter new string to swap with main string: ")
swapstr(string,newstring)