def open_or_senior(data):
    return ["Senior" if inf[0] >= 55 and inf[1] > 7 else "Open" for inf in data]