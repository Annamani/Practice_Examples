# def causeError():
#     try:
#         return 1/0
#     except Exception as e:
#         print(type(e))
#     finally:
#         print("This block always executed")
# causeError()

# def causeError():
#     try:
#         # return 1 + 'a'
#         return 1/0

#     except TypeError:
#         print('There was a type error!')
#     except ZeroDivisionError:
#         print('There was a zero division error!')
#     except Exception:
#         print('There was some sort of error!')

    
# causeError()

# Custome decorators
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception:
            print('There was some sort of error!')
    return wrapper

@handleException
def causeError():
    return 1/0

causeError()