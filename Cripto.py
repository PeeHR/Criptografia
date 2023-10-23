def cripto (frase):
    tradutor = ""
    for letra in frase:
        if letra in "Aa":
            tradutor = tradutor + "#"
        elif letra in "Bb":
            tradutor = tradutor + "$"
        elif letra in "Cc":
            tradutor = tradutor + "%"
        elif letra in "Dd":
            tradutor = tradutor + "!"
        elif letra in "Mm":
            tradutor = tradutor + "<" 
        elif letra in "Pp":
            tradutor = tradutor + ">"
        elif letra in "Ss":
            tradutor = tradutor + "^"
        elif letra in "Vv":
            tradutor = tradutor + "~"
        elif letra in "Ii":
            tradutor = tradutor + "*" 
        elif letra in "Nn":
            tradutor = tradutor + "2"
        elif letra in "Rr":
            tradutor = tradutor + "§" 

        else:
            tradutor = tradutor + letra

    return tradutor
        

print(cripto(input("Digite uma frase: ")))
             
