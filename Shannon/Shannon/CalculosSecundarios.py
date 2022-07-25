def verificar_palindromo(palabra):
    lista=list(palabra)
    lista_inversa=lista[::-1]

    if lista==lista_inversa:
        return True
    else:
        return False

resultado=verificar_palindromo("LAMINAANIMAL")
print(resultado)