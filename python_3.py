def get_revenue(order: tuple, order_amounts: list = None):
    order_amounts = order_amounts if order_amounts and isinstance(order_amounts, list) else list()
    order_amounts.append(order[1])
    return order_amounts

# print(get_revenue(order=(2,4), order_amounts=[2,4,5]))
