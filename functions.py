# def performOperations(num1, num2, operation):
#     if operation=='sum':
#         return num1+num2
#     if operation=='multiply':
#         return num1*num2
#     if operation=='div':
#         return num1/num2
#     if operation=='sub':
#         return num1-num2
#     if operation=='mod':
#         return num1%num2
# print(performOperations(2, 3, 'sum'))
# print(performOperations(3, 4, 'multiply'))
# print(performOperations(4, 5, 'div'))
# print(performOperations(5, 6, 'sub'))
# print(performOperations(6, 7, 'mod'))

# # Named Parameters
# def performOperations(num1, num2, operation='multiply', message='Default message'):
#     print(message)
#     if operation=='sum':
#         return num1+num2
#     if operation=='multiply':
#         return num1*num2
    
# print(performOperations(4, 4, 'multiply', message='successfully function is executed'))

# *Args
def printArgs(*args):
    print(args)

printArgs("Hello","Annamani","Thanks for writing me")
printArgs(1,2,3,4,5,6,7,8,9,10)
printArgs(('a','b'),{1,2,3,4},['abc','def'])
# **kwargs