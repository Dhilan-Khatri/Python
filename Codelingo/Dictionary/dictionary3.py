students = {
    
}

name=input("Enter Your name: ")
subject1=input("Enter Your Subject: ")
score1=int(input("Enter Score For that Subject: "))
subject2=input("Enter Your Subject 2: ")
score2=int(input("Enter Score For Subject 2: "))
subject3=input("Enter Your Subject 3: ")
score3=int(input("Enter Score For Subject 3: "))


students[name]={subject1:score1, subject2:score2, subject3:score3,}
print(students)
avg=0
sum=0

for key, value in students.items():
    for i,j in students[key].items():
        sum+=j
    avg=sum/3
    print(f"The Average is {avg} and sum is {sum}")