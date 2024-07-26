def check_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
