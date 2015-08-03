@@ -0,0 +1,149 @@
# def binarify(num): 
#   """convert positive integer to base 2"""  
#   powers=[]
#   for i in range(0,20):
# 	powers.append(2**i)
#   for i in range(0, len(powers)-1):
# 	if number > powers[i] and number <powers[i+1]:
# 	    myindex=i
#   digits=[]
#   for i in range (0, myindex+1)[::-1]
# 	  digit=str(number/(2**i))
#       remainder=number%(2**i)
# 	  number=remainder
# 	  digits.append(digit)
#   return''.join(digits)
# print binarify(159)
# 
# 
# #def binarify(num): 
#  # """convert positive integer to base 2"""
#   #if num<=0: return '0'
#   #digits = []
#   #return ''.join(digits)
# 
# 
# 
# 
# 
# def int_to_base(num, base):
#   """convert positive integer to a string in any base"""
# 
#  powers=[]
#   for i in range(0,20):
# 	powers.append(base**i)
#   for i in range(0, len(powers)-1):
# 	if num > powers[i] and num < powers[i+1]:
# 	    myindex=i
#   digits=[]
#   for i in range (0, myindex+1)[::-1]:
# 	  digit=str(num/(base**i))
#       remainder=num%(base**i)
# 	  num=remainder
# 	  digits.append(digit)
#   return''.join(digits)
# print int_to_base(23,2)


# def base_to_int(string, base):
#   """take a string-formatted number and its base and return the base-10 integer"""
#   length=len(string)
#   result=0
#   for i in length:
#   	result+=int(i)*base**(length-1)
#   	
#   	length-=1
#   return result
#   
# print base_to_int("1001",2)
#   
# 
# def flexibase_add(str1, str2, base1, base2):
#    """add two numbers of different bases and return the sum"""
#    length1=len(str1)
#    result1=0
#    for i in str1:
#    		result1+=int(i)*base1**(length1-1)
#    		length1-=1
#    
#    length2 = len(str2)
#    result2=0
#    for i in str2:
#    		result2+=int(i)*base2**(length2-1)
#    		length2-=1
#   
#    return result1+result2
#    
# print flexibase_add("1001", "55", 2, 10)
# 

def flexibase_multiply(str1, str2, base1, base2):
   """add two numbers of different bases and return the sum"""
   length1=len(str1)
   result1=0
   for i in str1:
   		result1+=int(i)*base1**(length1-1)
   		length1-=1
   
   length2 = len(str2)
   result2=0
   for i in str2:
   		result2+=int(i)*base2**(length2-1)
   		length2-=1
  
   return result1*result2
   
print flexibase_add("1001", "55", 2, 10)
# 


# def romanify(num):
#   """given an integer, return the Roman numeral version"""
#   one="I"
#   five="V"
#   ten="X"
#   fifty="L"
#   hundred="C"
#   fivehundred="D"
#   thousand="M"
#   if num==1: return "I"
#   elif num==5: return "V"
#   elif num==10: return "X"
#   elif num==50: return "L"
#   elif num==100: return "C"
#   elif num==500: return "D"
#   elif num==1000: return "M"
if num<4:
	print one*num
elif num %10==1
#string=str(num)
#length=len(string)
#ones=[,I,II,III, IV, V, VI, VII, VIII, IX]
#tens=[,X, XX, XXX, XL, L, LX, LXX, LXXX, XC]
#hundreds=[,C, CX, CXX, CXXX, CXL, CL, CLX, CLXX, CLXXX, CLXC, CC, C]
#thousands=[,M,MC,MCC, MCCC, MCD, MD, MDC, MDCC, MDCCC, MDCD
# 
#   #result = ""
#   #return result
#   
#   
#   
# # Copyright (c) 2014 Matt Dickenson
# # 
# # Permission is hereby granted, free of charge, to any person obtaining a copy
# # of this software and associated documentation files (the "Software"), to deal
# # in the Software without restriction, including without limitation the rights
# # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the Software is
# # furnished to do so, subject to the following conditions:
# # 
# # The above copyright notice and this permission notice shall be included in all
# # copies or substantial portions of the Software.
# # 
# # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# # SOFTWARE.
