def rental_car_cost(d):
    return d * 40 - (0, 20, 50)[(d > 3) + (d >= 7)]