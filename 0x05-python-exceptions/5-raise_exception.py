def raise_exception():
    try:
        raise TypeError("Exception raised")
    except TypeError as te:
        raise te
