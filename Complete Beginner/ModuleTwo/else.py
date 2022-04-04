def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else: 
        print ("Valid username")

def is_even(number):
    if number % 2 == 0: # "%" = Modulo and returns integer devision and remainder
        return True
    return False

#else is not required in this situation but is still valid in either situation.

