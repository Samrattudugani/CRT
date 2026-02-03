## bug -> error , debbug -> Finding and fixing of the errors 
## Types of errors
## 1. SYNTAX ERRORS : missing of colon and indentations .
## 2. RUNTIME ERRORS : Arithematic errors , div by 0.
## 3. LOGICAL ERRORS : wen there is a LOGIC Missing .
################################################################
## Debugging Techniques : 
## 1. Print function [print()]
#################################################################
## 2. try-except
 ##try:
   ## a = int(input())
    ##print(10/a)
 ##except ZeroDivisionError:
  ##  print("Can not divisible by Zero .")
 ##except ValueError:
  ##  print("Invalid")
######################################################################
## 3. using pdb :[ python de bugger ]
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## PURPOSE : 
##          1.Pause the execution 
##          2.insert the var values
##          3. to run code line by line
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
## PDB COMMANDS:
## 1.n - to execute the output in a next line 
## 2.p variable - to get the value of variable  
## 3.l - List near by code
## 4.c - continue the execution
## 5.s - to start a function
## 6.r - return from the function 
## 7.h - help
## 8.q - quit hte execution
##............................................
## Example:
##import pdb
##def add(a, b):
 ##   pdb.set_trace()  # Set the breakpoint
  ##  return a + b
 ##a = int(input())
 ##b = int(input())
## print(add(a, b))

