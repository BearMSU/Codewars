def derive(coefficient, exponent): 
    # your code here
    product = coefficient * exponent
    true_exponent = exponent - 1
    return f"{product}x^{true_exponent}"