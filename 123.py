#-*- coding:utf-8 -*-
def unlock(L, t=3):
	a1 = []
	n=t%26
	for i in L:
		if 97<=ord(i)<=122:
			if (ord(i))-n < 97:
				c = (chr(ord(i)-n+26))
				a1.append(c)
			else:
				c = chr(ord(i)-n)
				a1.append(c)
		elif 65<=ord(i)<=90:
			if (ord(i))-n < 65:
				c = (chr(ord(i)-n+26))
				a1.append(c)
			else:
				c = chr(ord(i) - n )
				a1.append(c)
		else:
			c = i
			a1.append(c)
	a2 = ('').join(a1)
	return a2
def lock(L, t=3):
	a3 = []
	n=t%26
	for i in L:
		if 97<=ord(i)<=122:
			if (ord(i))+n > 122:
				c = (chr(ord(i)+n-26))
				a3.append(c)
			else:
				c = chr(ord(i)+n)
				a3.append(c)
		elif 65<=ord(i)<=90:
			if (ord(i))+n > 90:
				c = (chr(ord(i)+n-26))
				a3.append(c)
			else:
				c = chr(ord(i)+n)
				a3.append(c)
		else:
			c = i
			a3.append(c)
	a4 = ('').join(a3)
	return a4
print('凯撒解密输入1，凯撒加密输入2:')
x=int(input())
print(x)
if x==1:
	print('凯撒解密中')
	L=input('请输入暗文：')
	n=int(input('请输入位移数(默认为3)：'))
	print(unlock(L,n))
elif x==2:
	print('凯撒加密中')
	L=input('请输入明文：')
	n=int(input('请输入位移数(默认为3)：'))
	print(lock(L,n))