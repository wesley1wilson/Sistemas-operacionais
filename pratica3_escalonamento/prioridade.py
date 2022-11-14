import time
with open('arquivo.txt', encoding="utf8") as f:
    contents = f.read()
p1 = contents.split("\n")
matriz = []
for i in p1:
    matriz.append(i.split(";"))
for i in matriz:
    i[1] = int(i[1])
    i[2] = int(i[2])

quantum = 10
p5 = []
p4 = []
p3 = []
p2 = []
p1 = []
for a in range(len(matriz)):
    if matriz[a][2] == 5:
        p5.append(matriz[a])
    elif matriz[a][2] == 4:
        p4.append(matriz[a])
    elif matriz[a][2] == 3:
        p3.append(matriz[a])
    elif matriz[a][2] == 2:
        p2.append(matriz[a])
    elif matriz[a][2] == 1:
        p1.append(matriz[a])

terminados5 = 0
while terminados5 != len(p5):
    for a in range(len(p5)):
        if p5[a][1] > 0:
            print("Processo {} está executando.".format(p5[a][0]))
            p5[a][1] -= quantum
            time.sleep(4)
            print("Processo {} executado.".format(p5[a][0]))
            if p5[a][1] <= 0:
                print("Tempo restante: 0.\n")
                print("\nProcesso {} terminado.\n".format(p5[a][0]))
                terminados5 += 1
            else:
                print("Tempo restante: {}.\n".format(p5[a][1]))

terminados4 = 0
while terminados4 != len(p4):
    for a in range(len(p4)):
        if p4[a][1] > 0:
            print("Processo {} está executando.".format(p4[a][0]))
            p4[a][1] -= quantum
            time.sleep(4)
            print("Processo {} executado.".format(p4[a][0]))
            if p4[a][1] <= 0:
                print("Tempo restante: 0.\n")
                print("Processo {} terminado.\n".format(p4[a][0]))
                terminados4 += 1
            else:
                print("Tempo restante: {}.\n".format(p4[a][1]))

terminados3 = 0
while terminados3 != len(p3):
    for a in range(len(p3)):
        if p3[a][1] > 0:
            print("Processo {} está executando.".format(p3[a][0]))
            p3[a][1] -= quantum
            time.sleep(4)
            print("Processo {} executado.".format(p3[a][0]))
            if p3[a][1] <= 0:
                print("Tempo restante: 0.\n")
                print("Processo {} terminado.\n".format(p3[a][0]))
                terminados3 += 1
            else:
                print("Tempo restante: {}.\n".format(p3[a][1]))

terminados2 = 0
while terminados2 != len(p2):
    for a in range(len(p2)):
        if p2[a][1] > 0:
            print("Processo {} está executando.".format(p2[a][0]))
            p2[a][1] -= quantum
            time.sleep(4)
            print("Processo {} executado.".format(p2[a][0]))
            if p2[a][1] <= 0:
                print("Tempo restante: 0.\n")
                print("Processo {} terminado.\n".format(p2[a][0]))
                terminados2 += 1
            else:
                print("Tempo restante: {}.\n".format(p2[a][1]))

terminados1 = 0
while terminados1 != len(p1):
    for a in range(len(p1)):
        if p1[a][1] > 0:
            print("Processo {} está executando.".format(p1[a][0]))
            p1[a][1] -= quantum
            time.sleep(4)
            print("Processo {} executado.".format(p1[a][0]))
            if p1[a][1] <= 0:
                print("Tempo restante: 0.\n")
                print("Processo {} terminado.\n".format(p1[a][0]))
                terminados1 += 1
            else:
                print("Tempo restante: {}.\n".format(p1[a][1]))