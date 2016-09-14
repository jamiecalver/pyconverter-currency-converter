print("Pounds, Euro Converter")

ep = input("If you would like to convert POUNDS TO EURO type 'pound'. If you would like to convert EURO TO POUND type 'euro': ")

if (ep == 'pound'):
	pound = float(input("Pounds: £"))
	print("£", pound, "-> €:")
	print('%.2f' % (pound*1.18))

elif (ep == 'euro'):
	euro = float(input("Euros: €"))
	print("€", euro, "-> £:")
	print('%.2f' % (euro*1.18))
	
input("Press <enter> to Quit")	
