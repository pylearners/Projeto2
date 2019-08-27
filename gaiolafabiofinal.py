hab = int(input('O animal está habituado? \n "Sim" ditige (1) se "Não" (2)?:  ')) 
if (hab==1):
    print('\n===================INICIANDO PROTOCOLO===================') 
else:
    print('=======Você deve habituar o animal=======')

if hab ==1:
    aproximacao = float(input('Animal deve se aproximar da barra <30cm\n (Simulando LEITURA DA DISTÂNCIA) \n Digite a distância(cm):' ))
    if (aproximacao<30):
        print('\n=======Aproximação CONFIRMADA, liberando recompensa!========\n')
    else:
        print('\n=======Teste Cancelado=======')
if aproximacao:
    barra = int(input('Barra deve ser pressionada pelo animal 20x\n Ditige número de repetições: '))
    if (barra>=20):
        print('\n=======ANIMAL PASSOU PAR PRÓXIMA ETAPA=======\n') 
    else:
        print('\n=======Teste incompleto=======\n')
if barra >=20:
    print('BARRA deve ser pressionada de acordo com emitido do SOM.\nPara libera recompensa Som Grave(1) = Barra(1) , Som Agudo(2) = Barra(2)')
    som = int(input("\nQual som será emitido? 1 ou 2?"))
    barra = int(input("Animal deve pressionar barra 1 ou 2.\n"))
    if (som==1 and barra==1):
        print ("=======Recompensa liberada=======")
    elif (som==2 and barra==2):
        print ("=======Recompensa liberada=======")
    else:
        print("======Recompensa não liberada======")

    

