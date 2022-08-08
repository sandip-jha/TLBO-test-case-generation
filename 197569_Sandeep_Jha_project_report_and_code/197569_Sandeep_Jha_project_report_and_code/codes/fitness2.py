from bd import BranchDistance

class Fitness:

	def __init__(self):
		self.branch_distance=BranchDistance()

	def calcFitnessVal(self,a,b,c,t_path):

		match=0 
		ch=''
		if a+b<c or b+c<a or a+c<b or a<0 or b<0 or c<0 :
			ch='A' 
		if a==b:
			match=match+1 
		if a==c:
			match=match+2 
		if b==c:
			match=match+3 
		if match==0:
			ch='B' 
		elif match==1:
			ch='C' 
		elif match==2:
			ch='D' 
		elif match==3:
			ch='E' 
		else:
			ch='F' 

		b_d,a_l=[0.0,0.0]
	 
		if ch== 'A': 	
			b_d,a_l=self.branch_distance.bdl_A(a,b,c,t_path,match)
						
		elif ch== 'B': 	
			b_d,a_l=self.branch_distance.bdl_B(a,b,c,t_path,match)
		elif ch== 'C':	
			b_d,a_l=self.branch_distance.bdl_C(a,b,c,t_path,match)
						
		elif ch== 'D':	
			b_d,a_l=self.branch_distance.bdl_D(a,b,c,t_path,match)
						 
		elif ch== 'E':	
			b_d,a_l=self.branch_distance.bdl_E(a,b,c,t_path,match)
						 
		elif ch== 'F':	
			b_d,a_l=self.branch_distance.bdl_F(a,b,c,t_path,match)
						 
		else:
			b_d,a_l=[0.0,0.0]

		fitness_val = a_l
		return fitness_val 
