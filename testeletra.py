texto = str(input("Digite um texto aqui \n"))
#Váriavel para contabilizar a quantidade de A no texto
contador_a = 0
#Verificar a quantidade de A no texto
for x in texto:
    if x.lower() == "a" :
        contador_a += 1
if contador_a == 0 :
    print("No texto foi observado a inexistência da letra ‘a’ nele")
elif contador_a == 1 :
    print(f"A letra ‘a’ apareceu apenas {contador_a} vez no texto digitado durante a execução do programa")
else :    
    print(f"A letra ‘a’ apareceu {contador_a} vezes no texto digitado durante a execução do programa")
