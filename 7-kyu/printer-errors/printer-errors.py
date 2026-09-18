def printer_error(s):
    return f"{sum(c > 'm' for c in s)}/{len(s)}"