# tao ham Tim so lon nhat trong 3 so

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

x = int(input("nhap vao x= "))
y = int(input("nhap vao y= "))
z = int(input("nhap vao z= "))

# goi ham - luu y la phai them 'str' truoc ham do
print ("so lon nhat la" + str(maxofthree(x,y,z)))
