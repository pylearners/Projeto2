inicio= str(input('O animal está habituado?'))
if (inicio== 'sim'):
    habituado=True
else:
    print('Habituar o animal')

print('Iniciar protoloco de aproximação')

from random import randint 

aproximacao= randint(1,35)
if (aproximacao < 30):
    print('O animal está a' ,aproximacao, 'cm da barra.')
    print('Liberar 0,5ml de recompensa' )
    print('Animal está aprendendo a tarefa!!')
else:
    print('Animal precisa se aproximar da barra!')
    
aproximacao2= randint(20,50)
if (aproximacao2 > 20):
   fase2= True
   print ('Animal se aproximou do sensor mais de 20 vezes e passou para próxima fase!')

print('Fase de discriminação de sons')
print('Quando animal ouvir som 1 deve tocar na barra esquerda, quando ouvir som 2 deve tocar na barra direita.')

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
proximafase= randint(50,100)
minutos= randint(30,32)
if(proximafase>=50 and minutos<30):
    print('Animal realizou a tarefa corretamente e passou para próxima fase')

animal2=str(input('Animal consegiu concluir o treinamento?'))
if(animal2=='sim'):
    print('Animal preparado para próxima fase!!')
else:
    print('Animal ainda precisa de treinamento.')

print('Fim do programa!')