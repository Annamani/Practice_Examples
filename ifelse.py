for n in range(1,35):
    if n%15==0:
        print("FizzBuzz")
    else:
        if n%3==0:
            print("Fizz")
        else:
            if n%5==0:
                print("Buzz")
            else:
                print(n)