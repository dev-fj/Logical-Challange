#%%


# 1️ Desafio Classificador de nível de Herói

# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões

# ## Objetivo

# # Crie uma variável para armazenar o nome e a quantidade de experiência (XP) 
# de um herói, depois utilize uma estrutura de decisão para apresentar alguma 
# das mensagens abaixo:

# Se XP for menor do que 1.000 = Ferro
# Se XP for entre 1.001 e 2.000 = Bronze
# Se XP for entre 2.001 e 5.000 = Prata
# Se XP for entre 5.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000= Imortal
# Se XP for maior ou igual a 10.001 = Radiante

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói de nome **{nome}** está no nível de **{nivel}**"

#%%


hero = input("Please hero, type your glorious name!")
hero = hero.upper()
xp = input(f"Now Glorious {hero} !! type how much knowledge you've already achieved! ")
rank = None

def xp_hero(xp1):
    if xp1 <= 1000:
        rank = "iron"
        return rank 

    elif 1001 <= xp1 <= 2000:
        rank = "Bronze"
        return rank
    
    elif 2001 <= xp1 <= 5000:
        rank = "silver"
        return rank 
    
    elif 5001 <= xp1 <= 7000:
        rank = "gold"
        return rank 
    
    elif 7001 <= xp1 <= 8000:
        rank = "platinum"
        return rank 
    
    elif 8001 <= xp1 <= 9000:
        rank = "Ascending"
        return rank 
    
    elif 9001 <= xp1 <= 10000:
        rank = "Imortal"
        return rank 
    
    elif xp1 >= 10001:
        rank = "Radiant"
        return rank 

# print(hero)
# print(xp1)


try:
    xp1 = int(xp)
    result = xp_hero(xp1)
    print(f"The glorious **{hero}** has the **{result}** status in this realm!!".upper()
    )

except(ValueError):
    print("We had a problem hero! Try to put a number on your knowledge level".upper())
# %%
