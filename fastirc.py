#!/usr/bin/env python3
import curses
import os
import sys
import math

from source.myCurses import *
from source.project import *
from source.myPrint import *

if (len(sys.argv)-1 ==0 ):
	vision = True
else:
	if (sys.argv[1] == 'more'):
		vision = False
	else:
		vision = True
myCmd = os.popen('ls | grep "\.log$"').read()
allFilesNames = myCmd.split()
nameProgram = 'FASTIRC'

if vision:
	screen = curses.initscr() # set the style
	curses.wrapper(do_it)    # pantalla de Inicio

	printCenter("WELLCOME TO "+nameProgram.upper(),screen)
	printFooterLeft("Version: 1.1",screen)
	printFooterRight("2020 ",screen)
	screen.refresh()
	curses.napms(3000)
    
	if len(allFilesNames) == 0:
		screen.clear()
		printCenter("No Files *.log :(",screen)
		screen.refresh()
		curses.napms(3000)
		curses.endwin()
		sys.exit(0)   # salir sin errores
else:
	printElement('-',40)
	printElementName(nameProgram.upper(),'-',40)
	printElement('-',40)
	if len(allFilesNames) == 0:
		printElementName('No Files *.log','=',40)
		sys.exit(0)   # salir sin errores


# List for the project

allProjectName =[]                  # Project Name
allBadFilesName = []                # Bad Project  Name

listProject = []                    # List Project 
listProjectIncomplete = []          # List Incomple Project 

# Load List All  Project & All Bad 

for i in range (len(allFilesNames)):
	name = allFilesNames[i]
	c1 = name.find('_irc.log') != -1 or name.find('_irc-f.log') != -1 or name.find('_irc-r.log') != -1
	c2 = name.find('-irc.log') != -1 or name.find('-irc-f.log') != -1 or name.find('-irc-r.log') != -1
	c3 = name.find('_IRC.log') != -1 or name.find('_IRC-F.log') != -1 or name.find('_IRC-R.log') != -1
	c4 = name.find('-IRC.log') != -1 or name.find('-IRC-F.log') != -1 or name.find('-IRC-R.log') != -1
	if   c1 or  c2 or c3 or c4:
		aux = allFilesNames[i].replace('.log','')
		aux = aux.replace('_irc-f','')
		aux = aux.replace('_irc-r','')
		aux = aux.replace('_irc','')
		aux = aux.replace('-irc-f','')
		aux = aux.replace('-irc-r','')
		aux = aux.replace('-irc','')
		aux = aux.replace('_IRC-F','')
		aux = aux.replace('_IRC-R','')
		aux = aux.replace('_IRC','')
		aux = aux.replace('-IRC-F','')
		aux = aux.replace('-IRC-R','')
		aux = aux.replace('-IRC','')
		#print('aux',aux)
		if not(aux in allProjectName):
			allProjectName.append(aux)
	else:
		allBadFilesName.append(allFilesNames[i].replace('.log',''))

#print('Contenido')
#print(allFilesNames)
#print(allBadFilesName)
#print('allProjectName:',allProjectName)
 
# load the project names

for i in range (len(allProjectName)):
	a = Project(allProjectName[i])
	a.loadingFiles(allFilesNames)
	a.checkUnique()
	if a.status2Files == True or a.statusCenter == True:
		listProject.append(a)
	else:
		listProjectIncomplete.append(a) 


#print('Project List:',listProject)

	

if len(listProject)!= 0:
	if vision:
		screen.clear()
		printTop("Project List",screen)
		for i in range (len(listProject)):
			aux=str(i)+': '+listProject[i].getName()
			printCenterPlus(aux,screen,i)
		screen.refresh()
	else:
		printElementName('Project List','*',40)
		for i in range (len(listProject)):
			print(str(i)+': ',listProject[i].getName())
		printElement('*',40)

else:
	if vision:
		screen.clear()
		printCenter("No Project  :(",screen)
		screen.refresh()
		curses.napms(2000)
		curses.endwin()
	else:
		printElementName('No Project  :(','=',40)
		sys.exit(0)   # salir sin errores



# Choose the project for work

flag = False

while True:
	if vision:
		answer = my_int_input('Choose Project',screen,flag)
	else:
		answer = checker('Choose Project')
	if ( answer < 0) or (answer > len(listProject)-1):
		if vision:
			flag = True
		else:
			print('Action not valid: ', answer)
	else:
		break

nproject = answer


# Step6

if vision:
    curses.napms(2000)
    screen.clear()
    printTop('*** Working ***',screen)
    screen.refresh()

else:
	printElementName('Working','*',40)

# working togheter
listProject[nproject].stageS1()
#listProject[nproject].viewColsHeader(0)
nameaux = listProject[nproject].getName()
if listProject[nproject].s1 :
	if vision:
	    curses.napms(1000)
	    screen.clear()
	    printCenter(nameaux,screen)
	    printTop('**** Working S1 ****',screen)
	    screen.refresh()
	else:
		printElementName(nameaux,'#',40) 
		printElementName(' --> S1 OK','',40) 

else:
	if vision:
	    curses.napms(1000)
	    screen.clear()
	    printCenter(nameaux,screen)
	    printTop('**** ERROR S1 ****',screen)
	    screen.refresh()

	else:
		printElementName(nameaux+'ERROR S1','*',40) 
	

nameCurrentProject = listProject[nproject].getName()
fileOutputCsv = nameCurrentProject +'_irc_cartesian_coord.csv'

#listProjectMethod[nproject].view()

colSize = 0
n = 0
buffer = ""
while True:
	if vision:

		answer = str(my_raw_input("Export Coord to CSV  y/n ? " ,screen))
		answer = answer.replace('b\'','')
		answer = answer.replace('\'','')

	else:
		if sys.version_info < (3,):  # python 2
			answer = raw_input("Export Coord to CSV    y/n: ?\n")
		else:
			answer = str(input("Export Coord to CSV    y/n: ?\n"))
	if answer == 'y':

		if listProject[nproject].statusCenter and not listProject[nproject].status2Files:
			t = listProject[nproject].colCenter
		elif not listProject[nproject].statusCenter and listProject[nproject].status2Files:	
			t = listProject[nproject].colLeft	
		colSize = len(t)  # largo de columas
		print('colSize:', colSize)
		if colSize > 2:
			if vision:
				screen.clear()
				printTop("Coord List",screen)
				if colSize > 5:
					for i in range (colSize): 
						if i > 1 :
							if i%10 == 0:
								buffer +=  str(i)+':'+t[i].colName+'\n'
							else:
								buffer += str(i)+':'+t[i].colName+'  '
					buffer = buffer.split('\n')
					for i in range(0,len(buffer)):
						printCenterPlus(buffer[i],screen,i+1)
				else:
					for i in range (colSize):
						if i > 1:  # no van las dos primeras
							aux=str(i)+': '+t[i].colName
							printCenterPlus(aux,screen,i)
				screen.refresh()
			else:
				printElementName('CoordList','*',40)

				if colSize > 5:
					for i in range (colSize): 
						if i > 1 :
							if i%10 == 0:
								buffer +=  str(i)+': '+t[i].colName+'\n'
							else:
								buffer += str(i)+': '+t[i].colName+' '
					print(buffer)
				else:
					for i in range (colSize):
						if i > 1 :
							print(str(i)+': ',t[i].colName)
				printElement('*',40)

			if vision:
				while True:
					answer = str(my_raw_input("Choose Coords by , ? " ,screen))
					answer = answer.replace('b\'','')
					answer = answer.replace('\'','')

					if len(answer)>1:
						a=answer.replace(',','')
					else:
						a=str(answer)
					if a.isdigit():  # numeros
						num = answer.split(',')
						#print('lent:',len(t))
						if numberCompares(num, colSize ):
							#print('True',num)
							break
						else:
							#print('False',num)
							continue
					else:
						screen.clear()
						printCenter("Error only digits",screen)
						screen.refresh()
						curses.napms(1000)
						screen.clear()

			else:
				while True:
					if sys.version_info < (3,):  # python 2
						answer = raw_input("Choose Coords by , ? \n")
					else:
						answer = str(input("Choose Coords by ,? \n"))
					if len(answer)>1:
						a=answer.replace(',','')
					else:
						a=str(answer)
					if a.isdigit():  # numeros
						num = answer.split(',')
						#print('lent:',len(t))
						if numberCompares(num, colSize ):
							#print('True',num)
							break
						else:
							#print('False',num)
							continue
					else:
						print('Error only digits')
			
			fileOutputCsv = nameCurrentProject +'_irc_cartesian_coord.csv'
			csv(fileOutputCsv , listProject[nproject],  answer)
			if vision:
				screen.clear()
				printTop('*** Csv File: ***',screen)
				printCenter(fileOutputCsv,screen)
				curses.napms(1000)
				screen.refresh()
			else:
				printElementName('Output Files','*',40)
				print('Csv File:',fileOutputCsv)
				printElement('*',40)

		else:
			fileOutputCsv = nameCurrentProject+'_irc.csv'
			csv(fileOutputCsv , listProject[nproject],  "Basic")
			if vision:
				screen.clear()
				printCenter("*** No Coord! ***",screen)
				printCenterPlus('Csv File:',screen,2)
				printCenterPlus(fileOutputCsv,screen,4)
				screen.refresh()
				curses.napms(1000)
				screen.clear()
				printTop('*** Working ***',screen)

			else:
				printElementName("No Coord  :(",'*',40)
				printElementName('Output Files','*',40)
				print('Csv File:',fileOutputCsv)
				printElement('*',40)
			break
		break
	elif answer == 'n':
		fileOutputCsv = nameCurrentProject+'_irc.csv'
		csv(fileOutputCsv , listProject[nproject],  "Basic")
		if vision:
			screen.clear()
			printTop('*** Csv File: ***',screen)
			printCenter(fileOutputCsv,screen)
			curses.napms(1000)
			screen.refresh()
		else:
			printElementName('Output Files','*',40)
			print('Csv File:',fileOutputCsv)
			printElement('*',40)
		break
	else:
		if vision:
			screen.clear()
			printTop('*** Working ***',screen)
			printFooter('Action not valid: ' +  answer ,screen)
			curses.napms(1000)

			screen.refresh()
		else:
			print('Action not valid: ', answer)




if vision:

	curses.napms(2000)
	screen.clear()

	printCenter('Thanks you :) ',screen)
	screen.refresh()
	curses.napms(2000)
	curses.endwin()
else:
	printElement('-',40)
	printElementName('Thanks :)','-',40)
	printElement('-',40)

