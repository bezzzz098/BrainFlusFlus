print("program brainf*ck++ ....\"inspired by codeabbey\"")
print("build: 0.0.12")
print("owned by \"risal098 (bezzzz098)\" \n\n")
print("visit https://github.com/bezzzz098/BrainFlusFlus for further information")
print("pastikan telah membaca file README untuk dokumentasi dan cara penggunaan\n")
print("==================================================================\n\n")

while True:
    try:
        try:
            inpud = list(input("input brain++ code/symbols= "))
            indeg = 0
            kolom = 0
            angka = list(map(int, input("input numbers (if any)= ").split()))
        except:
            print("masukkan input dengan benar :)\n\n")
            continue
        print("\n\n")
        Acounter = 0
        def brain(n):
            selesai=1
            global indeg
            global kolom
            data = []
            for i in range(inpud.count(">")+20):
                data.append(0)
            def identifier(x):
                global indeg
                global kolom
                global Acounter
                global angka
                global selesai
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
                    #try:
                        data[kolom] = angka[Acounter]
                        Acounter += 1
                    #except:
                     #   selesai=0
                     #   print("input angka tidak sesuai tempat dengan \";\" atau angka tidak ditemukan.\npastikan anda telah menaruh input dengan benar :).\nJika anda mengalami kesulitan, bisa membaca ulang README atau hubungi owner")
                      #  return 0
           # if selesai==0:
              #  return 0
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
                    else:
                        
                        print("program eror karna input salah :)\n\n")
                        return 0
                        break
                if indeg >= len(n):
                    break
            print("hasil=")
            print(data)
            print("...........................................\n\n")
        brain(inpud)
    except:
        print("input angka tidak sesuai tempat dengan \";\" atau angka tidak ditemukan.\npastikan anda telah menaruh input dengan benar :).\nJika anda mengalami kesulitan, bisa membaca ulang README atau hubungi owner\n\n")
        

                      
        

