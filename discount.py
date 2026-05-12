def get_discount(price, user_type):
    if user_type == "admin":
        discount = 0.5
    elif user_type == "member":
        discount = 0.1
    return price * discount

print(get_discount(100, "guest"))
