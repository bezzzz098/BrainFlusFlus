inpud = list(input())
indeg = 0
kolom = 0
angka = list(map(int, input().split()))
Acounter = 0
def brain(n):
    global indeg
    global kolom
    data = []
    for i in range(10):
        data.append(0)
    def identifier(x):
        global indeg
        global kolom
        global Acounter
        global angka
        if x == "+":
            data[kolom] = data[kolom] + 1
        elif x == "-":
            data[kolom] = data[kolom] - 1
        elif x == ">":
            kolom += 1
        elif x == "<":
            kolom -= 1
        elif x == ":":
            print(data[kolom])
        elif x == ";":
            data[kolom] = angka[Acounter]
            Acounter += 1
        indeg += 1
    def loop(kolomlokal):
        global indeg
        global kolom
        if data[kolom]==0:
               while n[indeg]!="]":
                                indeg+=1
               indeg+=1
        limit=indeg
        while data[kolomlokal] > 0:
            if n[indeg] == "]":
                indeg = limit
            identifier(n[indeg])
            if n[indeg] == "[":
                yes = kolom
                loop(yes)
                if n[indeg] == "]":
                    indeg += 1
        if n[indeg] == "]":
            indeg += 1  
    while True:
        ai = n[indeg]
        if ai in ["+", "-", ">", "<", ":", "]", ";"]:
            identifier(ai)
        else:
            if ai == "[":
                if data[kolom]>0:
                        loop(kolom)
                else:
                        while n[indeg]!="]":
                                indeg+=1
                        indeg+=1              
        if indeg >= len(n):
            break
    print(data)
brain(inpud)
