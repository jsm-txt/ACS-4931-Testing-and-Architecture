# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
def get_price():
    base_price = get_base_price(x,y)
    if base_price > 1000:
        return 0.95 * base_price
    else:
        return 0.98 * base_price

def get_base_price(quantity, item_price):
    return quantity * item_price