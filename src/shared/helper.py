from config.config import Config

def calculate_tax(price, code):
    """
    Calculate tax based on tax code.

    Attributes:
        price: Tax object price.
        code: Tax code.

    If tax code is 1 (food), tax is 10% of price
    If tax code is 2 (tobacco), tax is 10 + (2% of price)
    If tax code is 3 (entertainment), tax is:
        free if 0 < Price < 100,
        if price >= 100, then tax is 1% of (price - 100)
    """

    if code == 1:
        return 0.1*price
    elif code == 2:
        return 10 + (0.02*price)
    elif code == 3:
        if price < 100:
            return 0
        elif price >= 100:
            return 0.01*(price - 100)

def calculate_amount(price, tax):
    """
    Calculate amount for specific tax object.

    Attributes:
        price: Tax object price.
        tax: Tax to be paid.
    """
    return price + tax

def is_refundable(code):
    """
    Check if Tax Code is refundable or not.

    Attributes:
        code: Tax code.
    """

    return Config.TAX_CODE_IS_REFUNDABLE[code] if Config.TAX_CODE_IS_REFUNDABLE[code] else ''
