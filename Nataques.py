#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime

numero=3
fecha1='Nov 24 05:45:22'
fecha2='Nov 24 08:42:00'

def ana():
	f = open ('auth.log', 'r')
	ha={}
	ataques=[]
	for lin in f.readlines():
		if 'authentication failure' in lin:
			li=lin.split()
			#print li
			sfe = li[0]+li[1]+li[2]
			#print sfe
			fe = datetime.strptime(sfe,'%b%d%H:%M:%S')
			for ele in li:
				if 'rhost' in ele:
					ip = ele[6:]
					#print ip
			if ip not in ha:
				ha[ip]=[]
			ha[ip].append(fe)
			if lin[0-14] >= fecha1 and <= fecha2:
				if ip in lin:
					
				
						
	f.close()
	for ip in ha:
		ha[ip].sort(reverse=True)
	return ha
dic = ana()




