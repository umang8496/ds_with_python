def onehop(list):
     # list=[(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]
     # [(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]
     
     result=[]
     tp=()
     
     if len(list)==1:
          return []

     for i in range(len(list)):
          for j in range(1,2):
               index=list[i][j]
               for k in range(0,len(list)):
                    for l in range(1):
                         if list[k][l]==index:
                              tp=(list[i][j-1],list[k][l+1])
                              if tp[0]==tp[1]:
                                   pass
                              else:
                                   result.append(tp)
    return result
