def calculate_discount(total, coupon):
    if coupon == "SAVE10":
        return round(total * 0.90, 2)
    elif coupon == "SAVE20":
        return round(total * 0.80, 2)
    return total