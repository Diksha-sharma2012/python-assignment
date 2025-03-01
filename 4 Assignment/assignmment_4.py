Enter_number = input("Enter an integer number from 0 to 999: ")

def interger_to_word(n):
#words for number 0 to 19    
    one_to_nineteen = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
#words for  number 20 to 90 
    twenty_to_ninety = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    result = ""

#If user enter 0 then it will return Zero
    if n == 0:
     return "Zero" 

    # It will return integer number greater than or equal to hundred into words    
    if n >= 100:
            result += one_to_nineteen[n // 100] + " Hundred "  #example n = 249, 249//100 = 2 => Two (because one_to_nineteen[2]= Two) then Two + Hundred = Two Hundred (stored in result)
            n %= 100      # Reduce the number by the hundreds part
        
    if  n >= 20:
            result += twenty_to_ninety[n // 10] + " "  # remaining integer (except hundred position) i.e. 49 will calculated as n = 49, 49 // 10 = 4 => Fourty (because twenty_to_ninety[4]= Fourty)
            n %= 10      # Reduce the number by the tens part
            
    if n >= 0:
            result += one_to_nineteen[n] + " "   # The remaining part of example (i.e. 9) will be as one_to_nineteen[9] = Nine
            
            return result.strip()   #return result without spacing  (It will return the result by combining "Two Hundred" + "Fourty" + "Nine" = Two Hundred Fourty Nine)


    #Enter_number = input("Enter an integer number from 0 to 999: ")
if Enter_number.isdigit():
     number = int(Enter_number) 
     if 0<= number <= 999: # and Enter_number <= 999:
        print(interger_to_word(number))
     else:
        print("Please enter a valid number between 0 to 999.\nThankyou!☺️")    
else:
        print("Error: Please enter a valid integer.\nThankyou!☺️")        
            

    
        