#!/usr/bin/env python
#
''' Studying for the CWNA and wrote this to do the math for me to check and understand the examples better.

you can solve for dBm or mW using the math.log function for a more accurate that number or use the rules of 3s and 10s to get close '''

import math




#Solving for dBm based off formula.
#from my understand the math is pretty acturate
def solve_dBm():
	print' ~~~~~~~~~~~~~~~~~~~~~~~~~~ '
	mW=input('What is your mW? ')
	dBm = 10*(math.log10(mW))
	print ' '
	print 'Your dBm is: ', dBm
	print''



#Solving for dBm based off formula
def solve_mW():
	print ' ~~~~~~~~~~~~~~~~~~~~~~~~~ '
	dBm=input('What is your dBm? ')
	mW=math.pow(10,(dBm/float(10)))
	print ''
	print 'Your mW is: ',mW
		
	
	
#Rules of 3s and 10s calculates.
#NOT an expert, math was check against examples on line so... :)
def ruleofrules():
	total_dBm=0
	total_mW=1
	print' ================================================================== '
	print 'Estimate the dBm or mW need with  rule of 10s and 3s :)'
	print ' '
	num=''	
	while(num != 0):
		print' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'		
		print ' Add or Subtract 10 or 3 for you target goal'
		print ' [0] Quit'
		print ' [8]Restart'
		print ''
		num = input ('Ex: \'10\' for plus 10 or \'-3\' for minus three ')
			  
		if (num == 3):
			total_dBm= total_dBm+3 
			total_mW= total_mW*2
			print ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'	
			print ' Current', total_dBm, 'dBm :: ',total_mW, 'mW'
						
		elif (num == -3):
			total_dBm= total_dBm-3
			total_mW= total_mW/2
			print ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			print ' Current', total_dBm, 'dBm :: ',total_mW, 'mW'
			

		elif (num == 10):
			total_dBm= total_dBm+10
			total_mW= total_mW*10
			print' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			print' Current', total_dBm, 'dBm :: ',total_mW, 'mW'
			
		
		elif (num == -10): 
			total_dBm= total_dBm-10
			total_mW= total_mW/float(10)
			print' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			print' Current', total_dBm, 'dBm :: ',total_mW, 'mW'
				
					
		elif (num==8):
			total_dBm=0
			total_mW=1
			print ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			print ' Current', total_dBm, 'dBm :: ',total_mW, 'mW'
			 

		else:
			' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' 
			print ' Current', total_dBm, 'dBm :: ',total_mW, 'mW'
			print ' Choose a number that is 10, 3, -10, -3 :P '
			


#FRESNEL ZONE
def fresnel_midpoint():
#calculate the radius of the first Fresnel zone at the mid point between two antennas
	print ' ================================================= '
	print 'Calulating the Fresnel Zone either whole zone or\n the minimum of 60% at midpoint of two antennas'
	print''
	D=input(' What is the distance of the link in miles?  ')
	print float(D)
	print '' 
	F=input('What is the transmitting freqency in GHz')
	print float(F)
	print ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
	print ' [1] Calculate the whole zone '
	print ' [2] Calculate the minimun 60% unobstructed zone'
	print ' [0] Quit '
	print''
	opt=input(' ')

	while opt!=0:
		if opt == 1:
			print' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			radius=(72.2*(math.sqrt(D/float(4)*F)))
			print  'Radius is: ',radius
			print 	'Optimal clearence that you will want along the singal path.'
			print''
		
		elif opt == 2:
			print' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			#calculate the min 60% unobstructed
			radius = 43.4*(math.sqrt(D/float(4)*F))
			print 'Min radius: ',radius

		elif opt ==0:
			break
		
		else: 
			print' Not an option '



#Any point between two antennas to obsticle 
def fresnel_anypoint():
	print '==================================================='
	#calculate the fresnel zone at any point between two antennas

	print'Calculating the fresnel zone\n at any point between two antennas'
	print''
	N = input('Which Fresenel Zone are you calculating? (normally 1 or 2) ')
	print''
	print ' First what is distance from the obstacle \(in miles\) to the first antenna?  '
	d1=input('D1: ')
	print ''
	print '  Now the distance between the obstacle (in miles) to the other antenna?  '
	d2=input('D2: ')
	print''
	
	#convert to float, just in casee
	float(d1)
	float(d2)
	#calculate D per the formula
	D=(d1+d2)
	float(D)
	

	print ' What is the Frequency in  GHZ? '
	print''
	F=input('GHz: ')
	float(F)
	radius= 72.2*math.sqrt((N*d1*d2)/(F*D))
	print ''
	print ' Your Fresnel radius in feet:  ',radius
	print''


#Calculating how high something has to be
def earth_bulge():
	
	#calculate hight to compensate for earth 
	print ' ========================================= '
	print ' Use if antennas are 7 or more miles apart '
	D=input(' What is the distance between the two antennas? \n ')
	float(D)
	print '' 
	H=(math.pow(D, 2)/float(8))
	float(H)
	print''
	ob=input( ' What is the height of the obstacle? \n ')
	print''
	F=input(' What is the frequency you are operating ')
	print''
	print ' Cacluating the height of the antenna with a 60% Fresnel Zone... '
	total_height= (ob+H+(43.3*math.sqrt(D/ float(4*F))))
	print 'The height of the antenna shoud be: ',total_height,'ft'	



#creating a menu to choose between the midpoit or any point
def fres_menu():
	loop=1
	while loop!=0:
		print' ======================================='
		print"Calculate the Fresnel zone"
		print''
		print' [1] Calculate at midpoint between two antennas '
		print' [2] Calculate at any point between two antennas ' 
		print' [3] Calulate Height of antenna in feet '
		print' [0] Back '
	
		opt=input(' ')
	
		if opt==1:
			print''
			fresnel_midpoint()

		elif opt==2:
			print''
			fresnel_anypoint()
		elif opt==3:
			print''
			earth_bulge()
		elif opt==0:
			break

#main menu
def main_menu():
		print' ========================================================'
		print 'Calculating dBm or mW with log or use Rule of 10s or 3s'
		print ''
		opt= ''
		while (opt != 0):
			print ' [1] Calculate dBm choose '
       		 	print ' [2] Calculate mW  choose '
			print ' [3] Rules of 3s and 10s '
        		print ' [4] Fresnel Zone '	
			print ' [0] Quit '
			print ''
			print 
			opt  = input('What would you like to do?\n')
			
			if ( opt == 1):
				solve_dBm()
					
			
			elif (opt ==2):
				solve_mW()
				
			
			elif (opt == 3):
				ruleofrules()
								
	
			elif (opt==4):
				fres_menu()
			

			elif opt==0:

				break




#To run just this file uncomment out the below function

#main_menu()
