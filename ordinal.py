#Write a function that takes an integer as an input and returns a script with the ordinal number
#For example, for 1, it should give "1st"
#Write a test for your function


def ordinal_type(i):
	try:
		if i%1==0:
			nmb=str(i)																
			if nmb[-2:]=="11":
				return str(nmb)+"th"
			elif nmb[-2:]=="12":
				return str(nmb)+"th"				
			elif nmb[-2:]=="13":
				return str(nmb)+"th"
			elif nmb[-2:]=="14":
				return str(nmb)+"th"
			elif nmb[-2:]=="15":
				return str(nmb)+"th"
			elif nmb[-2:]=="16":
				return str(nmb)+"th"
			elif nmb[-2:]=="17":
				return str(nmb)+"th"
			elif nmb[-2:]=="18":
				return str(nmb)+"th"
			elif nmb[-2:]=="19":
				return str(nmb)+"th"	
			elif nmb[-1]=="0":
				return str(nmb)+"th"
			elif nmb[-1]=="1":
				return str(nmb)+"st"
			elif nmb[-1]=="2":
				return str(nmb)+"nd"
			elif nmb[-1]=="3":
				return str(nmb)+"rd"
			elif nmb[-1]=="4":
				return str(nmb)+"th"
			elif nmb[-1]=="5":
				return str(nmb)+"th"
			elif nmb[-1]=="6":
				return str(nmb)+"th"	
			elif nmb[-1]=="7":
				return str(nmb)+"th"	
			elif nmb[-1]=="8":
				return str(nmb)+"th"	
			elif nmb[-1]=="9":
				return str(nmb)+"th"																											
		else:
			return "Put in an integer."
	except:
		return "Enter an integer"
	finally:
		print "This is a function."
			
		
# print ordinal_type(221)
# print ordinal_type(228)
# print ordinal_type(12)
# print ordinal_type("hello")
print ordinal_type(2.6)	
