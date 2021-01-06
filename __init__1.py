#单参数传递
#def test(x):
#   print(x)
#test(2)

#位置参数：
#def test_1(x,y):
#    print(x,y)
#test_1(2,4)

#不定长参数：
#def test (*num):
#    print(num)
#test(1,2,'hello print')

#关键字参数：
#def test(x,y):
#    print(x)
#    print(y)
#test(x=1,y=2)

#关键字参数和位置参数混合使用的情况下：
#关键字函数的赋值要放到位置函数赋值的后面
#def test(name,age):
#    print(name)
#    print(age)
#test('小龙',age=10)

#给参数设定默认值：
#默认值在形式参数设置的时候已经设置好 (小花，1)
#在给实际参数赋值的时候，是可以不赋值的，会默认使用已经设置好的参数，赋值的话则会变成新的参数
#def test(name='小花',age=1):
#    print(age)
#test(name='小兰',)

#不定长传参：
#def test(x,*abc):
#    for i in abc:
#        print('当前数字',i)
#    print(x)
#test(1,2,3,'a','b')

#混合使用时，不定长参数要放在最后面：
#def test(x,*abc):
#    print(abc)
#    print(x)
#s=[1,2,3]
#test(*s)

#用列表元组里面的参数，注意个数必须和函数里面的格式相同，以下面的例子举例，s里面是两个数，分别给a和b，不然会报错
#def test(a,b):
#    print(a)
#    print(b)
#s=[1,2]
#test(*s)

#不定长关键字参数 入参必须是键值对的格式， 返回的结果也是字典
#def test(**abc):
#    print(abc)
#test(name='小花',age=12,highet=1.6,weight=120)

#用已知字典进行不定长函数的传参：
#def test(**abc):
#    for i in abc.items():
#        print(i)
#dict={'name':'小明','age':15}
#test(**dict)

#复杂的混合使用
#def test(name,age=12,*height,**weight):
#    print(name,'\n',age,'\n',height,'\n',weight)

#test('小强',13,weight=120)
#test('小强',13,150,weight=120)
#小强
# 13
# ()
#{'weight': 120}
#小强
# 13
# (150,)
# {'weight': 120}.


