def process_order(flavor, topping, cone):
    """
    Write a Python function that returns a string representing an
    ice cream order for a drive through window

    The inputs to the function are flavor, topping and cone, which are each strings

    The output is a string that matches the format below (with appropriate variable names)

    You ordered a ordered a chocolate ice cream with sprinkles in a cake cone. Your order is coming right up.

    """
    output = "You ordered a ordered a "
    output += flavor
    output += " ice cream with "
    output += topping
    output += " in a "
    output += cone

    output += " cone. Your order is coming right up."
    return output
