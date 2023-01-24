"""
I have created a program where the teacher will put:
-their students with their respective grades
-the positives or negatives they have (which will be defined what they add or subtract later)
-the average will be calculated along with the positive/negative
-rounded off (in case of being close to passing)
-finally the passes will be displayed on the screen.
"""

#IMPORT
import numpy as np

##
print()
subject=input("What subject is being evaluated?: ")
print()
print("You will be asked for the names of your students. Write '0' to finish.")
print()

students= np.array([])
name= input("Student name: ")

#STUDENT'S ENTRY
while name!= "0":
    students=np.append(students,name)
    name= input("Student name: ")

print("The following students have been introduced: {}".format(students))
right= input("right? Yes/No: ").upper()

#STUDENTS ENTRY (WRONG)
while right!="YES":
    students= np.array([])
    print("you have marked that it is NOT correct, you will be asked again for the names of your students.")
    print()
    print("You will be asked for the names of your students. Write '0' to finish.")
    print()
    name= input("Student name: ")

    while name!= "0":
        students=np.append(students,name)
        name= input("Student name: ")

    print("The following students have been introduced: {}".format(students))
    right= input("right? Yes/No: ").upper()
print()
##

#NOTE ENTRY
g1=np.array([])
g2=np.array([])
g3=np.array([])
for student in students:
    grade= float(input("Enter the 1st note of {}: ".format(student)))
    g1=np.append(g1,grade)
    grade2= float(input("Enter the 2nd note of {}: ".format(student)))
    g2=np.append(g2,grade2)
    grade3= float(input("Enter the 3rd note of {}: ".format(student)))
    g3=np.append(g3,grade3)
    print()
print()

print("The following notes have been introduced:")
for student in range(len(students)):
    print("-",students[student], ": ",g1[student],g2[student],g3[student])

right= input("right? Yes/No: ").upper()

#NOTE ENTRY (WRONG)
while right!="YES":
    print("you have marked that it is NOT correct, you will be asked again for the student's notes.")
    print()

    g1=np.array([])
    g2=np.array([])
    g3=np.array([])
    for student in students:
        grade= float(input("Enter the 1st note of {}: ".format(student)))
        g1=np.append(g1,grade)
        grade2= float(input("Enter the 2nd note of {}: ".format(student)))
        g2=np.append(g2,grade2)
        grade3= float(input("Enter the 3rd note of {}: ".format(student)))
        g3=np.append(g3,grade3)
        print()
    print()

    print("The following notes have been introduced:")
    for student in range(len(students)):
        print("-",students[student], ": ",g1[student],g2[student],g3[student])
    print()
    right= input("right? Yes/No: ").upper()
print()
##

#CALCULATION OF AVERAGES AND POSITIVES/NEGATIVES
print("positive/negative count: ")
positives=np.array([])
negatives=np.array([])
vPosi= float(input("How much is a POSITIVE (+) worth?: "))
vNega= float(input("How much is a NEGATIVE (-) worth?: "))
print()

for student in students:
    cPosi=float(input("How many positives (+) does {} have?: ".format(student)))
    cNega=float(input("How many negatives (-) does {} have?: ".format(student)))
    
    positive= cPosi*vPosi
    negative= cNega*vNega

    positives= np.append(positives,positive)
    negatives= np.append(negatives,negative)
    print()

print("Value: positive: {} | Negative: {}".format(vPosi,vNega))
for i in range(len(students)):
    student= students[i]
    score= positives[i]-negatives[i]
    print("- {}: {} points".format(student,score))
    print()
right= input("right? Yes/No: ").upper()

#COUNT (WRONG)
while right!="YES":
    positives=np.array([])
    negatives=np.array([])
    vPosi= float(input("How much is a POSITIVE (+) worth?: "))
    vNega= float(input("How much is a NEGATIVE (-) worth?: "))
    print()

    for student in students:
        cPosi=float(input("How many positives (+) does {} have?: ".format(student)))
        cNega=float(input("How many negatives (-) does {} have?: ".format(student)))
        
        positive= cPosi*vPosi
        negative= cNega*vNega

        positives= np.append(positives,positive)
        negatives= np.append(negatives,negative)
        print()

    print("positives/negatives count: ")
    print("Value: positive: {} | Negative: {}".format(vPosi,vNega))
    for i in range(len(students)):
        student= students[i]
        score= positives[i]-negatives[i]
        print("- {}: {} points".format(student,score))
        print()
    right= input("right? Yes/No: ").upper()

total= positives - negatives #final score.
print()
##

print("total average: ")
average= float(input("How many points are needed to pass?: "))
tAverage= ((g1+g2+g3)/3)+total

print("final grades: ")
for i in range(len(tAverage)):
    student=students[i]
    grade=tAverage[i]
    print("-",student,":",grade)
print()

print("rounding up: ")
vBool1= (tAverage>=(average-0.2))&(tAverage<average) #round up
tAverage[vBool1]=average 
vBool= tAverage>=average #pass condition
passed= students[vBool]
print("Students who have passed '{}': ".format(subject), passed)
##
