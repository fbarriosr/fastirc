import os
import sys
from source.myPrint import *


class data:
	def __init__(self, key, value):
		self.dato = {'key': key,
					 'value': value	
					}
	def view(self):
		print(self.dato['key'], self.dato['value'])

class header:
	
	def __init__(self, name):
		self.colName = name
		self.lista = []
	def view(self):
		print('col: ',self.colName)
		for list in self.lista:
			list.view()

class Project:
	name = ""

	statusCenter = False
	status2Files = False
	errorMsg     = "No message"
	flagWindow   = False
	flagScaneado = False
	s1 = False

	def __init__(self, name):
		self.name 			= name
		self.colCenter   	= []
		self.colLeft   		= []
		self.colRight   	= []
		self.files 			= []

	def getNamePosFile(self):
		aux = self.name+'_irc-f.log'
		if self.status2Files:
			if aux in self.files:
				return aux
			else:
				return "False"
		else:
			return "False"

	def getNameNegFile(self):
		aux = self.name+'_irc-r.log'
		if self.status2Files:
			if aux in self.files:
				return aux
			else:
				return "False"
		else:
			return "False"

	def getNameMainFile(self):
		aux = self.name+'_irc.log'
		if self.statusCenter:
			if aux in self.files:
				return aux
			else:
				return "False"
		else:
			return "False"

	def getName(self):
		return self.name
	def getShortName(self):
		return self.shortName
		
	def viewName(self):
		print('Name:',self.name)

	def view(self):
		printElement('-',40)
		print('Name:',self.name)
		print('files:',self.files)
		print('status2Files:',self.status2Files)
		print('statusCenter:',self.statusCenter)
		print('error:',self.errorMsg)
		printElement('-',40)
		return

	def viewColsHeader(self,number):
		self.colCenter[number].view()
		

	def loadingFiles(self, allFilesNames):
		self.files =[]
		for i in range (len(allFilesNames)):
			if allFilesNames[i].find(self.name) != -1:           # encuentra los archivos del proyecto
				self.files.append(allFilesNames[i])
		#print('files:',self.files)
		return
		
	def checkUnique(self):
		countNIrcf = 0
		countNIrcr = 0
		count      = 0

		for i in range (len(self.files)):
			if   self.files[i].find('_irc-f.log') != -1:
				countNIrcf += 1
			elif self.files[i].find('_irc-r.log') != -1:
				countNIrcr += 1
			elif self.files[i].find('_irc.log') != -1:
				count 	   += 1

		#print('file:',self.files)
		#print('countNIrcf:',countNIrcf)
		#print('countNIrcr:',countNIrcr)
		#print('countN    :',count)

		if (len(self.files) == 2):
			if ( (countNIrcf == 1 ) and (countNIrcr == 1 )  ):
				self.status2Files = True
				self.statusCenter = False
				
			elif ( (countNIrcf == 1 ) and (count== 1 )  ):
				self.status2Files = False
				self.statusCenter = False
				archivo = self.name + "_irc-r.log"
				self.errorMsg = "Hay errores. Te falta el archivo: "+ archivo
			elif ( (countNIrcr == 1 ) and (count== 1 )  ):
				self.status2Files = False
				self.statusCenter = False
				archivo = self.name + "_irc-f.log"
				self.errorMsg = "Hay errores. Te falta el archivo: "+ archivo

		elif (len(self.files) == 1):
			if ( countNIrcf == 1 )  :
				self.status2Files = False
				self.statusCenter = False
				archivo1 = self.name + "_irc.log"
				archivo2 = self.name + "_irc-r.log"
				self.errorMsg = "Hay errores. Te faltan los archivos: "+ archivo1+' y ' + archivo2
			elif ( countNIrcr == 1 )  :
				self.status2Files = False
				self.statusCenter = False
				archivo1 = self.name + "_irc.log"
				archivo2 = self.name + "_irc-f.log"
				self.errorMsg = "Hay errores. Te faltan los archivos: "+ archivo1+' y ' + archivo2
			elif ( count == 1 )  :
				self.status2Files = False
				self.statusCenter = True
				
		elif (len(self.files)  >= 3):
			self.status2Files = False
			self.statusCenter = False
			archivo1 = self.name + "_irc.log"
			archivo2 = self.name + "_irc-r.log"
			archivo3 = self.name + "_irc-f.log"
			self.errorMsg = "Hay errores, se encontraron multiples archivos, solo debes tener un archivo:"+archivo1+', o dos archivos:'+archivo2 +' y '+archivo3
		return


	def finder(self, fileName):
		self.flagWindow = False
		self.flagScaneado = False
		columnas = []
		p = 0
		prevLine = '0'
		#print(fileName)
		with open(fileName) as f:
				lines = f.readlines() #read
				f.close()

		for line in lines:
			if not(self.flagWindow) and not(self.flagScaneado) : 
				prev    = prevLine.upper().find('SUMMARY OF REACTION PATH FOLLOWING')
				current = line.find('--------')
			    # buscamos Sistema
				if prev != -1 and current!= -1:   # abrirmos la ventana y el scan
					#print('openWindow')
					#print('*',line)
					self.flagWindow = True
					self.flagScaneado = False
					
			elif self.flagWindow and not(self.flagScaneado):  # ventana abierta y escaneado
				aux = line.find('--------')  # buscamos el final de la ventana
				if aux == -1 : # no lo encontro
						
					dataArray = line.split()

					try:
						key = int(dataArray[0])
						#print('$',dataArray)      # datos
						
						for i in range (1,len(dataArray)):

							#print('grabando:',self.col[p+i-1].colName )
							t = data(key, dataArray[i])
							columnas[p+i-1].lista.insert(len(columnas[p+i-1].lista),t)		
	
					except ValueError:
			
						#print('C',line)  # col names
						flagRecorded = True
						
						p = len(columnas)  # primer valor de las col
						
						#print('p1',p)
						#print(dataArray)
						for d in dataArray:
							t = header(d)
							columnas.append(t)


					self.flagWindow = True
					self.flagScaneado = False
				elif aux != -1 :  # lo encontro
					#print('#',line)
					#print('CloseWindow')
					self.flagWindow = False
					self.flagScaneado = True
					
			prevLine = line
		
		#print('columnas',len(columnas))
		
		return columnas


	def stageS1(self):
		if self.statusCenter:
			self.colCenter = self.finder(self.getNameMainFile())
			self.s1 = True
		elif self.status2Files:
			self.colLeft 	= self.finder(self.getNameNegFile())
			self.colRight 	= self.finder(self.getNamePosFile())
			self.s1 = True



def checker(message):
	if message == "":
		inputt = input()
	else:
		inputt = input(message+'\n')
	try:
		return int(inputt)
	except ValueError:
		print ("Error!, Enter a number!")
		return checker("")

def numberCompares(list, number):
	for value in list:
		#print('value',value)
		if int(value) > 1 and int(value) < number:
			continue
		else:
			return False
	return True
								

