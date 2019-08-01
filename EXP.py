#Exp.py
def Replace_EXP(Exp):
	NUM = list();TMP=''
	for i in Exp:
		if i == 'U': continue
		if i == '-' or i == '+' or i == '*' or i == '/': 
			NUM.append(TMP);NUM.append(i);TMP='';
			continue
		TMP+=str(i)
	NUM.append(TMP)
	return NUM
def Num_of_Bracket(Exp):
	cnt = 0
	for i in range(0,len(Exp)):
		if Exp[i] == ')': cnt+=1
	return cnt
def Replace_Bracket(Exp):
	first=0;last=0;NUM = list()
	Tmp_Exp=list();Exp = list(Exp)
	for i in range(0,Num_of_Bracket(Exp)): 
		first = Find_Left_Bracket(Exp)	   ### 알고리즘 -> 왼쪽부터 괄호를 찾아 나간다 맨 마지막에 위치한 왼쪽 괄호를 first변수에 저장
		last = Find_Right_Bracket(Exp)	   ### (만약 왼쪽 괄호의 위치가 오른쪽 괄호의 위치보다 크다면 오른쪽 괄호보다 작은 위치의 왼쪽 괄호 위치를 반환한다)
		Tmp_Res = Calculate(Exp[first:last]) 
		for j in range(first-1,last+1):
			Exp[j] = 'U'
		Exp.insert(first-1,Tmp_Res)
	return Calculate(Exp)
def Find_Left_Bracket(Exp):
	Out_cnt = 0
	for i in range(0,len(Exp)):
		if Out_cnt > 0: break
		if Exp[i] == ')': Out_cnt+=1
		if Exp[i] == '(': first = i
	return first+1
def Find_Right_Bracket(Exp):
	for i in range(len(Exp)-1,-1,-1):
		if Exp[i] == ')': last = i
	return last
def Find_NUM_Left(Exp,Loc): 
	for i in range(Loc,-1,-1):
		if Exp[i] != 'U' and Exp[i] != '+' and Exp[i] != '-' and Exp[i] != '/' and Exp[i] != '*':
 			return i
def Find_NUM_Right(Exp,Loc,LEN):
	for i in range(Loc,LEN+1):
		if Exp[i] != 'U' and Exp[i] != '+' and Exp[i] != '-' and Exp[i] != '/' and Exp[i] != '*':
			return i
def Find_FP_OP(Exp):
	cnt = 0
	for i in range(0,len(Exp)):
		if Exp[i] == '*': cnt+=1
		if Exp[i] == '/': cnt+=1
	return cnt
def Find_SP_OP(Exp):
	cnt = 0
	for i in range(0,len(Exp)):
		if Exp[i] == '+': cnt+=1
		if Exp[i] == '-': cnt+=1
	return cnt
def Calculate(Exp):
	Tmp_NUM = list();NUM = Replace_EXP(Exp)[::] ### 숫자들을 정렬(1,100,1000)
	FPv = Find_FP_OP(Exp) 			### 연산하고자 하는 연산자의 수를 센다
	for i in range(0,len(NUM)+FPv): 		### 곱하기와 나누기 연산 진행						
		if NUM[i] == '*':
			Tmp_Res = float(NUM[Find_NUM_Left(NUM,i)])*float(NUM[Find_NUM_Right(NUM,i,len(NUM))])
			for j in range(Find_NUM_Left(NUM,i),Find_NUM_Right(NUM,i,len(NUM))+1):
				NUM[j] = 'U'
			NUM.insert(i-1,Tmp_Res)
		elif NUM[i] == '/':
			Tmp_Res = float(NUM[Find_NUM_Left(NUM,i)])/float(NUM[Find_NUM_Right(NUM,i,len(NUM))])
			for j in range(Find_NUM_Left(NUM,i),Find_NUM_Right(NUM,i,len(NUM))+1):
				NUM[j] = 'U'
			NUM.insert(i-1,Tmp_Res)
	for i in NUM: 				### 리스트의 길이를 위해 대신 채운 u 값을 거를 차례
		if i == 'U': continue
		Tmp_NUM.append(i)
	SPv = Find_SP_OP(Tmp_NUM) 						### 연산하고자 하는 연산자의 수를 센다
	for i in range(0,len(Tmp_NUM)+SPv):			 ### 더하기와 빼기 연산 진행
		if Tmp_NUM[i] == '+':
			Tmp_Res = float(Tmp_NUM[Find_NUM_Left(Tmp_NUM,i)])+float(Tmp_NUM[Find_NUM_Right(Tmp_NUM,i,len(Tmp_NUM))])
			for j in range(Find_NUM_Left(Tmp_NUM,i),Find_NUM_Right(Tmp_NUM,i,len(Tmp_NUM))+1):
				Tmp_NUM[j] = 'U'
			Tmp_NUM.insert(i-1,Tmp_Res)
		elif Tmp_NUM[i] == '-':
			Tmp_Res = float(Tmp_NUM[Find_NUM_Left(Tmp_NUM,i)])-float(Tmp_NUM[Find_NUM_Right(Tmp_NUM,i,len(Tmp_NUM))])
			for j in range(Find_NUM_Left(Tmp_NUM,i),Find_NUM_Right(Tmp_NUM,i,len(Tmp_NUM))+1):
				Tmp_NUM[j] = 'U'
			Tmp_NUM.insert(i-1,Tmp_Res)
	for i in Tmp_NUM:
		if i == 'U': continue
		RESULT = i
	return RESULT
EXP = input("수식을 입력해주세요 : ")
print("RESULT : %.2lf"%Replace_Bracket(EXP))
	