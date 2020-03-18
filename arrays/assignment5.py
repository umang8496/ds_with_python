
def Programming_Assignment_5():
     Courses,Students,Grades,l = [],[],[],[]
     c,c1,ind =0,0,0
     grade = dict(A = 10,AB = 9, B = 8, BC=7, C = 6, CD = 5, D = 4) 

     while True:
          x = input()
          if x != "EndOfInput":
             l.append(x)
          else: break

     for i in range(1,len(l)):
         if l[i]!= "Students":
              Courses.append(l[i])
              ind = i
         else: break

     for i in range(ind+2,len(l)):
         if l[i]!= "Grades":
              Students.append(l[i])
              ind = i
         else: break

     [Grades.append(l[i]) for i in range(ind+2,len(l))]
 
     for i in sorted(Students):
          for j in Grades:
             if (i[:(i.index("~"))]) in j:
                  c1+=1
                  c+= grade[(j.split("~")[-1])]
             if c1>1:print("{0:}~{1:}".format(i,round(c/c1,2)))
             elif c1==1:print("{0:}~{1:}".format(i,round(float(c),2)))
             else:print("{0:}~{1:}".format(i,c))
             c,c1 =0,0
#Students
#SLY2301~Hannah Abbott
#SLY2302~Euan Abercrombie
#SLY2303~Stewart Ackerley
#SLY2304~Bertram Aubrey
#SLY2305~Avery
#SLY2306~Malcolm Baddock
#SLY2307~Marcus Belby
#SLY2308~Katie Bell
#SLY2309~Sirius Orion Black

     
#Grades
#TRAN~1~2011-2012~SLY2301~AB
#TRAN~1~2011-2012~SLY2302~B
#TRAN~1~2011-2012~SLY2303~B
#TRAN~1~2011-2012~SLY2305~A
#TRAN~1~2011-2012~SLY2306~BC
#TRAN~1~2011-2012~SLY2308~A
#TRAN~1~2011-2012~SLY2309~AB
#CHAR~1~2011-2012~SLY2301~A
#CHAR~1~2011-2012~SLY2302~BC
#CHAR~1~2011-2012~SLY2303~B
#CHAR~1~2011-2012~SLY2305~BC
#CHAR~1~2011-2012~SLY2306~C
#CHAR~1~2011-2012~SLY2307~B
#CHAR~1~2011-2012~SLY2308~AB
#EndOfInput

#Output
#SLY2301~Hannah Abbott~9.5
#SLY2302~Euan Abercrombie~7.5
#SLY2303~Stewart Ackerley~8.0
#SLY2304~Bertram Aubrey~0
#SLY2305~Avery~8.5
#SLY2306~Malcolm Baddock~6.5
#SLY2307~Marcus Belby~8.0
#SLY2308~Katie Bell~9.5
#SLY2309~Sirius Orion Black~9.0

