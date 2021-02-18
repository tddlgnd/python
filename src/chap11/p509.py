# max(), min()
values = [ 1, 2, 3, 4, 5]
print(max(values))
print(min(values))


# enumerate()
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))


# filter()
def myfilter(x):  
	return x > 3  

result = filter(myfilter, (1, 2, 3, 4, 5, 6))  
print(list(result)) 
