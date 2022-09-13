#现成变量运算
x=3
y=4
z=5
q = (x+y+z)/2 #三角形三边和一半
s = (q*(q-x)*(q-y)*(q-z))**0.5 #海伦公式求面积
print(float(s)) #输出s

#交互式运算
x = int(input('x:')) #input的数据类型为字符串,要用int函数将其类型转换为整型
y = int(input('y:')) 
z = int(input('z:'))
q = (x+y+z)/2
s = (q*(q-x)*(q-y)*(q-z))**0.5
print(s)

#函数式
def s(x,y,z):
    q = (x+y+z)/2
    s = (q*(q-x)*(q-y)*(q-z))**0.5
    print(s)
s(3,4,5)
