#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Se trata de modificar el código para que el coche no pueda conducirse
# cuando no esté arrancado y no arrancarse cuando ya lo está
class Coche:
	'''Abstraccion de los objetos coche.'''
	def __init__ (self, gas, col):
		self.gasolina = gas
		self.color = col
		self.estado = 'Parado'
		print 'Tenemos', self.gasolina, 'litros'
	def arrancar(self):
		if self.gasolina > 0 and self.estado == 'Parado':
			self.estado = 'Arrancado'
			print 'Arranca'
		else:
			print 'No arranca'
	def conducir(self):
		if self.gasolina > 0 and self.estado == 'Arrancado':
			self.gasolina -= 1
			print 'Quedan', self.gasolina, 'litros'
		else:
			print 'No se mueve'
			

