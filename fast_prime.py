# def fast_prime():
#     for number in range(2,50):
#         for factor in range(2,int(number** 0.5)+1):
#             if number%factor==0:
#                 break
#         else:
#             print(f'{number} is prime')

# fast_prime()

def fast_prime():
    
    for number in range(2,50):
        found_factor=False
        for factor in range(2,int(number** 0.5)+1):
            if number%factor==0:
                found_factor=True
        if not found_factor:
            print(f'{number} is prime')

fast_prime()