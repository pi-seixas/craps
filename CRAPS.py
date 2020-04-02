# -*- coding: utf-8 -*-
import random

fichas = True

fichas = 50

print ("Você possui 50 fichas")

a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")

while a == "APOSTAR":

    print ("Você possui {} fichas".format(fichas))

    tipo_de_aposta = input ("Escolha qual o tipo de aposta você quer fazer: PASS LINE BET, FIELD, ANY CRPS ou TWELVE ")
    valor = int(input ("Qual valor você deseja apostar? "))

    if tipo_de_aposta == "PASS LINE BET":
        print ("FASE COME OUT")
        d = random.randint(1,6)
        e = random.randint(1,6)
        soma = d+e
        print ("Os dados lançados apontaram", d ,"e", e)
        if soma == 7 or soma == 11:
            fichas = fichas + valor
            print ("Você ganhou! Agora tem {} fichas a mais.".format(valor))
            print ("Agora você possui {} fichas".format(fichas))
            a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
        elif soma == 2 or soma == 3 or soma == 12:
            fichas = fichas - valor
            print ("Craps! Você perdeu. Agora tem {} fichas a menos.".format(valor))
            print ("Agora você possui {} fichas".format(fichas))
            if fichas > 0:
                a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
            else:
                print ("Você não possui mais fichas. Fim da rodada.")
                break
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
                x = input("Aperte enter para lançar novamente ")
                if x==" " or "":
                    continue
            if f + g == soma:
                print ("Os dados apontaram", f, "e", g)
                fichas = fichas + valor
                print ("A soma dos dados resultou no Point! Você ganhou {} fichas.".format(valor))
                print ("Agora você possui {} fichas".format(fichas))
                a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
            elif f + g == 7:
                print ("Os dados apontaram", f, "e", g)
                print ("A soma dos dados resultou em 7! Você perdeu tudo!")
                print ("Fim da rodada.")
                if fichas > 0:
                    a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
                else:
                    print ("Você não possui mais fichas. Fim da rodada.")
                    break
                
    if tipo_de_aposta == "FIELD":
        print ("FASE COME OUT")
        h = random.randint(1,6)
        i = random.randint(1,6)
        if h+i==5 or h+i==6 or h+i==7 or h+i==8:
            print ("Os dados lançados apontaram", h, 'e', i)
            print ("Você perdeu tudo!")
            print ("Fim da rodada.")
            if fichas > 0:
                a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
            else:
                print ("Você não possui mais fichas. Fim da rodada.")
                break
        if h+i==3 or h+i==4 or h+i==9 or h+i==10 or h+i==11:
            print ("Os dados lançados apontaram", h, "e", i)
            fichas = fichas + valor
            print ("Você ganhou {} fichas".format(valor))
            print ("Agora você possui {} fichas".format(fichas))
            a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
        if h+i==2:
            print ("Os dados lançados apontaram", h, "e", i)
            fichas = fichas + 2*valor
            print ("Você ganhou {} fichas".format(2*valor))
            print ("Agora você possui {} fichas".format(fichas))
            a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
        if h+i==12:
            print ("Os dados lançados apontaram", h, "e", i)
            fichas = fichas + 3*valor
            print ("Você ganhou {} fichas".format(3*valor))
            print ("Agora você possui {} fichas".format(fichas))
            a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")

    if tipo_de_aposta == "ANY CRAPS":
        print ("FASE COME OUT")
        j = random.randint(1,6)
        k = random.randint(1,6)
        if j+k==2 or j+k==3 or j+k==12:
            print ("Os dados lançados apontaram", j, "e", k)
            fichas = fichas + 7*valor
            print ("Você ganhou {} fichas".format(7*valor))
            print ("Agora você possui {} fichas".format(fichas))
            a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
        else:
            print ("Você perdeu a aposta!")
            fichas = fichas - valor
            print ("Você perdeu {} fichas".format(valor))
            print ("Agora você possui {} fichas".format(fichas))
            if fichas > 0:
                a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
            else:
                print ("Você não possui mais fichas. Fim da rodada.")
                break

    if tipo_de_aposta == "TWELVE":
        print ("FASE COME OUT")
        l = random.randint(1,6)
        m = random.randint(1,6)
        if l+m==12:
            print ("Os dados lançados apontaram", l, "e", m)
            fichas = fichas + 30*valor
            print ("Você ganhou {} fichas!".format(30*valor))
            print ("Agora você possui {} fichas.".format(fichas))
            a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
        if l+m!= 12:
            print ("Os dados lançados apontaram", l, "e", m)
            fichas = fichas - valor
            print ("Você perdeu {} fichas!".format(valor))
            print ("Agora você possui {} fichas.".format(fichas))
            if fichas > 0:
                a = input ("Você quer APOSTAR ou SAIR DO JOGO? ")
            else:
                print ("Você não possui mais fichas. Fim da rodada.")
                break

if a == "SAIR DO JOGO":
   print ("Fim de jogo.")



