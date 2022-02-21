# Zadanie 1
# Stwórz dwie zmienne `a` i `b` i przypisz do nich różne wartości. Napisz program który zamienia wartości
# zmiennych miejscami.

# a = 10
# b = 20
# a,b= b,a
# print("a:",a)
# print("b:",b)

# Zadanie 2
# Napisz program który przyjmie trzy liczby i wypisze średnią z nich.

# def f2(a,b,c):
#     sr= (a+b+c)/3
#     return(sr)
#
# print(f2(1,5,8))

# Zadanie 3
# Kupiłeś Bitcoiny i zastanawiasz się ile zarobisz. Napisz program, który:
# - przyjmie wartość bitcoina w momencie zakupu;
# - przyjmie procent wzrostu (lub spadku) wyrażony jako liczba z przedziału (-1, 1);
# - wypisze aktualna wartość twoich bitcoinów i ile zyskałeś (straciłeś).

# def bit():
#     p = float(input("Podaj wkład własny: "))
#     i = float(input("Podaj procent wzrostu w przedziale (-1, 1): "))
#     while i >=1 or i <=-1:
#         print("Błędny przedział wartości wzrostu:")
#         i = float(input("Podaj procent wzrostu w przedziale (-1, 1): "))
#     else:
#         zysk = i * p
#         kwota = zysk + p
#     print("Zyskałes: {} zł".format(zysk))
#     print("Aktualna wartość bitcoinów Adasia: {} zł".format(kwota))
#     return("Wpłać kolejne pieniązki")
# print(bit())

# Zadanie 4
# Napisz program który przyjmuje rozmiary działki i zwraca jej pole.

# def pole ():
#     a = float(input("Podaj długość krótszego boku:"))
#     b = float(input("Podaj długość dłuższego boku:"))
#     p = a * b
#     return("Pole działki o wymiarach {} na {} wynosi: {}".format(a,b,p))
# print(pole())

# Zadanie 5
# Świetnie Ci idzie zarabianie na bitcoinach. Chcesz teraz zainwestować w inne kryptowaluty. Napisz program, który
# przyjmie:
# - ilość twojej gotówki;
# - cenę bitcoina, etherum i litecoina;
# - i zwróci ile za swoją gotówkę możesz kupić bitcoinów, etherum i litecoinów.

# def bit2():
#     a = float(input("Ile gotówki chcesz zainwestować: "))
#     b = float(input("Podaj kurs Bitcoina: "))
#     e = float(input("Podaj kurs Etherum: "))
#     l = float(input("Podaj kirs Litecoinów:"))
#     kursy = [b,e,l]
#     ilosc = list(map(lambda x: a/x, kursy))
#     return("Za {} zł możesz kupić {} Bitcoinów, {}Etherum, {}Litecoinów".format(a, str(ilosc[0]), str(ilosc[1]), str(ilosc[2])))
# print(bit2())

# Zadanie 6
# Chcesz kupić laptopa z Chin, ale możliwe, że Urząd Celny doliczy Ci cło. Napisz program, który:
# - przyjmie cenę laptopa
# - procent cła
# - i wypisze ile będziesz miał faktycznie do zapłaty.

# def clo():
#     price = float(input('Podaj cenę laptopa: '))
#     duty = float(input('Podaj wysokość cła w %:'))
#     while price == (''):
#         return("Podaj cenę laptopa ")
#     else:
#         while duty == (''):
#             return('Podaj wysokość cła w %:')
#         else:
#             duty_n = duty/100
#             price2 = price + (price * duty_n)
#             return('Cena z cłem od komputera wartego {} zł, wynosi {}'.format(price,price2))
# print(clo())

# Zadanie 7
# W firmie w której pracujesz, premia jest wyliczana na podstawie Twojego stażu pracy. Za każdy przepracowany
# rok pracy otrzymujesz ekstra 250zł. Napisz program, który przyjmie:
# - podstawę twojego wynagrodzenia;
# - staż pracy;
# - wypisz jakie dostaniesz wynagrodzenie wraz z premią.

# def salary():
#     base = float(input('Podaj wysokość podstawy: '))
#     sen = float(input('Podaj staż pracy: '))
#     salary_p= base + (50*sen)
#     return('Wynagrodzenie z premią wynosi {}'.format(salary_p))
# print(salary())

# Zadanie 8
# Napisz program który zwróci cyfrę jedności podanej liczby.

# def unit():
#     n = input('Podaj liczbę zmiennoprzecinkową:')
#     u = n.split('.')
#     return(u[0])
# print(unit())

# Zadanie 1
# Napisz program który wczyta wyrazy wczytane przez użytkownika i wypisze te które kończą się na 'a'.

# def word_a():
#     words = input('Podaj słowa rozdzielone przecinkami:')
#     lista_s = list(words.split(','))
#     word_list=[]
#     for word in lista_s:
#         if word[-1] == 'a':
#             word_list.append(word)
#     return('Lista słów, które kończą się na literę "a" to {} '.format(word_list))
# print(word_a())

# Zadanie 2
# Napisz program który wczyta zdanie napisane przez użytkownika i przetłumaczy je na Pig Latin.
# Pig Latin - gra językowa oparta na języku angielskim.
# Polega na przesunięciu pierwszej litery na koniec wyrazu i dodaniu końcówki "ay".

# def pig():
#     sent = input('Wpisz zdanie: ')
#     div_sent= list(sent.split())
#     new_sent=(" ")
#     for el in div_sent:
#         el1 = str(el[1:])+str(el[0])+"py"
#         new_sent= new_sent +" " + el1
#     return(print('Twoje zdanie w języku Pig Latin to:{}'.format(new_sent)))
# print(pig())

# Zadanie 3
# Z podanych przez użytknownika wyrazów wypisz takie, które są dłuższe niż 5.

# def f3():
#     words = input("Wprowadź zbiór słów:")
#     div_words = list(words.split())
#     word5=[]
#     for word in div_words:
#          if len(word)>5:
#              word5.append(word)
#     return('Słowa dłuższe od 5 to {}'.format(word5))
# print(f3())

# Zadanie 4
# Napisz program który z wyrazów podanych przez użytkownika wypisze te które są napisane wielkimi literami.

# def big():
#     a= input("Podaj wyrazy oddzielony spacjami: ")
#     div_a= a.split()
#     zb = []
#     for word in div_a:
#         zb.append(word) if word.isupper() else None
#     return('Słowa napisane wielkimi literami to:{}'.format(zb))
# print(big())

# Zadanie 5
# Napisz program który z wyrazów podanych przez użytkownika wypisze palindromy.

# def pali():
#     words = input('Podaj listę słów, które chcesz przeszukać: ').split()
#     empty=[]
#     for word in words:
#         if word == word[::-1]:
#             empty.append(word)
#     return('Słowa, które są palindromami to:{}'.format(empty))
# print(pali())

# Zadanie 6
# Napisz program który przyjmie wyrazy od użytkownika i wypisze je, jednak jeżeli wyraz ma parzystą ilość liter
# to wypisz go wielkimi literami.

# def lett():
#     a = input('Podaj wyrazy:').split()
#     for word in a:
#         print(word.upper(), end=" ") if len(word)%2 == 0 else print(word, end=" ")
# print(lett())

# Zadanie 7
# Napisz program który znajdzie minimum i maksimum w liście liczb podanej przez użytkownika.

# def mm():
#     number =list(input('Podaj liczby oddzielone spacją: ').split())
#     a =max(number)
#     b= min(number)
#     return('Wartość max to:{}, wartość min to {}'.format(a, b))
# print(mm())

# Zadanie 8
# Napisz program który działa jak `str.rfind` - znajduje pierwsze wystąpienie wzorca w stringu ale od prawej strony.