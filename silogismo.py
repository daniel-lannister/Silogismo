def testarsilogismo(v=[]):
	cont = 1
	for i in range(len(v)-1):
		cont = 0
		if (v[i]!="-"):
			for j in range(len(v)-1):
				if (v[j]!="-"):
					if (v[i]==v[j]):
						cont=cont+1
						if (i==j+1 or i==j-1):
							return False
					if (j==len(v)):
						if (cont!=1):
							return False
	return True

def validarargumento(s=[],v=[]):
	r = []
	i=0
	for i in range (0,len(s)-4):
		if (s[i]=="-"):
			if(s[i+1]==1 and s[i+2]==4):
				print("epa")
				r.extend(["-",1,2,3,4])
			if(s[i+1]==1 and s[i+2]==5):
				r.extend(["-",0,1,3])
			if(s[i+1]==2 and s[i+2]==4):
				r.extend(["-",0])
			if(s[i+1]==2 and s[i+2]==5):
				r.extend(["-",2,4])
			if(s[i+1]==3 and s[i+2]==4):
				r.extend(["-",2,4])
			if(s[i+1]==3 and s[i+2]==5):
				r.extend(["-",0])
			
	i = 0
	
	for j in range (0,(len(r)-1)):
		if (r[j]==0):
			print(" não pertence ")
		if (r[j]==1):
			print (" interceção ")
		if (r[j]==2):
			print(" pertence ")
		if (r[j]==3):
			print(" é pertencido ")
		if (r[j]==4):
			print(" igualdade ")
	
	
	
				
			
		
			
        
        
menu = True
silogismo = []
simbolos = []
r = []
prop=0
aux=0
cont=0

while menu:
	print ("1 = Fazer proposição")
	print ("2 = Fazer conclusão")
	print ("3 = Sair")
	opcao=int(input())
	
	if opcao == 1:
		silogismo.append("-")
		simbolos.append("-")
		print ("1 - Algum, 2 - Nenhum, 3 - Todo")
		simbolos.append(int(input()))
		simbolos.append("-")
		print ("(insira uma variável)")
		silogismo.append((input()))
		print ("4 - é, 5 - não é")
		simbolos.append(int(input()))
		print ("(insira uma variável)")
		silogismo.append((input()))
	if opcao == 2:
		silogismo.append("-")
		simbolos.append("-")
		print ("1 - Algum, 2 - Nenhum, 3 - Todo")
		simbolos.append(int(input()))
		simbolos.append("-")
		print ("insira uma variável")
		silogismo.append((input()))
		print ("4 - é, 5 - não é")
		simbolos.append(int(input()))
		print ("(insira uma variável)")
		silogismo.append((input()))
		z=testarsilogismo(silogismo)
		if (z == False):
			print ("Esse não é um silogismo")
		if (z==True):
			print ("Esse é um silogismo")
			validarargumento(simbolos, silogismo)
			
		menu = False
		
		
		
		
			
