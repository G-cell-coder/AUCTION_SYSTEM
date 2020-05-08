#-----------------ISP BIDDIND SYSTEM--------------------
items = []
while True:
    display = input('Press enter to continue.')
    print('------------------Welcome to  AUCTION portal------------------')
    print('1. View Operators Interested \n2. Add Operator Name for sale\n3. Purchase Operator \n4. Search Operator \n5. Edit Operator details \n6. Exit')
    choice = input('Enter the number of your choice : ')

    if choice == '1' :
        print('------------------View Operators Interested ------------------')
        print('The number of items in the inventory are : ',len(items))
        while len(items) != 0:
            print('Here are all the items available in the ISP portal.')
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)
            break

    elif choice == '2' :
        print('------------------Add Operator Name for sale------------------')
        print('Operator you wanted to own:')
        # for num in range(number_items):
        item = {}
        item_name = input('Item name : ')
        print(items)
        print(item_name)
        dic =  [ sub['name'] for sub in items ]
        print(dic)
        if item_name in dic:
            print("Already the product is added, Please try some other name")
           
        else:
            item['name'] = item_name
            while True:
                try:
                    item['quantity'] = int(input('Item quantity : '))
                    break
                except ValueError:
                    print('Quantity should only be in digits')
            while True:
                try:
                    item['price'] = int(input('Price $ : '))
                    break
                except ValueError:
                    print('Price should only be in digits')
            print('Item has been successfully added.')
            items.append(item)

    elif choice == '3' :
        print('------------------Purchase Operator------------------')
        print(items)
        purchase_item = input('which Operator do you want to purchase? Enter name : ')
        for item in items:
            if purchase_item.lower() == item['name'].lower() :
                if item['quantity'] != 0 :
                    print('Pay ', item['price'] , 'at checkout counter.')
                    item['quantity'] -= 1
                else:
                    print('item out of stock.')

    elif choice == '4' :
        print('------------------Search Operator------------------')
        find_item = input('Enter the Operator name to search in inventory : ')
        for item in items:
            if item['name'].lower() == find_item.lower():
                print('The item named ' + find_item + ' is displayed below with its details')
                print(item)
            else:
                print('item not found.')

    elif choice == '5' :
        print('------------------Edit Operator details------------------')
        item_name = input('Enter the name of the item that you want to edit : ')
        for item in items:
            if item_name.lower() == item['name'].lower():
                print('Here are the current details of ' + item_name)
                print(item)
                item['name'] = input('Item name : ')
                while True:
                    try:
                        item['quantity'] = int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                while True:
                    try:
                        item['price'] = int(input('Price $ : '))
                        break
                    except ValueError:
                        print('Price should only be in digits')
                print('Item has been successfully updated.')
                print(item)
            else:
                print('Item not found')
               
    elif choice == '6' :
        print('------------------exited------------------')
        break

    else:
         print('You entered an invalid option')

