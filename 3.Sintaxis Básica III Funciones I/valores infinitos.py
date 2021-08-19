#Con el asterisco nos hace una matriz de todos los valores que le podemos pasar
def mostra_personas(*personas):
    for persona in personas:
        print("Esta persona es",persona)


mostra_personas("Nick","Jack","Dan","King","Smiley")