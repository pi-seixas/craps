# -*- coding: utf-8 -*-
import random

fichas = True

fichas = 50

print ("Você possui 50 fichas")

a = input ("Você quer APOSTAR ou SAIR DO JOGO?")

while a == "APOSTAR":

    print ("Você possui {} fichas".format(fichas))

    tipo_de_aposta = input ("Escolha qual o tipo de aposta você quer fazer: PASS LINE BET, FIELD, ANY CRPS ou TWELVE ")
    valor = int(input ("Qual valor você deseja apostar? "))

    if tipo_de_aposta == "PASS LINE BET" or "pass line bet":
        print ("FASE COME OUT")
        d = random.randint(1,6)
        e = random.randint(1,6)
        soma = d+e
        print ("Os dados lançados apontaram", d ,"e", e)
        if soma == 7 or soma == 11:
            fichas = fichas + valor
            print ("Você ganhou! Agora tem {} fichas a mais.".format(valor))
            print ("Agora você possui {} fichas".format(fichas))
            a = input ("Você quer APOSTAR ou SAIR DO JOGO?")
        elif soma == 2 or soma == 3 or soma == 12:
            fichas = fichas - valor
            print ("Craps! Você perdeu. Agora tem {} fichas a menos.".format(valor))
            print ("Agora você possui {} fichas".format(fichas))
            if fichas > 0:
                a = input ("Você quer APOSTAR ou SAIR DO JOGO?")
            else:
                print ("Você não possui mais fichas. Fim da rodada.")
        else:
            print ("FASE POINT")
            f = random.randint(1,6)
            g = random.randint(1,6)
            while f+g!=7 and f+g!=soma:
                print ("Os dados apontaram", f, "e", g)
                print ("A soma não é 7 nem Point")
                print ("Você permanece na FASE POINT")
                f = random.randint(1,6)
                g = random.randint(1,6)
            if f + g == soma:
                print ("Os dados apontaram", f, "e", g)
                fichas = fichas + valor
                print ("A soma dos dados resultou no Point! Você ganhou {} fichas.".format(valor))
                print ("Agora você possui {} fichas".format(fichas))
                a = input ("Você quer APOSTAR ou SAIR DO JOGO?")
            elif f + g == 7:
                print ("Os dados apontaram", f, "e", g)
                print ("A soma dos dados resultou em 7! Você perdeu tudo!")
                print ("Fim da rodada.")
