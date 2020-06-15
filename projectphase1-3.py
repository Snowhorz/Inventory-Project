#Name : Jovan Leung
#Admin no: 190326Z
#Module : IT2653-02

from collections import  deque
transactiondates = deque()


print("Welcome to Jovan's Grocery Store!")


serialno = 3
dateno = 4
#legend[serialno.,fruit,country,quantity,price]
itemlist = [[1,'Apple', 'japan', 9, 100.00],[2,'Banana', 'USA', 5, 200.00],[3,'Passionfruit','USA',7,150.00],[4,'Durian','Malaysia',2,145.00]]
shipments_50 = []
max = 0
for i in itemlist:
    if i[0] > max:
        max = i[0]

'''                            # add 50 items in inventory for testing 
serialno_50= max + 1
for i in range(50):
    shipments_50.append(serialno_50)
    shipments_50.append('Apples')
    shipments_50.append('SG')
    shipments_50.append(10)
    shipments_50.append(55.00)
    itemlist.append(shipments_50)
    serialno_50 +=1
    shipments_50=[]
'''

list = []
sortedlist = []


dailyrevenue = {}
dailyrevenue["11/07/19"] = 500.0
dailyrevenue["12/07/19"] = 800.0
monthlyrevenue = {}
monthlyrevenue["07/19"] = 1300.0
sales = {}
sales["1"] = ['date:11/07/19', 'SerialNo. 1', 'qty sold:2', 'amount($)200.0', "item desc:['Apple', 'japan'"]
sales["2"] = ['date:11/07/19', 'SerialNo. 1', 'qty sold:3', 'amount($)300.0', "item desc:['Apple', 'japan']"]
sales["3"] = ['date:12/07/19', 'SerialNo. 2', 'qty sold:4', 'amount($)800.0', "item desc:['Banana', 'USA']"]
transactiondates.append(['date:11/07/19', 'SerialNo. 1', 'qty sold:2', 'amount($)200.0', "item desc:['Apple', 'japan'"])
transactiondates.append(['date:11/07/19', 'SerialNo. 1', 'qty sold:3', 'amount($)300.0', "item desc:['Apple', 'japan']"])
transactiondates.append(['date:12/07/19', 'SerialNo. 2', 'qty sold:4', 'amount($)800.0', "item desc:['Banana', 'USA']"])
def add_inventory():                         #add item
    shipment = []
    max = 0
    for i in itemlist:
        if i[0] > max:
            max = i[0]
    serialno= max + 1
    while True:
        shipment.append(serialno)
        fruit = input("Enter the name of the fruit: ").lower()
        shipment.append(fruit)
        country = input("Enter the country of origin for the "+fruit+" :").lower()
        shipment.append(country)
        while True:
            try:
                qty = int(input("Enter the quantity:"))
                shipment.append(qty)
            except ValueError:
                print("Please enter a valid quantity.")
                continue
            while True:
                try:
                    price = float(input("Enter the price:"))
                    shipment.append(price)
                except ValueError:
                    print("Please enter a valid price.")
                    continue
                break
            break
        itemlist.append(shipment)
        serialno += 1
        print("Successfully added Shipment!")
        for i in itemlist:
            print(i)
        break


def create_sales():       #remove item
    x = False
    global dateno
    saleslist = []
    while True:
        if x:
            break
        date = input("Enter date of sales(dd/mm/yy): ")
        if len(date) != 8:
            print("Please enter the correct date format!")
            continue

        soldserial = int(input("Enter serial no. of fruit sold: "))
        found = False
        for i in itemlist:
            if i[0] == soldserial:
                found = True

                try:
                    qtysold = int(input("Enter the quantity purchased: "))
                except ValueError:
                    print("Please enter a valid number!")
                    continue
                if qtysold > i[3]:
                    print("Not enough stocks, please check the product details.")
                    return
                else:
                    i[3] -= qtysold
                    saleslist.append("date:" + date)
                    saleslist.append("SerialNo. " + str(soldserial))
                    saleslist.append("qty sold:" + str(qtysold))
                    salesrevenue = i[4] * qtysold
                    saleslist.append("amount($)" + str(salesrevenue))
                    saleslist.append("item desc:" + str(i[1:3]))
                    sales[dateno] = saleslist
                    dateno += 1
                    if date not in dailyrevenue:
                        dailyrevenue[date] = salesrevenue
                    else:
                        dailyrevenue[date] += salesrevenue
                    if date[3:8] not in monthlyrevenue:
                        monthlyrevenue[date[3:8]] = salesrevenue
                    else:
                        monthlyrevenue[date[3:8]] += salesrevenue
                    transactiondates.append(saleslist)                              #stack
                    print("Successfully added Sale!")
                    print(dailyrevenue)
                    print(monthlyrevenue)
                    x = True

                    break
        if found == False:
            print('Invalid')







def display_revenue():                  # display revenue
    typereport = input("Choose a monthly or daily report (m/d) ").lower()
    if typereport == 'm':
        while True:
            monthreport = input("Enter date of monthly report(mm/yy) ")
            if len(monthreport) != 5:
                print("Please enter the correct date format!")
                continue
            else:
                break
        found_record = monthlyrevenue.get(monthreport, "not found")
        if found_record == "not found":
            print("Nothing has been sold on " + str(monthreport) + " yet!")
        else:
            print("The total revenue for " + str(monthreport) + " is $" +
                  str(monthlyrevenue[monthreport]))
    elif typereport == 'd':
        while True:
            dailyreport = input("Enter date of daily report(dd/mm/yy) ")
            if len(dailyreport) != 8:
                print("Please enter the correct date format!")
                continue
            else:
                break
        found_record = dailyrevenue.get(dailyreport, "not found")
        if found_record == "not found":
            print("Nothing has been sold on " + str(dailyreport) + " yet!")
        else:
            print("The total revenue for " + str(dailyreport) + " is $" +
                  str(dailyrevenue[dailyreport]))


def edit_inventory():                   #remove/edit item
    x = False
    while True:
        if x:
            break
        todelkey = input("Are you deleting a Product Serial No.?(Y/N):").lower()
        if todelkey == "y":
            for i in itemlist:
                print(i)
            key = int(input("Enter the Serial number you want to delete: "))
            found = False
            for i in itemlist:
                if key == i[0]:
                    found = True
                    print('Deleted item ',i)
                    itemlist.pop(itemlist.index(i))
                    x = True
                    break
            if found == False:
                print('Invalid Serial Number')
                x = True
                break

        elif todelkey == "n":
            while True:
                if x :
                    break
                for i in itemlist:
                    print(i)
                serialtoedit = int(input("Which Serial number would you like to edit?"))
                found = False
                for i in itemlist:
                    if serialtoedit  == i[0]:
                        found = True
                        fruit = input("Enter the name of the fruit: ").lower()
                        i[1] = fruit
                        country = input("Enter the country of origin for the " + fruit + " :").lower()
                        i[2] = country
                        while True:
                            try:
                                qty = int(input("Enter the quantity:"))
                                i[3] = qty
                            except ValueError:
                                print("Please enter a valid quantity.")
                                continue
                            while True:
                                try:
                                    price = float(input("Enter the price:"))
                                    i[4] = price
                                except ValueError:
                                    print("Please enter a valid price.")
                                    continue
                                x = True
                                break
                            break
                        break
                if found == False:
                    print('Invalid serial no')
                    x = True
                    break


        else:
            print("Please enter a valid option!")
            continue



def display_product():           #display items
    found = False
    x = False
    display = input('View Products By: \n'
                    'Serial number(s) -binarysearch \n'
                    'Price(p) -insertionsort \n'
                    'Quantity(q) -bubblesort')
    if display.lower() == 's':                            #insertionsort & binarysearch
        list = []



        n = len(itemlist)

        for i in range(1, n):            # Save the value to be positioned
            value = itemlist[i]
            pos = i
            while pos > 0 and value[0] < itemlist[pos - 1][0]:
                # Shift the items to the right during the search
                itemlist[pos] = itemlist[pos - 1]
                pos -= 1

                # Put the saved value into the open slot.
                itemlist[pos] = value
        target = int(input('Serial No. of product you are searching for:'))       #search key for binarysearch
        for i in itemlist:
            list.append(i[0])

        low = 0
        high = len(list) - 1

        while low <= high:
            if x:
                break
            mid = (low + high) // 2
            if list[mid] == target:
                for i in itemlist:
                    if i[0] == target:
                        found = True
                        print('Details of Serial Number',target,':',i)
                        x = True
                        break

            elif target < list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        if found == False:
            print('ID does not exist')


    elif display.lower() == 'p':                                    #insertionsort
        n = len(itemlist)

        for i in range(1, n):

            # Save the value to be positioned
            value = itemlist[i]
            pos = i
            while pos > 0 and value[4] < itemlist[pos - 1][4]:
                # Shift the items to the right during the search
                itemlist[pos] = itemlist[pos - 1]
                pos -= 1

                # Put the saved value into the open slot.
                itemlist[pos] = value
        print('By Price:')
        for i in itemlist:
            print(i)

    elif display.lower() == 'q':                                      #bubblesort
        n = len(itemlist)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if itemlist[j][3] > itemlist[j + 1][3]:
                    tmp = itemlist[j]
                    itemlist[j] = itemlist[j + 1]
                    itemlist[j + 1] = tmp
        print('By Quantity:')
        for i in itemlist:
            print(i)





def display_sales():                           #display sales
        choice = input( 'To view all Transactions from the latest one type a \n'
                       'To view most recent (n) transaction type n')
        found = False
        '''
        if choice.lower() == 't':
            print('Transaction dates starting from the oldest sale')
            for i in sales:
                print(i, sales[i],'\n')
        '''
        if choice.lower() =='a':                                                                        #stack
            found = True
            print('Transaction dates starting from the most recent sale')
            x = len(transactiondates)
            while x > 0:
                print(x,transactiondates[x-1])
                x -= 1
        if choice.lower() == 'n':                                                                       #stack
            found = True
            x = int(input('View latest n transactions (key in n) :  '))
            if x <= len(transactiondates):
                while x > 0:
                    print(x,transactiondates[x-1])
                    print(transactiondates[x-1][1][10::])
                    x -= 1

            else:
                print('Not sufficient transaction records , currently only has',len(transactiondates),'transactions')


        if found == False:
            print('Enter valid option')



def display_stock():                     #total and average stock
    choice = input('Display Total(t) or Average(a) stock:')
    if choice.lower() == 't':
        stock = 0
        for i in itemlist:
            stock += i[3]
        print('Total Stock: ',stock)
    elif choice.lower() == 'a':
        stock = 0
        for i in itemlist:
            stock += i[3]
        stock = stock / len(itemlist)
        print('Average Stock:',stock)

def refund():                     # uses stack --> when u remove the transaction you can check the inventory and revenue ,
                                            # the transaction revenue will be remove and the goods will be returned to the inventory.
    x = len(transactiondates)
    for i in itemlist:
        if x !=0:
            #print(i[0])
            #print(transactiondates[x - 1][1][10::])
            if int(transactiondates[x - 1][1][10::]) == int(i[0]):
                # replace the inventory back
                #print(i)
                #print(i[3])
                #print('inventory',int(transactiondates[x - 1][2][9::]))
                i[3] += int(transactiondates[x - 1][2][9::])
                #print(i[3])
                # remove the revenue earned
                #print(transactiondates[x - 1])
                day = transactiondates[x - 1][0][5::]
                #print(day)
                month = transactiondates[x - 1][0][8::]
                #print(month)
                price = transactiondates[x - 1][3][9::]
                #print(price)
                if day in dailyrevenue:
                    dailyrevenue[day] -= float(price)
                if month in monthlyrevenue:
                    monthlyrevenue[month] -= float(price)
                print('Refunded the most recent transaction:', transactiondates.pop())
                break
        else:
            print('No more transaction')
            break





while True:
    firstchoice = input("Please select any of the following option to continue: \n"
                            "(1) Add inventory \n"
                            "(2) Create sales \n"
                            "(3) Display revenues \n"
                            "(4) Edit/Delete current inventory \n"
                            "(5) Display product details \n"
                            "(6) Display sales details \n"
                            "(7) Display stock level \n"
                            "(8) Undo Most Recent Transaction \n"
                            "(0) Exit program(Enter Q/q to exit)").lower()
    if firstchoice == "1":
        add_inventory()
    elif firstchoice == "2":
        create_sales()
    elif firstchoice == "3":
        display_revenue()
    elif firstchoice == "4":
        edit_inventory()
    elif firstchoice == "5":
        display_product()
    elif firstchoice == "6":
        display_sales()
    elif firstchoice == '7':
        display_stock()
    elif firstchoice =='8':
        refund()
    elif firstchoice == "0":
        exit()
    elif firstchoice == "q":
        exit()
    else:
        print("Please enter a valid option!")
        continue




