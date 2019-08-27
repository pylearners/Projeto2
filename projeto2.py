habituado= str(input('O animal está habituado?'))
if (habituado== 'sim'):
    print('Iniciar protoloco de aproximação')
elif (habituado== 'nao'):
    print('Habituar o animal')

habituado2 = str(input('O animal está habituado?'))
if (habituado2 == 'sim'):
    print('Iniciar protoloco de aproximação')



from random import randint 

aproximacao= randint(1, 100)
print('O animal está a',aproximacao,'cm da barra.' )
if(aproximacao< 30):
    print('Liberar 0,5ml de recompensa')
else:
    print('Animal precisa se aproximar da barra.')
animal=str(input('Animal se aproximou da barra?'))
if(animal=='sim'):
    print('Animal está aprendendo a tarefa!!')
tbarra = int(input('Quantas vezes o animal tocou na barra?'))
if(tbarra >= 20):
    print('Animal passou para a proxima fase')
else:
    print('Animal permanece na mesma fase')
    print('Voltar ao treinamento.')

print('Fase de discriminação de sons')
print('Quando animal ouvir som 1 deve tocar na barra esquerda, quando ouvir som 2 deve tocar na barra direita.')
from random import randint
som1= randint(0,1)
barraesq= randint(0,1)

if(som1 == barraesq):
    print('Animal ouviu som 1 e tocou na barra esquerda.')
    print('0,5 ml de recomenpensa liberada')
else:
    print('Animal não realizou a tarefa corretamente')
    print('Recompensa não liberada')

som2= randint(0,1)
barradir= randint(0,1)

if(som2 == barradir):
    print('Animal ouviu som 2 e tocou na barra direta.')
    print('0,5 ml de recomenpensa liberada')
else:
    print('Animal não realizou a tarefa corretamente')
    print('Recompensa não liberada')

print('Análise de performance do animal')
print('Animal precisa realizar a tarefa pelo menos 50 vezes em no máximo 30 minutos.')
proximafase= randint(48,100)
minutos= randint(25,32)
if(proximafase>=50 and minutos<30):
    print('Animal realizou a tarefa corretamente e passou para próxima fase')
else:
    print('Animal não realizou a tarefa corretamente')
    print('Continue o treinamento do animal.')

animal2=str(input('Animal consegiu concluir o treinamento?'))
if(animal2=='sim'):
    print('Animal preparado para próxima fase!!')
else:
    print('Animal ainda precisa de treinamento.')

print('Fim do programa!')

