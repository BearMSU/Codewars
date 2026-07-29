def calculate_age(year_of_birth, current_year):
    total = abs(current_year - year_of_birth)
    
    y = 'years'
    if total == 1:
        y = 'year'
        
    if year_of_birth < current_year:
        return f"You are {total} {y} old."
    elif year_of_birth > current_year:
        return f"You will be born in {total} {y}."
    else:
        return "You were born this very year!"