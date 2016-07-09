#   Exercise 3:...........................................................
# Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in,
#  but writing it yourself is nevertheless a good exercise.)

def coutStringLength(inputString):
    cout = 0
    for i in inputString:
        cout = cout + 1
    return cout
String = input("Input a string: ")
print("String has: " + str(coutStringLength(String)))

# Find length of the List..............................................

list = [1,2,3,4,5,6,'truong', 'python']
list_count = 0
for i in list:
     list_count = list_count + 1

print("list length: " +str(list_count))

# su dung ham leng(str) co san!........................................

x = input("nhap chuoi")
print(len(x))
