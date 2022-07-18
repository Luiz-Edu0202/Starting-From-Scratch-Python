print('Programa que te diz o que você escreveu é')
test = input('Digite algo: ')
if(test.isalpha() == True):{print('O que você digitou é alfabético')}
if(test.isalnum() == True):{print('O que você digitou é um numero')}
if(test.islower() == True):{print('O que você digitou está tudo em minusculo')}
if(test.isupper() == True):{print('O que você digitou está tudo em maiusculo')}
