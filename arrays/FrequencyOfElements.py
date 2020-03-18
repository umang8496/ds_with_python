# Frequency of elements in an array
# Printing the Unique Elements of an array

def uniqueElements(array):
     unique=[]
     element=0
     
     for i in range(len(array)):
          element=array[i]
          appeared=0
          for j in range(0,i):
               if element==array[j]:
                    appeared=1
          if appeared==0:
               unique.append(element)

     print("original array :",array)
     print("distinct elements are :",unique)
     print()
     return unique


def frequency(array):
     distinct=uniqueElements(array)
     elementFrequency={}
     
     for i in range(len(distinct)):
          count=0
          for j in range(len(array)):
               if distinct[i]==array[j]:
                    count=count+1
          if count!=0:
               elementFrequency[distinct[i]]=str(count)

     print("elementFrequency :",elementFrequency)


# Driver Code
print("Enter some values in array")
array=[]

while True:
    x = input()
    if x != "":
        array.append(x)
    else:
         break
     
#uniqueElements(array)
frequency(array)
# End of Driver Code
