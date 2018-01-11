#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime

numero=3
contador=0
fecha1='Nov 24 05:45:22'
fecha2='Nov 24 07:13:33'

def ana():
	f = open ('auth.log', 'r')
	ha={}
	ataques=[]
	for lin in f.readlines():
		if 'authentication failure' in lin:
			li=lin.split()
			sfe = li[0]+li[1]+li[2]
			fe = datetime.strptime(sfe,'%b%d%H:%M:%S')
			for ele in li:
				if 'rhost' in ele:
					ip = ele[6:]
			if ip not in ha:
				ha[ip]=[]
			ha[ip].append(fe)
	for lin in f.readlines():
		
		while contador <= numero:
			ataques.append()
						
	f.close()
	for ip in ha:
		ha[ip].sort(reverse=True)
	return ha
dic = ana()




