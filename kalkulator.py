def dodawanie(x, y):
    try:
        return x + y
    except:
        return "error"


def odejmowanie(x, y):
    try:
        return x - y
    except:
        return "error"


def mnozenie(x, y):
    try:
        return x * y
    except:
        return "error"


def dzielenie(x, y):
    try:
        return x / y
    except:
        return "error"


def kalkulator(x, y, znak):
    """
    Funkcja kalkulator() zwraca wartość typu 'int' lub 'float' dla prawidłowych danych
    w przeciwnym przypadku zwraca wartość 'error'
    """

    #Jeżeli x,y nie są liczbami zwracamy 'error'
    if not ((type(x) == int or type(x) == float) and (type(y) == int or type(y) == float)):
        return "error"

    if znak == '+':
        return dodawanie(x, y)
    if znak == '-':
        return odejmowanie(x, y)
    if znak == '*':
        return mnozenie(x, y)
    if znak == '/':
        return dzielenie(x, y)

    #Jeżeli funkcja nie zwróciła do tej pory żadnej wartości, niech teraz zwróci 'error'
    return "error"

# Funkcja wyswietlająca wynik działania arytmetycznego
def wyswietl_wynik(x, y, znak):
    print(f"{x} {znak} {y} = {kalkulator(x, y, znak)}")