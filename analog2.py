#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime
formato = "%b %d %H:%M:%S"
fecha = []
dic = {}
contador = 0
fichero_origen = open('auth.log', 'r')
for linea in fichero_origen.readlines():
	if 'authentication failure' in linea:
		fecha.append(datetime.strptime(linea[0:15],formato))
		spl=linea.split()
		ip=spl[13]
		clave=ip[6:]
		dic[clave]=linea[0:15]
		
#		if dic.has_key(clave):
#			dic[clave] += ','+linea[0:15]
				
		
fichero_origen.close
print fecha

