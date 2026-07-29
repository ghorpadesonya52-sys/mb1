import time 
import matplotlib.pyplot as plt  
def bubblesort(list1): 
    n=len(list1) 
    for i in range(n-1):  
            
           swapped=False           
           for j in range(n-1-i):
             if list1[j]>list1[j+1]: 
                  list1[j],list1[j+1]=list1[j+1],list1[j] 
                  swapped=True   
           if swapped==False:  
            break 
    return list1 
list1=[] 
n=int(input("How many elements??")) 
for i in range(n): 
    list1.append(int(input("Enter %d number:" %i))) 
 
print(f"before swapping:{list1}") 
 
list1=bubblesort(list1) 
print(f'After swapping:{list1}') 
 
x=list(range(1,10000)) 
plt.plot(x , [y*y for y in x] ) 
plt.title("Bubble Sort- Time Complexity is O(n\u00b2)") 
plt.xlabel("Input") 
plt.ylabel("Time") 
plt.show()
