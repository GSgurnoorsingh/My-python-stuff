#The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples.
# Each tuple contains elements from the input iterables that are at the same position.
name=['John','Alice','Bob','Lucy']
scores=[85,90,78,92]
res=zip(name,scores)
print(list(res))

d={'name':'Alice','age':25,'grade':'A'}
keys=d.keys()
values=d.values()
res=zip(keys,values)
print(list(res))