class BranchDistance:
	def bdl_A(self,tp):
		branch_distance_value=0.0
		approach_level_value=0.0

		if tp=='A':
			branch_distance_value=0.0
			approach_level_value=0.0
		
		elif tp=='B':
			branch_distance_value=0.0
			approach_level_value=4.0
		
		elif tp=='C':
			branch_distance_value=0.0
			approach_level_value=6.0
		
		elif tp=='D':
			branch_distance_value=0.0
			approach_level_value=7.0

		elif tp=='E':
			branch_distance_value=0.0
			approach_level_value=8.0
	
		else:
			branch_distance_value=0.0
			approach_level_value=9.0

		return [branch_distance_value,approach_level_value]

	def bdl_B(self,a,b,c, tp, match):
		branch_distance_value=0.0
		approach_level_value=0.0
		if tp=='A':
			branch_distance_value=0.0
			approach_level_value=4.0

		elif tp=='B':
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr7 = abs(b-c)+0.1
			pr9= match+0.1
			branch_distance_value = pr3+pr5+pr7+pr9
			approach_level_value = 0.0

		elif tp=='C':
			pr3 = abs(a-b)+0.1
			pr7 = abs(b-c)+0.1
			pr9 = match+.01
			branch_distance_value = pr3 + pr7 + pr9
			approach_level_value = 2.0

		elif tp=='D':
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr9 = match+.01
			branch_distance_value = pr3 + pr5 + pr9
			approach_level_value = 3.0
			
		
		elif tp=='E':
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr7 = abs(b-c)+0.1
			branch_distance_value = pr3+pr5+pr7
			approach_level_value = 1.0

		elif tp=='F':
			pr3 = abs(a-b)+0.1
			branch_distance_value = pr3
			approach_level_value = 6.0

		return [branch_distance_value,approach_level_value]

	def bdl_C(self,a,b,c, tp, match):

		branch_distance_value=0.0
		approach_level_value=0.0
		if tp=='A' :
			branch_distance_value=0.0
			approach_level_value=6.0
		
		elif tp=='B' :
			pr3 = abs(a-b)+0.1
			pr7 = abs(b-c)+0.1
			pr9 = match+0.1
			branch_distance_value = pr3 + pr7 + pr9
			approach_level_value = 2.0

		
		elif tp=='C' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr7 = abs(b-c)+0.1
			pr9 = match+0.1
			pr13 = (match-1)+0.1
			branch_distance_value = pr3 + pr5 + pr7 + pr9 + pr13
			approach_level_value = 0.0
		
		elif tp=='D' :
			pr3 = abs(a-b)+0.1
			pr9 = match+0.1
			pr13 = (match-1)+0.1
			branch_distance_value = pr3 + pr9 +pr13
			approach_level_value = 2.0
		
		elif tp=='E' :
			pr3 = abs(a-b)+0.1
			pr7 = abs(b-c)+0.1
			pr13 = (match-1)+0.1
			branch_distance_value = pr3 + pr7 + pr13
			approach_level_value = 3.0
		
		else:
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr13 = (match-1)+0.1
			branch_distance_value = pr3 + pr5 + pr13
			approach_level_value = 4.0

		return [branch_distance_value,approach_level_value]
		

	def bdl_D(self,a,b,c, tp, match):

		branch_distance_value=0.0
		approach_level_value=0.0
		if tp=='A' :
			branch_distance_value=0.0
			approach_level_value=7.0
		
		elif tp=='B' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr9 = match+.01
			branch_distance_value = pr3 + pr5 + pr9
			approach_level_value = 3.0
		
		elif tp=='C' :
			pr3 = abs(a-b)+0.1
			pr9 = match+0.1
			pr13 = (match-1)+0.1
			branch_distance_value = pr3 + pr9 +pr13
			approach_level_value = 2.0
		
		elif tp=='D' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr7 = abs(b-c)+0.1
			pr9 = match+0.1
			pr13 = (match-1)+0.1
			pr17 = (match-2)+0.1
			branch_distance_value = pr3 + pr5 + pr7 + pr9 + pr13 + pr17
			approach_level_value = 0.0

		
		elif tp=='E' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr13 = (match-1)+0.1
			pr17 = (match-2)+0.1
			branch_distance_value = pr3 + pr5 + pr13 + pr17
			approach_level_value = 3.0
		
		else :
			pr3 = abs(a-b)+0.1
			pr7 = abs(b-c)+0.1
			pr13 = (match-1)+0.1
			pr17 = (match-2)+0.1
			branch_distance_value = pr3 + pr7 + pr13 + pr17
			approach_level_value = 3.0

		return [branch_distance_value,approach_level_value]
			

	def bdl_E(self,a,b,c, tp, match):

		branch_distance_value=0.0
		approach_level_value=0.0
		if tp=='A' :
			branch_distance_value=0.0
			approach_level_value=8.0
		
		elif tp=='B' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr7 = abs(b-c)+0.1
			branch_distance_value = pr3+pr5+pr7
			approach_level_value = 1.0
		
		elif tp=='C' :
			pr3 = abs(a-b)+0.1
			pr7 = abs(b-c)+0.1
			pr13 = (match-1)+0.1
			branch_distance_value = pr3 + pr7 + pr13
			approach_level_value = 3.0
		
		elif tp=='D' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr13 = (match-1)+0.1
			pr17 = (match-2)+0.1
			branch_distance_value = pr3 + pr5 + pr13 + pr17
			approach_level_value = 3.0
		
		elif tp=='E' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr7 = abs(b-c)+0.1
			pr9 = match+0.1
			pr13 = (match-1)+0.1
			pr17 = (match-2)+0.1
			pr21 = (match-3)+0.1
			branch_distance_value = pr3 + pr5 + pr7 + pr9 + pr13 + pr17 + pr21
			approach_level_value = 0.0

		
		else :
			pr3 = abs(a-b)+0.1
			pr9 = match+0.1
			branch_distance_value = pr3+pr9
			approach_level_value = 3.0

		return [branch_distance_value,approach_level_value]
	

	def bdl_F(self,a,b,c, tp, match):

		branch_distance_value=0.0
		approach_level_value=0.0
		if tp=='A' :
			branch_distance_value=0.0
			approach_level_value=9.0
		
		elif tp=='B' :
			pr3 = abs(a-b)+0.1
			branch_distance_value = pr3
			approach_level_value = 6.0

		
		elif tp=='C' :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr13 = (match-1)+0.1
			branch_distance_value = pr3 + pr5 + pr13
			approach_level_value = 4.0
		
		elif tp=='D' :
			pr3 = abs(a-b)+0.1
			pr7 = abs(b-c)+0.1
			pr13 = (match-1)+0.1
			pr17 = (match-2)+0.1
			branch_distance_value = pr3 + pr7 + pr13 + pr17
			approach_level_value = 3.0

		
		elif tp=='E' :
			pr3 = abs(a-b)+0.1
			pr9 = match+0.1
			branch_distance_value = pr3+pr9
			approach_level_value = 3.0
		
		else :
			pr3 = abs(a-b)+0.1
			pr5 = abs(a-c)+0.1
			pr7 = abs(b-c)+0.1
			pr9 = match+0.1
			pr13 = (match-1)+0.1
			pr17 = (match-2)+0.1
			pr21 = (match-3)+0.1
			branch_distance_value = pr3 + pr5 + pr7 + pr9 + pr13 + pr17 + pr21
			approach_level_value = 0.0

		return [branch_distance_value,approach_level_value]