def testartautologia(v=[]):
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

def validarargumento(v=[],s=[]):
	ini = 0
	for i in range (ini,len(s)-4):
		if (s[i]=="-"):
			if(s[i+1]==1 and s[i+2]==4):
				relacoes.extend(["-",2,3,4])
			if(s[i+1]==1 and s[i+2]==5):
				relacoes.extend(["-",1,2])
			if(s[i+1]==2 and s[i+2]==4):
				relacoes.extend(["-",1])
			if(s[i+1]==2 and s[i+2]==5):
				relacoes.extend(["-",3,4])
			if(s[i+1]==3 and s[i+2]==4):
				relacoes.extend(["-",3,4])
			if(s[i+1]==3 and s[i+2]==5):
				relacoes.extend(["-",1])
	
				
			
		
			
        
        
menu = True
tautologia = []
simbolos = []
relacoes = []
prop=0
aux=0
cont=0

while menu:
	print ("1 = Fazer proposição")
	print ("2 = Fazer conclusão")
	print ("3 = Sair")
	opcao=int(input())
	
	if opcao == 1:
		tautologia.append("-")
		simbolos.append("-")
		print ("1 - Algum, 2 - Nenhum, 3 - Todo")
		simbolos.append(int(input()))
		simbolos.append("-")
		print ("(insira uma variável)")
		tautologia.append((input()))
		print ("4 - é, 5 - não é")
		simbolos.append(int(input()))
		print ("(insira uma variável)")
		tautologia.append((input()))
	if opcao == 2:
		tautologia.append("-")
		simbolos.append("-")
		print ("1 - Algum, 2 - Nenhum, 3 - Todo")
		simbolos.append(int(input()))
		simbolos.append("-")
		print ("insira uma variável")
		tautologia.append((input()))
		print ("4 - é, 5 - não é")
		simbolos.append(int(input()))
		print ("(insira uma variável)")
		tautologia.append((input()))
		z=testartautologia(tautologia)
		if (z == False):
			print ("Essa não é tautologia")
		if (z==True):
			print ("Essa é uma tautologia")
		
		
			
