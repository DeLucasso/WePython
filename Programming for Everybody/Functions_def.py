def greet(lang):
    if lang == ("eng"):
        print("Hi!")
    elif lang == ("esp"):
        print("Ola!")
    elif lang == ("cz"):
        print("Ahoj!")
                
usr_input = input("Choose your language. Type 'eng' for English, 'esp' for Spanish or 'cz' for Czech")

greet(usr_input)
