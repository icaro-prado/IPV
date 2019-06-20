
inteiro = input('DIGITE UM INTEIRO DE 4 DÍGITOS\n')

if (len(inteiro)==4):
    inteiro=int(inteiro)
    
    primeiro_d = inteiro//1000
    segundo_d = inteiro%1000//100
    terceiro_d = inteiro%1000%100//10
    quarto_d = inteiro%1000%100%10

    primeiro_d = (primeiro_d+6)%10
    segundo_d = (segundo_d+6)%10
    terceiro_d = (terceiro_d+6)%10
    quarto_d = (quarto_d+6)%10

    backup_primeiro_d = primeiro_d
    primeiro_d = terceiro_d
    backup_segundo_d = segundo_d
    segundo_d = quarto_d
    terceiro_d = backup_primeiro_d
    quarto_d = backup_segundo_d

    a="O INTEIRO CRIPTOGRAFADO FICA :"
    print(a ,primeiro_d , segundo_d, terceiro_d, quarto_d)

    inteiro = int(input('\nDIGITE UM INTEIRO DE 4 DÍGITOS PARA DESCRIPTOGRAFAR :\n'))

    primeiro_d = inteiro//1000
    segundo_d = inteiro%1000//100
    terceiro_d = inteiro%1000%100//10
    quarto_d = inteiro%1000%100%10

    backup_primeiro_d = primeiro_d
    primeiro_d = terceiro_d
    backup_segundo_d = segundo_d
    segundo_d = quarto_d
    terceiro_d = backup_primeiro_d
    quarto_d = backup_segundo_d

    primeiro_d = ((primeiro_d+10)-6)%10
    segundo_d = ((segundo_d+10)-6)%10
    terceiro_d = ((terceiro_d+10)-6)%10
    quarto_d = ((quarto_d+10)-6)%10

    a="O INTEIRO DESCRIPTOGRAFADO FICA :"
    print(a ,primeiro_d , segundo_d, terceiro_d, quarto_d)

else:
    print('Inteiro inválido!')


