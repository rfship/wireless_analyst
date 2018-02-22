#! /usr/bin/env python


import rfmath

import wireless_network


def main():
	print'==============================================================='
	print'option 1 Calculate dBm or mW'
	print'option 2 Kismet.netxml file parse'
	print''
	opt=input('What would you like to do?  ')
	if opt==1:
		rfmath.main_menu()
	if opt==2:
		wireless_network.kismet_main()





main()
