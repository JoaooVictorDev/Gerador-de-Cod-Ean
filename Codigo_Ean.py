'''País de origem – 3 primeiros dígitos (No Brasil é 789 ou 790);
   Fabricante – 4, 5 ou 6 dígitos;(primeiros digitos do CPF ou CNPJ)
   Produto produzido – 3, 4 ou 5 dígitos;(INICIAR COM 00000)
   Dígito verificador – 1 dígito(ADICIONADO DEPOIS DA VALIDAÇÃO)'''

def gerar_codigos(cod,quant_anuncios):

    contador = -1
    lista_cod = []
    while contador <= quant_anuncios:
        cod += 1 
        lista_cod.append(cod)    
        contador += 1 
        if contador == quant_anuncios:
            break 

    return lista_cod

def validar_codigo(lista_cod):
    lista_cod_ean = []
    for cod in lista_cod:
        cod = str(cod)
        #Calculo de Validação do 13 digito
        soma =(int(cod[0])*1+int(cod[1])*3+
            int(cod[2])*1+int(cod[3])*3+
            int(cod[4])*1+int(cod[5])*3+
            int(cod[6])*1+int(cod[7])*3+
            int(cod[8])*1+int(cod[9])*3+
            int(cod[10])*1+int(cod[11])*3
            )
        #Encontrar o Multiplo de 10 mais proximo
        multiplo = 0
        while multiplo <= soma:
            multiplo = multiplo + 10
            if multiplo == soma:
                break
        #Digito Verificador
        digito13 = multiplo-soma
        codigo_ean = cod+str(digito13)
        lista_cod_ean.append(codigo_ean)

    return lista_cod_ean

print(validar_codigo(gerar_codigos(789262900026,27)))