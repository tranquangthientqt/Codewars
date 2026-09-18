def number(bus_stops):
    return sum(bus[0] - bus[1] for bus in bus_stops)