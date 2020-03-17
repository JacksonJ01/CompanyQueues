# Jackson J.
# 3/9/2020
# A program that simulates the order system for a small paper supply company.
# The company gets in cases of paper that it then resells at a 10% profit
from LinkedQueue import *
from getpass import getuser
from time import sleep
terminal = getuser()
MyQueue = Queue()
MyCost = Queue()
Inventory = 0
Profit = 0
menu = 'Hello World'


input("CLICK HERE, THEN PRESS ENTER")

name = input("\nHello there user, what is your name?"
             "\n>>>").title()

sleep(1)
print("\nI like that name a lot."
      f"\n{name}\b\b\b, {name}\b\b, {name}"
      f"\n{name} rolls off the tongue nicely.")

sleep(2)
print(f'\nAs you may know I, {terminal} (your terminal), have a FIFO inventory set up for you to use.'
      "\nAnd now that I've mentioned this, it's only natural for me to take you to the menu."
      "\nHave fun XD")

input("\nPress Enter")


while menu != 'Exit' or menu != '4':
    sleep(.5)
    print(f'\nInventory: {Inventory}')
    menu = input('\n1. ADD to inventory'
                 '\n2. SELL from inventory'
                 '\n3. check PROFIT to date'
                 '\n4. EXIT'
                 '\n>>>').title()

    if menu == 'Add' or menu == '1':
        add = "Hello World"
        while add != int:
            value = input("\nHow much would you like to add to inventory?"
                          "\n>>>")
            try:
                add = int(value)
                if add > 0:
                    break
                else:
                    print("Enter a whole number greater than 0.")
            except ValueError:
                print("No... Enter a whole number greater than 0."
                      "\nNo letters, words and or floats.")

        MyQueue.push(add)
        Inventory += add

        cost = "Hello World"
        while add != int:
            value = input("\nHow much did each item cost?"
                          "\n>>>")
            try:
                if int(value) > 0:
                    cost = int(value)
                    break
                else:
                    print("Enter a number greater than 0.")
            except ValueError:
                try:
                    if float(value) > 0:
                        cost = float(value)
                        break
                    else:
                        print("Enter a number greater than 0.")
                except ValueError:
                    print("No... Enter a number greater than 0, not text.")
        MyCost.push(cost)
        print(f"{add} items added at ${cost} each.")

    elif menu == 'Sell' or menu == '2':
        sell = 'Hello World'
        while sell != int:
            value = input("\nHow much do you want to sell from the inventory?"
                          "\n>>>")
            try:
                sell = int(value)
                if sell > 0:
                    break
                else:
                    print("Enter a whole number greater than 0.")
            except ValueError:
                print("Enter whole a whole number greater than 0."
                      "\nNo letters, words and or floats.")
        value = MyQueue.head()

        if value is None or Inventory < sell:
            print("\nERROR:"
                  "\nAdd units more to inventory")

        elif value > sell or value == sell:
            Inventory -= sell
            cost = MyCost.head()
            if value > sell:
                value -= sell
                MyQueue.re_head(value)

            elif value == sell:
                MyQueue.pop()
                MyCost.pop()

            made = cost * 1.1 * sell
            profit = made - cost * sell
            print(f"You made ${made: .2f}, with a profit of ${profit: .2f}.")
            Profit += profit

        elif value < sell or Inventory > sell or Inventory == sell:
            sold = sell
            Inventory -= sell
            divider = 0
            total_cost = []
            # This is not working as intended
            # If i want to sell 8 items and the first value is five, while the next is ten, something gets screwed up
            while sell - value >= 0:
                if sell - value > 0:
                    sell -= value
                    MyQueue.pop()
                    value = MyQueue.head()
                    total_cost.append(MyCost.head())
                    MyCost.pop()
                    divider += 1
                    # I want to see where the program fails
                    print("chess")
                    if value - sell > 0:
                        value -= sell
                        MyQueue.re_head(value)
                        total_cost.append(MyCost.head())
                        divider += 1
                        # I want to see where the program fails
                        print('bacon')

                    elif value - sell == 0:
                        total_cost.append(MyCost.head())
                        MyQueue.pop()
                        MyCost.pop()
                        divider += 1
                        # I want to see where the program fails
                        print('eggs')
                    break
                # I think the problem arises here
                else:
                    if value - sell > 0:
                        value -= sell
                        MyQueue.re_head(value)
                        total_cost.append(MyCost.head())
                        divider += 1
                        # I want to see where the program fails
                        print('bacon')

                    elif value - sell == 0:
                        total_cost.append(MyCost.head())
                        MyQueue.pop()
                        MyCost.pop()
                        divider += 1
                        # I want to see where the program fails
                        print('eggs')
                    break
            # I added this part because i wanted to see what was going o behind the scenes(where it was failing at)
            made = sum(total_cost) / divider * 1.1 * sold
            profit = made - sum(total_cost) / divider * sold
            print(f'You made ${made: .2f}, with a ${profit: .2f} profit.'
                  f'\ntotal_cost values {total_cost}'
                  f'\ntotal_cost values summed up {sum(total_cost)}'
                  f'\nhow many values to divide {divider}'
                  f'\nhow many sold {sold}.')

    elif menu == 'Profit' or menu == '3':
        print(f'The current profit to date is ${Profit}.')

    elif menu == 'Exit' or menu == '4':
        print(f"\nThanks for playing {name}."
              f"\nI mean it, from one terminal, to another."
              f"\n{terminal} over and out")
        break
