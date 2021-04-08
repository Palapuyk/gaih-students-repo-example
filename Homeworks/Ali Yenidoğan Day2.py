#Ali Yenidoğan
#1st Homework

list1 = [1,2,3,4,5,6,7,8,9,10]
list1[5:] = list1[10:4:-1]
print(list1)


x = int(input("Please insert a single digit integer:",))
list2 = list(range(x))
evens = [i for i in list2 if i % 2 == 0]
print(evens)        
        