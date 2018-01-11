#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime

numero=3
fecha1='Nov 24 05:45:22'
fecha2='Nov 24 16:28:14'
pregunta ='122.225.18.142'

def ana():
	f = open ('auth.log', 'r')
	ha={}
	ataques=[]
	menor = datetime.strptime(fecha1,'%b %d %H:%M:%S')
	mayor = datetime.strptime(fecha2,'%b %d %H:%M:%S')
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
			if fe >= menor and fe <= mayor:
				ataques.append(ip)
			resultados = ataques.count(pregunta)
			if resultados >= numero:
				final = pregunta
			else:
				final = 'No se han encontrado tantos ataques.'
	
	print final						
	f.close()
	for ip in ha:
		ha[ip].sort(reverse=True)
	return ha
dic = ana()
