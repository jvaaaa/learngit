#-*- coding:utf-8 -*-
def move(n,a,b,c):
	if n ==1:
		return(a,'-->',c)
	return(move(n-1,a,b,c),a,'-->',b,
		move(n-1,c,b,a),b,'-->',c,move(n-1,a,b,c))