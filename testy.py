import kalkulator

# W przypadku nie przejścia poprawnie przez wszystkie testy otrzymamy błąd AssertionError

# ---------------------TEST 1--------------------------
# (GIVEN) biorąc liczby a,b typu int lub float (gdzie b != 0) i znak '+', '-', '*' lub '/'
# (WHEN) kiedy wywolujemy funkcję kalkulator(a, b, znak)
# (THEN) wówczas otrzymujemy wartość typu int lub float

wartosci_testowe = [2, 4, 0.5, 1.4, -3, -7.0]
znaki = ['+', '-', '*', '/']
for a in wartosci_testowe:
    for b in wartosci_testowe:
        for znak in znaki:
            assert (type(kalkulator.kalkulator(a, b, znak))) == int \
                   or (type(kalkulator.kalkulator(a, b, znak)) == float)

# ---------------------TEST 2--------------------------
# (GIVEN) biorąc liczbę a typu int lub float, b = 0 oraz znak = '/'
# (WHEN) kiedy wywolujemy funkcję kalkulator(a, b, znak)
# (THEN) wówczas otrzymujemy wartość 'error' (bo nie można dzielić przez zero!)

assert kalkulator.kalkulator(1.5, 0, '/') == 'error'
assert kalkulator.kalkulator(0, 0, '/') == 'error'

# ---------------------TEST 3--------------------------
# (GIVEN) biorąc za a, b i znak niepoprawne wartości
# (WHEN) kiedy wywołujemy funkcję kalkulator(a, b, znak)
# (THEN) wówczas otrzymujemy wartość 'error'

assert kalkulator.kalkulator(1, 2, 'WITAM') == 'error'
assert kalkulator.kalkulator('2', '3', '/') == 'error'
assert kalkulator.kalkulator('a', 'b', '+') == 'error'
assert kalkulator.kalkulator('a', 3, '*') == 'error'
assert kalkulator.kalkulator({'a': 1}, {'b': 2}, '+') == 'error'
assert kalkulator.kalkulator((1,2), (3), '+') == 'error'

print("Funkcja kalkulator pomyślnie przeszła przez testy!")