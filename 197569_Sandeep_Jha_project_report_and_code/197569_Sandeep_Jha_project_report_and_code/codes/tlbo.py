import random
from fitness import Fitness
import time
begin=time.time()
def calDiffMean(l,mean):
	val = 0.5*(l-mean)
	return val



def print_guide():
	print('****************************************************************************************')
	print('\t\tProgram Guide')
	print('\t\tpath A : Not a Triangle')
	print('\t\tpath B : Scalene Triangle')
	print('\t\tpath C : Isosceles Triangle with First side = Second Side')
	print('\t\tpath D : Isosceles Triangle with First side = Third Side')
	print('\t\tpath E : Isosceles Triangle with Second Side = Third Side')
	print('\t\tpath F : Equilateral Triangle')
	print('****************************************************************************************\n')


def which_triangle(a,b,c):
	if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
		return 'a'

	elif a==b and a==c and b==c:
		return 'f'

	elif a!=b and b!=c and a!=c:
		return 'b'

	elif a==b:
		return 'c'

	elif a==c:
		return 'd'

	elif b==c:
		return 'e'


def count_triangle(a,b,c,d,e,f):
	print()
	print('Triangle with path A '+str(a))
	print('Triangle with path B '+str(b))
	print('Triangle with path C '+str(c))
	print('Triangle with path D '+str(d))
	print('Triangle with path E '+str(e))
	print('Triangle with path F '+str(f))



def main():
	print_guide()

	
	print("Give the number of inputs you want to generate")
	x=int(input())
	print("\n***number of inputs generated are : "+str(x))

	t_path=input("Enter the Target Path : A, B, C, D, E or F : ")
	t_path=t_path.upper()
	if t_path not in ['A','B','C','D','E','F']:
		print("invalid input")	
		return
	f=open("input.txt",'r+')
	f.truncate(0)
	
	sa=0.0
	sb=0.0
	sc=0.0
	t=x
	min_fit_val=99999999
	l1=0
	l2=0
	l3=0
	input_list=[]
	index=0

	fitness=Fitness()

	path_a=0
	path_b=0
	path_c=0
	path_d=0
	path_e=0
	path_f=0

	# Input Generation Phase
	print('**************************** Initially Generated Inputs *********************************')
	while x:
		a = random.randint(1,2)
		b = random.randint(1,2) 
		c = random.randint(1,2) 

		if which_triangle(a,b,c)=='a':
			path_a+=1
		elif which_triangle(a,b,c)=='b':
			path_b+=1
		elif which_triangle(a,b,c)=='c':
			path_c+=1
		elif which_triangle(a,b,c)=='d':
			path_d+=1
		elif which_triangle(a,b,c)=='e':
			path_e+=1
		elif which_triangle(a,b,c)=='f':
			path_f+=1

		sa+=a
		sb+=b
		sc+=c    
		fitness_val =round(fitness.calcFitnessVal(a,b,c,t_path),3)
		input_list.append([a,b,c,fitness_val])
		#min_fit_val = fmin(min_fit_val,fitness_val)
		if min_fit_val>fitness_val:
		
			min_fit_val = fitness_val
			l1=a
			l2=b
			l3=c
		
		res = str(float(a))+ "	"+ str(float(b))+"	"+str(float(c))+"	"+str(float(fitness_val))
		print(res)
		f.write(res+'\n')
		res=""

		x=x-1
	print('\nInitial Test cases has Triangles with ')
	count_triangle(path_a,path_b,path_c,path_d,path_e,path_f)


	#Teacher Phase

	#Calculating Mean
	Ma=sa/t
	Mb=sb/t
	Mc=sc/t
	# print()
	# print('Mean Ma, Mb & Mc : '+str(Ma)+' '+str(Mb)+' '+str(Mc))
	# print('l1, l2, l3 : '+str(l1)+' '+str(l2)+' '+str(l3))
	# print('min_fit_val : '+str(min_fit_val))
	diffMeanA = calDiffMean(l1,Ma)
	diffMeanB = calDiffMean(l2,Mb)
	diffMeanC = calDiffMean(l3,Mc)
	#print(' value of diffMeanA, B, C : '+str(diffMeanA)+' '+str(diffMeanB)+' '+str(diffMeanC))

	L2=[]
	count=100
	# Open file to store final output
	tf = open("TeacherLearnerPhase.txt",'r+')
	tf.truncate(0)
	while count:
		

		# print()
		# print()

		#Finding index of Teacher so that in Learner Phase we can avoid the choosen Teacher
		for i in range(0,len(input_list),1):
		
			if input_list[i][0]==l1 and input_list[i][1]==l2  and input_list[i][2]==l3 and input_list[i][3]==min_fit_val:
				index=i
				break

		L=[]
		for i in range(0,len(input_list)):
		
			newA = abs(round(input_list[i][0]+diffMeanA,3))
			newB = abs(round(input_list[i][1]+diffMeanB,3))
			newC = abs(round(input_list[i][2]+diffMeanC,3))
			val = round(fitness.calcFitnessVal(newA,newB,newC,t_path),3)
			if val<input_list[i][3]:
			
				L.append([newA,newB,newC,val])
			
			else:
			
				L.append([input_list[i][0],input_list[i][1],input_list[i][2],input_list[i][3]])

			# for j in L[i]:
			# 	print(j,end='\t')
			# print()
		input_list=L

		print('_______________________________________________________________________________________')
		print('After '+str(100-count+1)+'th Teacher Phase')
		for i in L:
			for j in i:
				print(str(j),end='\t')
			print()

		print()
		print()

		#LearnerPhase
		n=len(L)
		res=[[]]*n
		for i in range(0,len(L)):
		
			if i==index:
			
				res[index]=L[i]
				continue
			
			for j in range(0,len(L)):
			
				if i==j:
					continue
				if j!=index:
				
					if L[i][3]<L[j][3]:
					
						nA = abs(round(L[i][0]+0.5*(L[i][0]-L[j][0]),3))
						nB = abs(round(L[i][1]+0.5*(L[i][1]-L[j][1]),3))
						nC = abs(round(L[i][2]+0.5*(L[i][2]-L[j][2]),3))
						val = round(fitness.calcFitnessVal(nA,nB,nC,t_path),3)
						if val<L[i][3]:
							res[i] = [nA,nB,nC,val]
							L[i]=[nA,nB,nC,val]
						else:
							res[i] = L[i]

					
					else:
					
						nA = abs(round(L[j][0]+0.5*(L[j][0]-L[i][0]),3))
						nB = abs(round(L[j][1]+0.5*(L[j][1]-L[i][1]),3))
						nC = abs(round(L[j][2]+0.5*(L[j][2]-L[i][2]),3))
						val = round(fitness.calcFitnessVal(nA,nB,nC,t_path),3)
						if val<L[j][3]:
							res[i] = [nA,nB,nC,val]
							L[i]=[nA,nB,nC,val]
						else:
							res[i] = L[i]

		print('After '+str(100-count+1)+'th Learner Phase')
		for i in L:
			for j in i:
				print(str(j),end='\t')
			print()

		print()
		print()

		if (L2==L):
			print()
			print('***program converged after '+str(100-count)+' number of steps.')
			print('The initial input generated are stored in input.txt and final results are in TeacherLearnerPhase.txt')
			print()

			for i in range(0,len(res)):
		
				r = str(float(res[i][0]))+ "\t\t"+ str(float(res[i][1]))+"\t\t"+str(float(res[i][2]))+"\t\t"+str(float(res[i][3]))
				tf.write(r+'\n')
				r=""

			path_a=0
			path_b=0
			path_c=0
			path_d=0
			path_e=0
			path_f=0

			for i in range(len(L)):
				if which_triangle(L[i][0],L[i][1],L[i][2])=='a':
					path_a+=1

				elif which_triangle(L[i][0],L[i][1],L[i][2])=='b':
					path_b+=1

				elif which_triangle(L[i][0],L[i][1],L[i][2])=='c':
					path_c+=1

				elif which_triangle(L[i][0],L[i][1],L[i][2])=='d':
					path_d+=1

				elif which_triangle(L[i][0],L[i][1],L[i][2])=='e':
					path_e+=1

				elif which_triangle(L[i][0],L[i][1],L[i][2])=='f':
					path_f+=1


			print('\nFinal Test cases has Triangles with ')
			count_triangle(path_a,path_b,path_c,path_d,path_e,path_f)

			break

		L2=L

		count=count-1

	tf.close()
	f.close()
	return 0

main()

end=time.time()
print(f"Total runtime of the program is {end-begin}")
print()
print('**************************************************************************************')
print()
