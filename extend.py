myList=list()

# class UniqueList(list):
#     def append(self, item):
#         if item in self:
#             return
#         super().append(item)
        
# uniqueList = UniqueList()
# uniqueList.append(1)
# uniqueList.append(1)
# uniqueList.append(2)
class UniqueList(list):
    
    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'
        

    def append(self, item):
        if item in self:
            return
        super().append(item)
        
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)

print(uniqueList)