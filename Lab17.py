even= lambda x: x%2==0
x=even(4)
print(x)
numbers=[1,2,3,4,5]
even_numbers=list(filter(even,numbers))
print(even_numbers)
fruits=["Cherry","Banana","Date","Apple","Mango","Dragonfruit"]
print(fruits)
Sorted_fruits=sorted(fruits,key=lambda x: len(x),reverse=True)
print(Sorted_fruits)

def fibonacci(n):
    if n <= 0:
        return 
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)

        return result
print(fibonacci(10))
sequence=[]
for i in range(1,11):
    sequence.append(fibonacci(i))

print(sequence)

