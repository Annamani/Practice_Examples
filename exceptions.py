def causeError():
    try:
        return 1/0
    except Exception as e:
        print(type(e))
causeError()