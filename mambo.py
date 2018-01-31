#!/usr/bin/env python
#-*- coding: utf-8 -*-
from random import randrange
class Minas:
	"""Agrupa todos los atributos y métodos relacionados con Mambo
	   Los niveles de dificultad son 1 (8x12), 2 (16x20), 3 (24x28) """
	def __init__(self, nivel):
		self.filas = nivel*8
		self.columnas = nivel*8+4
		self.nubo= self.filas*self.columnas/5*nivel
		self.campo =[]
		fila = []
		for i in range(self.filas):
			self.campo.append(fila)
			for j in range(self.columnas):
				self.campo[i].append('_')
		self.__metebombas()
	def __metebombas(self):
		for bomba in range(self.nubo):
			fila = randrange(self.filas)
			colu = randrange(self.columnas)
			while self.campo[fila][colu] == 'B':
				fila = randrange(self.filas)
				colu = randrange(self.columnas)
			self.campo[fila][colu] = 'B'
		
	def mostrar(self):
		for i in range(self.filas):
			for j in range(self.columnas):
				print self.campo[i][j],
			print
