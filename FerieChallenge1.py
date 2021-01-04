import webbrowser

Url = "https://poocoo.pl/scrabble-slowa-z-liter/"
Input = ""
def isPalindrome(wordToCheck):
    global text 
    text = (''.join([char for char in wordToCheck if char.isalpha()])).casefold()
    output = ''.join(reversed(text))
    output = output.casefold()
    output1 = ''.join(list(reversed(wordToCheck)))
    print("Odwrocone wyrazenie: " + output1)
    webbrowser.open(Url+text) 
    if output == text:
        return 1
    else:
        return 0

while (Input != "esc"):
    print("Podaj wyraz do sprawdzenia: ")
    x = " nie jest palindromem"
    Input = input() 
    if isPalindrome(Input):
        x = " jest palindromem" 
    else:
        x = " nie jest palindromem"
    print("Wyraz " + Input + x)
    



    


