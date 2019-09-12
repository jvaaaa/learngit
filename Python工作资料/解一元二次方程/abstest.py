#-*- coding:utf-8 -*-
import math
def quadratic(a,b,c):
	x=b**2-4*a*c
	x1=(-b+math.sqrt(b**2-4*a*c))/2*a
	x2=(-b-math.sqrt(b**2-4*a*c))/2*a
	if x>0:
		return(x1,x2)
	if x == 0:
		return(x1) 
	if x<0:
		print('无实根')