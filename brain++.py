inpud = list(input())                  #to input brainF symbol/code
indeg = 0                                #code assistant to call item of input list [must see code below in brain funch to understand it]
kolom = 0                                #code assistant to call item of angka list [must see code below in brain funch to understand it]
angka = list(map(int, input().split()))  #to input brainF integer, [since its brain++ interpreter, now u can input integer number and change it to brainf symbol or put it in the cell [if there is no numbers in your brainF code just put random number or modify it if u want]
Acounter = 0                              #code assistant to count how many integer that already called {n-1} [this is important since its a brain++ ,to avoid int calling error] 
def brain(n):                             #a main function to do the work
    global indeg
    global kolom
    data = []                             #a list to contain brain++ cell
    for i in range(10):                   # to generate space in cell, you can change the value in range , automation space generator may be updated soon
        data.append(0)
    def identifier(x):                    # a function to identify brain++ symbol and execute command for each symbol
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
        elif x == ":":                           #this is the first brain++ statement that will print the current cell
            print(data[kolom])
        elif x == ";":                           #this is the second brain++ statement that will get/input the integer number in current cell [for example: traditional way, u need to type multiple or do looping to generate some numbers in certain cell, but brain++ u only need to input integer number and ";" symbol]
            data[kolom] = angka[Acounter]
            Acounter += 1
        indeg += 1
    def loop(kolomlokal):                      # third function to execute looping command when the symbol is "[" 
        global indeg
        global kolom
        if data[kolom]==0:                     #if the cell value of looping is zero, this statement will count the symbol in the looping symbol "[ /symbol ]" this way we can skip the loop 
               while n[indeg]!="]":
                                indeg+=1
               indeg+=1
        limit=indeg
        while data[kolomlokal] > 0:          # statement of looping command when the symbol is "[" and the cell of loop is not zero
            if n[indeg] == "]":
                indeg = limit
            identifier(n[indeg])
            if n[indeg] == "[":              #statement if there is/are nested loops in brainf*ck code/symbols
                yes = kolom
                loop(yes)
                if n[indeg] == "]":          #after the loop statement is done, this statement will be executed to skip the loop
                    indeg += 1
        if n[indeg] == "]":                   #the statement that only work in parent loop in nested loop (if any)
            indeg += 1  
    while True:                               #work as for loop but more accurate, this statement is for calling each symbol in brainf input
        ai = n[indeg]
        if ai in ["+", "-", ">", "<", ":", "]", ";"]:           #this code choose the symbol and do the identifier function to execute the command for each identifier
            identifier(ai)
        else:
            if ai == "[":
                if data[kolom]>0:                 #as long as the ceil of loop is not zero, this statement will do the loop function
                        loop(kolom)
                else:
                        while n[indeg]!="]":          #this code will skip the loop if the cell is zero
                                indeg+=1
                        indeg+=1              
        if indeg >= len(n):
            break
    print(data)
brain(inpud)
