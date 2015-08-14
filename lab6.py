#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers
def intersect(a, b):
     return list(set(a) & set(b))

def missing(a,b):
	return list(set(a) & set(b))

def devisor(n1, n2):
	n1list=[]
	n2list=[]
	bothlist=[]
	for i in range(1,n1):
		if n1%i==0:
			n1list.append(i)
	for i in range(1,n2):
		if n2%i==0:
			n2list.append(i)
	bothlist=intersect(n1list, n2list)		
	print n1list
	print n2list
	print bothlist
	print bothlist[-1]	


def devisor(n1, n2):



  
 #Exercise 2
#Write a function that returns prime numbers less than 121

def primer(n1):
	prime_list=[]
	nonprime_list=[]
	total_num=[]
	for i in range(1,n1):
		first_devisor=[]
		for j in range(1,i):
			if i%j==0:
				first_devisor.append(i)
				if len(first_devisor)==2:
					nonprime_list.append(i)
	total_num=range(1,n1)
	set1=set(total_num)
	set2=set(nonprime_list)
	primelist=set1-set2
					
	#print nonprime_list	
	prime_list=list(primelist)
	print prime_list[1:]			

primer(122)		


						
		
			

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html 

def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
      
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print source, helper, target


def fib(n):
  if n<=1:
    return n
  return fib(n-1) + fib(n-2)
  
for i in range(40):
print "{0} : {1}".format(i, fib(i))
