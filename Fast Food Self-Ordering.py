import random


#declare all variables

#quantity of food items
beefburger_qty = 0
fishburger_qty = 0
frenchfries_qty = 0
colddrink_qty = 0
beefburgervm_qty = 0
fishburgervm_qty = 0

#price of food items
beefburger_price = 8
fishburger_price = 6.5
frenchfries_price = 3.5
colddrink_price = 3.8
beefburgervm_price = 10
fishburgervm_price = 8.5

#queue number
queue_no=0


#creating a while loop 
#displaying menu options so user can choose
while True:
    #automatically print introduction
    print("""Welcome to Happy Burger!
Please select the options:
======================================
m for menu
n for new order
e for edit order
c to check your final order, and total amount""")

    #printing menu    
    #getting user input
    userinput = input("Enter option: ")
    if userinput == "M" or userinput == "m":
        print(""" MENU
==============================================
ID                Food                  Price
1.             Beef burger               $8.00
2.             Fish burger               $6.50
3.             French fries              $3.50
4.             cold drink                $3.80
5.        Beef Burger Value Meal         $10.00
6.        Fish Burger Value Meal         $8.50 """)
        
        while True:
            mainmenu = input(""" 
Yes = '0'
Return to main menu?: """)
            if mainmenu == "0":
                    break    
    
#getting order from the user
    elif userinput == "N" or userinput == "n":
        #Input food ID to select order or exit
        #if foodID is zero then break
        while True:
            foodID = int(input("Enter food ID to select your orders or '0' to exit: "))
            if foodID == 0:
                break          

            #beef burger 
            elif foodID == 1:
                while True:
                    beefburger_qty = int(input("Quantity of Beef burger: "))
                    if beefburger_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #fish burger
            elif foodID == 2:
                while True:
                    fishburger_qty = int(input("Quantity of Fish burger: "))
                    if fishburger_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #french fries
            elif foodID == 3:
                while True:
                    frenchfries_qty = int(input("Quantity of French fries: "))
                    if frenchfries_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #cold drinks
            elif foodID == 4:
                while True:
                    colddrink_qty = int(input("Quantity of Cold drink: "))
                    if colddrink_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #beef burger value meal
            elif foodID == 5:
                while True:
                    beefburgervm_qty = int(input("Quantity of Beef burger value meal: "))
                    if beefburgervm_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #fish burger value meal
            elif foodID == 6:
                while True:
                    fishburgervm_qty = int(input("Quantity of Fish burger value meal: "))
                    if fishburgervm_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            
            else:
                print('Type in the correct command please')

#editing order
    elif userinput == "E" or userinput == "e":
        #Display current order list of food item
        print("""
Your current order :
============================
Qty      Food
%s    Beef burger
%s    Fish burger
%s    French fries
%s    Cold drink
%s    Beef burger value meal
%s    Fish burger value meal
""" %(beefburger_qty, fishburger_qty, frenchfries_qty, colddrink_qty, beefburgervm_qty, fishburgervm_qty))

        while True:
            #Display No. and order item for edit (menu)
            print("""
Please select the order you would like to edit:
================================================
No.      Food
1.    Beef burger
2.    Fish burger
3.    French fries
4.    cold drink
5.    Beef Burger Value Meal
6.    Fish Burger Value Meal
""")

            #Input food no. to edit order or exit
            #break
            edit_no = int(input("Enter the food no. you would like to edit or '0' to exit: "))
            if edit_no == 0:
                break
            #editing beef burger quantity
            elif edit_no == 1:
                print("Current quantity of Beef burger: %s" %(beefburger_qty))
                while True:
                    beefburger_qty = int(input("Re-enter quantity of Beef burger: "))
                    if beefburger_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #editing fish burger quantity
            elif edit_no == 2:
                print("Current quantity of Fish burger: %s" %(fishburger_qty))
                while True:
                    fishburger_qty = int(input("Re-enter quantity of Fish burger: "))
                    if fishburger_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #editing french fries quantity
            elif edit_no == 3:
                print("Current quantity of French fries: %s" %(frenchfries_qty))
                while True:
                    frenchfries_qty = int(input("Re-enter quantity of French fries: "))
                    if frenchfries_qty < 0:
                         print("Please re-enter again")
                    else:
                        break
            #editing cold drink quantity
            elif edit_no == 4:
                print("Current quantity of Cold drinks: %s" %(colddrink_qty))
                while True:
                    colddrink_qty = int(input("Re-enter quantity of Cold drink: "))
                    if colddrink_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #editing beef burger value meal quantity
            elif edit_no == 5:
                print("Current quantity of Beef burger value meal: %s" %(beefburgervm_qty))
                while True:
                    beefburgervm_qty = int(input("Re-enter quantity of Beef burger value meal: "))
                    if beefburgervm_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            #editing fish burger value meal quantity        
            elif edit_no == 6:
                print("Current quantity of Fish burger value meal: %s" %(fishburgervm_qty))
                while True:
                    fishburgervm_qty = int(input("Re-enter quantity of Fish burger value meal: "))
                    if fishburgervm_qty < 0:
                        print("Please re-enter again")
                    else:
                        break
            else:
                print('Type in the correct command please')

#final order and checkout
    elif userinput == "C" or userinput == "c":
        #Display final order list of food item
        print("""
Your final order list :
============================
Qty      Food
%s    Beef burger
%s    Fish burger
%s    French fries
%s    Cold drink
%s    Beef burger value meal
%s    Fish burger value meal
""" %(beefburger_qty, fishburger_qty, frenchfries_qty, colddrink_qty, beefburgervm_qty, fishburgervm_qty))

        #Input checkout or cancel order
        checkout_option = input("""
Checkout = '1'
Cancel order = '0'
Would you like to proceed to checkout or cancel order?: """)

        #Reset all food items
        if checkout_option == "0":
            beefburger_qty = 0
            fishburger_qty = 0
            frenchfries_qty = 0
            colddrink_qty = 0
            beefburgervm_qty = 0
            fishburgervm_qty = 0
            print("Order cancelled!")
            continue

        #Calculate cost for each item, total GST, total cost for order
        elif checkout_option == "1":
            totalcost_beefburger = beefburger_qty * beefburger_price
            totalcost_fishburger = fishburger_qty * fishburger_price
            totalcost_frenchfries = frenchfries_qty * frenchfries_price
            totalcost_colddrink = colddrink_qty * colddrink_price
            totalcost_beefburgervm = beefburgervm_qty * beefburgervm_price
            totalcost_fishburgervm = fishburgervm_qty * fishburgervm_price
            totalcost_item = totalcost_beefburger + totalcost_fishburger + totalcost_frenchfries + totalcost_colddrink + totalcost_beefburgervm + totalcost_fishburgervm
            gst = 0.07 * totalcost_item
            totalcost = gst + totalcost_item

        #Generate new queue number
        queue_no = queue_no + 1
        
        #Print receipt
        print("""

Queue: %s
====================================
Confirmed order list:
====================================
Qty      Food                Amount
%s    Beef burger             $ %.2f
%s    Fish burger             $ %.2f
%s    French fries            $ %.2f
%s    Cold drink              $ %.2f
%s    Beef burger value meal  $ %.2f
%s    Fish burger value meal  $ %.2f
====================================
Total amount (exclude GST) : $ %.2f
Total amount with GST : $ %.2f
====================================
Total cost : $ %.2f
====================================
   Thank you! Please come again
""" %(queue_no, beefburger_qty, totalcost_beefburger, fishburger_qty, totalcost_fishburger, frenchfries_qty, totalcost_frenchfries, colddrink_qty, totalcost_colddrink, beefburgervm_qty, totalcost_beefburgervm, fishburgervm_qty, totalcost_fishburgervm, totalcost_item, gst, totalcost))        

        #Reset all food item to 0
        beefburger_qty = 0
        fishburger_qty = 0
        frenchfries_qty = 0
        colddrink_qty = 0
        beefburgervm_qty = 0
        fishburgervm_qty = 0




