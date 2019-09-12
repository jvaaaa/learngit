#-*- coding:utf-8 -*-
from abstest import quadratic
a=float(input('请输入一元二次方程的a\n'))
b=float(input('请输入一元二次方程的b\n'))
c=float(input('请输入一元二次方程的c\n'))
x=b**2-4*a*c
if x<0:
	print('无实根')
else:
	print('该方程的两根为：',quadratic(a,b,c))