'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  ///
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

MAX_AMOUNT = 1000000
MAX_QUANTITY = 1000
MAX_NET = 1000000

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')


def validorder(order: Order):
    net = 0

    for item in order.items:

        if item.type == 'payment':
            if item.amount >= MAX_AMOUNT or item.amount <= - MAX_AMOUNT:
                print(f"Invalid amount: {item.amount} for item {str(item)}.")
                continue

            net += item.amount

        elif item.type == 'product':
            if item.amount >= MAX_AMOUNT or item.amount <= - MAX_AMOUNT:
                print(f"Invalid amount: {item.amount} for item {str(item)}.")
                continue

            if item.quantity >= MAX_QUANTITY or item.quantity < 0:
                print(f"Invalid quantity: {item.quantity} for item {str(item)}.")
                continue

            net -= item.amount * item.quantity

            if net >= MAX_NET:
                return(f"The total amount has exceeded the maxinum value: {net}")

        else:
            return("Invalid item type: %s" % item.type)

    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
