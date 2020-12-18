itens = [['1- Alface americano','2- Alface crespa','3- Alho poró','4- Capim santo','5- Cebola','6- Cebolinha','7- Coentro','8- Couve folha','9- Chinguezay (acelga chinesa)','10- Espinafre','11- Hortelã','12- Salsinha','13- Rúcula'],['1- Banana pacovan (unidade)','2- Cana(saquinho)','3- Laranja comum (4 Unidades)','4- Laranja mimo (4 Unidades)','5- Maracujá (kg)'],['1- Batata doce (kg)','2- Cará (kg)','3- Cenoura(molho)','4- Jerimum (kg)','5- Macaxeira (kg)','6- Rabanete(molho)','7- Quiabo (15 Un)'],['1- Fava seca (Kg)','2- Mel italiana (250 g)','3- Mel italiana (500 g)','4- Mel no favo (450 g)','5- Ovos de capoeira (un)','6- Polpa de cajá (400g)','7- Própolis (20 ml)','8- Pão sem trigo (grande)','9- Pão com trigo (grande)','10- Pão com trigo (pequeno)','11- Bolo(sem trigo)','12- Bolinho de bacia(c/trigo)','13- Mini pizza (un)','14- Pizza brotinho','15- Bolacha com trigo (saquinho)','16- Sucos sem açucar (200 ml)','17- Sucos com açucar (200 ml)','18- Sucos com ou sem açucar (1 l)','19- Refeições congeladas (500 g)','20- Refeições congeladas (750 g)','21-Hambúrguer de ora-pro-nóbis, (6 Un)','22- Molhos prontos','23- Massa artesanal lasanha ou taglatelle'],['1- Pepita de girassol','2- Homus de grão de bico com paprika','3- Bisnaga Maionese de pepita de girassol (250 ml)','4- Pimentas ao mel de engenho','5- Confit de tomatinho, pimenta, pimentão ou berinjela','6- Geleia de tomate com pimenta/abacaxi/manga','7- Capotana Siciliana'],['1- Quiche de macaxeira c/ alho poró','2- Quiche de macaxeira c/ tomate seco','3- Sanduíche sem glúten de ricota','4- Sanduíche sem glúten de caponata Siciliana','5- Sanduíche sem glúten de ragu'],['1- Empada de falso camarão','2- Empada de antepasto de berinjela','3- Empada de tofu com cebola caramelizada','4- Pãozinhos de inhames recheados']]
prices = [[2.50,2.50,2.00,2.50,3.00,2.50,2.50,2.50,3.00,3.00,2.50,2.50,2.50],[0.25,2.00,2.00,7.00,2.00],[4.00,5.00,3.00,5.00,4.00,2.50,2.00],[12.00,20.00,35.00,25.00,1.00,6.00,16.00,13.00,13.00,7.00,10.00,2.00,3.00,5.00,5.00,3.00,3.00,10.00,12.00,15.00,12.00,10.00,12.00],[5.00,5.00,10.00,15.00,15.00,13.00,13.00],[5.00,5.00,6.00,6.00,6.00],[5.00,5.00,5.00,5.00]]
sectors = ['1- folhas e hortaliças  o molho','2- frutas','3- raízes, tubérculos, legumes e afins','4- outros','5- Pastinhas, antepastos e geleias','6- Lanches (sem trigo)','7- Lanches (com trigo)']
cart = list()
quantities = list()
total = 0
invoice = str()
g = 0

print("**********************************************************")
print('==========================================================')
print('-------------------- Welcome! ----------------------------')
print("==========================================================")
print('Escolha um dos setores que deseja realizar as suas compras')
print("**********************************************************")
print('**********************************************************')
option = 1
while option != 0 :
    print("========== SETORES ===========")
    print("******************************")
    print("********** 0- SAIR ***********")
    for i in range(0,len(sectors)) :
        print(sectors[i])
    print('*** 8- FINALIZAR A COMPRA ***')

    print("*****************************")
    option = int(input("Digite o número do setor: "))
    print("*****************************")
    if option != 0 and option < 8 :
        i = option -1
        for j in range(0,len(prices[i])) :
            print(itens[i][j],prices[i][j])
        
        options = 1
        while options != 0 :
            print(" ")
            options = int(input("Número do item ou tecle 0 para voltar: "))
            print("**********************")
            h = options -1
            if options != 0 :
                quantities = (int(input("Quantidade do produto: ")))
                print("*********************")
                cart.append(f'{itens[i][h]:<25}{prices[i][h]:<7}{quantities:<5}{prices[i][h]*quantities}\n')
                total += prices[i][h]*quantities
                g += 1
                print("Valor total da compra: ",total)

    elif option != 0 and option == 8 :
        print(" ")
        name = str(input('Cliente, digite seu nome: '))
        print(" ")
        address = str(input("Cliente, digite seu endereço: "))
        print(" ")
        payment = str(input("FORMAS DE PAGAMENTO: /***Dinheiro***/***Debito***/***Credito***/: "))
        option = 0

invoice += str("=========================================\n")
invoice += str('*****************************************\n')
invoice += str("-----------   *NOTA FISCAL*   -----------\n")
invoice += str("*****************************************\n")
invoice += str(f'NOME               PREÇO  QUANTID  TOTAL\n')
invoice += str('*****************************************\n')
invoice += str("=========================================\n")


for i in cart:
    invoice += i
invoice += str("*----*-----*-----*-----*-----*-----*----*\n")
invoice += str(f'TOTAL DO PAGAMENTO{total:>30}\n')
invoice += str(f'NOME: {name}\n')
invoice += str(f'ENDEREÇO: {address}\n')
invoice += str(f'PAGAMENTO: {payment}\n')
print(invoice)   

arquivo = open(f'{name}invoice.txt', "x+", encoding= 'utf8')
arquivo.write(invoice)