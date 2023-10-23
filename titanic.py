import csv
titanic = []

def carrega_dados():
 with open('train.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for linha in csv_reader:
        titanic.append(linha)
        

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*len(texto))

def estatistica_sexo():
    titulo("Estatistica por sexo")
      
    mas = 0
    fem = 0
    for linha in titanic:
          if linha["Sex"] == "male":
              mas += 1
          elif linha["Sex"] == "female":
              fem += 1 
              
    print(f"Total de Passageiros: {len(titanic)}")
    print(f"Homens: {mas}")
    print(f"Mulheres: {fem}")    
      
    #outra forma(1)
    num_mas = [linha["Sex"] for linha in titanic].count("male")
    num_fem = [linha["Sex"] for linha in titanic].count("female")
    print(f"Total de Passageiros: {len(titanic)}")
    print(f"Homens: {num_mas}")
    print(f"Mulheres: {num_fem}")
    
    num_mas_sob = len([linha for linha in titanic if linha["Sex"] == "male" and linha["Survived"] == "1"])
    num_mas_mor = len([linha for linha in titanic if linha["Sex"] == "male" and linha["Survived"] == "0"])
    
    num_fem_sob = len([linha for linha in titanic if linha["Sex"] == "female" and linha["Survived"] == "1"])
    num_fem_mor = len([linha for linha in titanic if linha["Sex"] == "female" and linha["Survived"] == "0"])    
    
    print(f" - Sobreviventes homens: {num_mas_sob}")
    print(f" - Mortos homens: {num_mas_mor}")
    print(f" - Sobreviventes mulheres: {num_mas_sob}")
    print(f" - Mortos mulheres: {num_mas_mor}") 


def estatistica_idade():
    
    pass

def agrupar_portos():
    pass

carrega_dados()
while True:
    titulo("Passageiros do Titanic")    
    print("1. Estatistica por sexo")
    print("2. Estatistica por idade")
    print("3. Portos de embarque")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        estatistica_sexo()
    elif opcao == 2:
        estatistica_idade()
    elif opcao == 3:
        agrupar_portos()
    else:
        break