#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime
formato = "%b %d %H:%M:%S"
fecha = []
dic = {}
prueba = []
fichero_origen = open('auth.log', 'r')
for linea in fichero_origen.readlines():
	if 'authentication failure' in linea:
		fecha.append(datetime.strptime(linea[0:15],formato))
		spl=linea.split()
		ip=spl[13]
		clave=ip[6:]
		if clave in linea:
			prueba.append(linea[0:15]+',')
			dic[clave]=prueba
				
		
fichero_origen.close
for dia in fecha:
	print datetime.strftime(dia, '%m %d %H:%M:%S')

print dic
