def fibonacci (n):
    
    if n == 0:
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2)
 


b = fibonacci(4)

print(zero_count)
print(one_count)


## 강사님 풀이

def Fibonacci(num):
    global count_one, count_zero
    if num == 0:
        count = count + 1 
#1 1 2 3 5 8 


### 2. 별 찍기 (for, range, input 사용)

x = int(input("입력")) * 2
a = []
b = []
for i in range(1, x, 2):
    a.append(i) 
    b.append(i)
 
b.reverse()
b.remove(1)
for i in range(len(b)):
    print(" " *(i) , "*" * b[i], " " *(i))
 
for i in range(len(a)):
    print(" " * ((len(a)-1) - i), "*" * a[i], " " * ((len(a)-1) - i))

# x = int(input("입력")) * 2
# a = []
# b = []
# for i in range(1, x, 2):
#     a.append(i) ## [1, 3, 5, 7, 9]
#     b.append(i)

# b.reverse()
# b.remove(1)
# # len(b) = 5
# for i in range(len(b)):
#     print(" " *(i) , "*" * b[i], " " *(i))

# for i in range(len(a)):
#     print(" " * ((len(a)-1) - i), "*" * a[i], " " * ((len(a)-1) - i))