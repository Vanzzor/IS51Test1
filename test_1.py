

"""
The program calculates the best payment option (better salary)
first option is 100 dollarers , per day for 10 days
second option is 1 a day with it being doubled ea day for 10 days, two functions to calculate pay rate,
function1 calcs the amount for the first option
function2 calcs the amount for the second option

function1 will output 100*10 days
function2 will loop 10 times, withe a time x2 (double amount) and add to total

if amount is equal, we output to the user "option 1 and option 2 pays the same"
if option1 is better, we output to the user "Option1 is better"
if option2 is better, we output to the user "Option2 is better"

"""

"""
 #option1
    return 100 * 10

#option2
 amount = 1
 list1= []
 loop 10 times
    add amount list1
    amount *=2
    sum = sum of all items in loop
 return sum

#main
 var1=option1
 var2=option1

 if var1=var2
 "option1 and option 2 pays the same"
if var1 < var2
    "option 2 is better"
    else
    "option 1 is better"

main

"""

def option1():
    return 100*10


def option2():
    amount=1
    list1=[]
    for i in range(0, 10):
        list1.append(amount)
        amount *=2
    print("list1", list1)
    total=sum(list1)
    return total


    def main():
        answer=""
        var1=option1() # 1000
        var2=option2() #1023
        print("from main: varl1", var1, "var2", var2)
        if var1==var2:
         answer="Option 1 and option 2 pays the same"
        if var1<var2:
            answer="Option 2 is better"
        else:
            answer="option 1 is better"
        print(answer)
  
    main()