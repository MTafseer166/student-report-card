name=input("Enter your name:")


marks=float(input("Enter marks in phy:"))
marks1=float(input("Enter marks in math:"))
marks2=float(input("Enter marks in chem:"))
marks3=float(input("Enter marks in eng:"))


total_marks4=400
obtained_marks5=marks+marks1+marks2+marks3

percentage=(obtained_marks5/total_marks4)*100

print("obtained marks are:",obtained_marks5)
print("total percentage is:",percentage)

print(name.capitalize())

if(percentage>=80):
    print("Grade is A")
elif(percentage>=60):
    print("Grade is B")
elif(percentage>=40):
    print("Grade is C")
else:
    print("Ahh!Sorry.WE WANNA SEE YOU NEXT TIME ")
