'''Prime Factorization - Have the user enter a number and \
find all Prime Factors (if there are any) and display them.'''

num = int(input("Enter the number to find prime factors for: "))
factors = [1]
factors_sort = []
final = []

########################################################
def check_prime(num):
    flag = False
    if num >= 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                flag = False
                break
        else:
            flag =True
    else:
        flag = False
    
    return flag

########################################################
if num>=1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            factors_sort.append(i)
    else:
        factors_sort.append(None)

########################################################
for k in factors_sort:
    if k != None:
        factors.append(k)

########################################################
if len(factors)!=0: 
    for j in factors:
        if check_prime(j)==True:
            final.append(j)
    print("Prime Factors are: ",final)           
    if final == [1]:
        print("Number given was already prime.")

########################################################
