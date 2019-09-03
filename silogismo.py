def testartautologia(v=[]):
    cont = 0
    for cont in range(len(v)-1):
        cont=cont+1
        
        
menu = True
tautologia = []
prop=None
aux=0

while menu:
	print ("1 = Fazer proposição")
	print ("2 = Fazer conclusão")
	print ("3 = Sair")
	opcao=int(input())
	
	if opcao == 1:
		print ("1 - Algum, 2 - Nenhum, 3 - Todo")
		prop=int(input())
		tautologia.insert(cont, prop)
		print ("(insira uma variável)")
		tautologia.insert(cont, (input()))
		cont=cont+1
		print ("1 - é, 2 - não é")
		prop=int(input())
		tautologia.insert(cont, prop)
		cont=cont+1
		print ("(insira uma variável)")
		tautologia.insert(cont, (input()))
	if opcao == 2:
	    print ("1 - Algum, 2 - Nenhum, 3 - Todo")
		prop=(int(input()))
		tautologia.insert(cont, prop)
		print ("(insira uma variável)")
		tautologia.insert(cont, (input()))
		print ("1 - é, 2 - não é")
		prop=int(input())
		tautologia.insert(cont, prop)
		cont=cont+1
		print ("(insira uma variável)")
		tautologia.insert(cont, (input()))
		
		for cont in range (length(tautologia), 0):
			if tautologia[cont] >= 1 or tautologia[cont] <= 3:
				if tautologia[cont+1] == tautologia[cont+3]:
					print ("Não é tautologia")
				for cont1 in range (cont, 0):
					if tautologia[cont] >= 1 or tautologia[cont] <= 3:
						if tautologia[cont1+1]
		
			
			
