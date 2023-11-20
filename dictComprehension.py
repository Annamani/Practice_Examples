animalList=[('a','ape'),('b','bear'),('c','cat'),('d','dog'),('e','elephant')]
# Converting list to a dictionary
animals={item[0]:item[1] for item in animalList}
print(animals)
# other way we can convert a list to a dict
animals1={key:value for key,value in animalList}
print(animals1)