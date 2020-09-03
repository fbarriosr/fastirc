import os
def printElement(element, large):
	print (element.replace(element, element * large,1))
	return 0
		
def printElementName(name,element, large):
	s = element.replace(element, element * large,1)
	name = ' '+name+' '
	t1 = len(name)
	t2 = len(s)

	position = int( t2/2 - t1/2 -1)

	s = s[:position] + name + s[position+t1:]
	print (s)

	return 0

def csvData(fileName, columna ,headerOption, deleteZero):

	#header = ' \t '.join(projects[0].labels())
	#header += '\n'
	#print('Csv File:',fileName)
	header = []
	auxHeader = ''
	aux = ''
	data = []

	if headerOption:
		option = 'w'
	else:
		option = 'a'
	with open(fileName,option) as f:
		if headerOption:
			for obj in columna:
				header.append(obj.colName)
			header.insert(0, 'id')
			auxHeader = ' \t '.join(header)
			f.write(auxHeader+'\n')
		for i in range (0,len(columna[0].lista)):
			for obj in columna:
				#print('***',obj.colName)
				#print('¢¢',obj.lista[i].dato['value'])
				data.append(obj.lista[i].dato['value'])
			data.insert(0, str(columna[0].lista[i].dato['key']))
			aux = ' \t '.join(data)

			if deleteZero:
				if i != len(columna[0].lista)-1:
					f.write(aux+'\n')
			else:
				f.write(aux+'\n')

			data = []
			
		f.close()

	return 0

def csv(fileName, project,modo):
	t = []
	t1 = []
	t2 = []
	if project.statusCenter and not(project.status2Files):
		if modo == "All":
			t =  project.colCenter
		elif modo == 'Basic':
			t.append(project.colCenter[0])
			t.append(project.colCenter[1]) 
		else:
			modo = modo.split(',')
			t.append(project.colCenter[0])
			t.append(project.colCenter[1]) 
			for col in modo:
				t.append(project.colCenter[int(col)])
		csvData(fileName, t  , True, False)	
	elif not(project.statusCenter) and project.status2Files:
		if modo == "All":
			t1 =  project.colLeft
			t2 =  project.colRight
		elif modo == 'Basic':
			t1.append(project.colLeft[0])
			t1.append(project.colLeft[1]) 
			t2.append(project.colRight[0])
			t2.append(project.colRight[1]) 
		else:
			modo = modo.split(',')
			t1.append(project.colLeft[0])
			t1.append(project.colLeft[1]) 
			t2.append(project.colRight[0])
			t2.append(project.colRight[1]) 
			for col in modo:
				t1.append(project.colLeft[int(col)])
				t2.append(project.colRight[int(col)])
		csvData(fileName, t1 ,  True, True)
		csvData(fileName, t2 ,  False, False)
	return 0

