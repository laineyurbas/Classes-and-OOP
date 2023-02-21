import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]


customer = fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712','dsellyarft@gmpg.org', '254-555-9362', False)
customer = fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710','ahimsworthfs@list-manage.com', '254-555-2273', True)

order_total = 0


print(f'Customer Name: {customer.get_name()}')
print(f'Phone: {customer.get_phonenum()}')

### NEED TO PRINT CUSTOMER NAME AND PHONE NUMBER ###

dict = {'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
        'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
        'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
        'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
        }
for t in dict:
    t = fc.Transaction(dict[t][0], dict[t][1], dict[t][2], dict[t][3])

    if int(t.get_customer_id()) == int(customer.get_customer_id()):
        st = int(t.get_cost())
        order_total += st
        print(
            f"Order Item: {t.get_item_name()}  Price: ${(format(t.get_cost(),'.2f'))}")
print(f"Total cost: ${format(order_total, '.2f')}")

if customer.get_member_status() == True:
    discount = .2 * order_total
    dt = order_total - discount
    print(f"Member Discount: ${format(discount, '.2f')}")
    print(f"Total cost after Discount: ${format(dt, '.2f')}")
