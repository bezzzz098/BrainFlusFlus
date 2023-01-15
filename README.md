'# BrainFlusFlus 
newest version (0.0.15)
this is a code for brainF*ck interpreter with python programing language. This is a modified intrepeter,"inspired by codeabbey" thats called brain++. The difference is this brain++ interpreter contain 2 additional function that can print and automatic input

additional symbol/statement
":" and ";"


":" this statement print the value of current cell
";" this statement/symbol is to input integer number and put it in currect cell of brainf*ck

explanation:  traditional brainF need multiple "+" symbol just to generate certain value of number in certain cell
like you need 8 "+" to generate value 8 in current cell but with ";" you just need type the certain value of 
example:

traditional way=
input:
++++++++++++++++++++++++>+++[<+>-]<:>: 

output: 27 0



brain++ way=  
input:
;>;[<+>-]<:>: 
24 3
  

output: 27 0


as you can see that ";" will "return" number in the same position. whereas first ";" return 24 and second ";" return 3. after each ";" return its number. the brain++ program executed
