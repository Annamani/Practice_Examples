def causeError():
    try:
        return 1/0
    except Exception as e:
        print(type(e))
    finally:
        print("This block always executed")
causeError()