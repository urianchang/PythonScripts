try:
    raise ValueError
except ValueError:
    if False:
        try:
            raise Exception("hi")
        except:
            raise
    else:
        raise
except:
    raise
