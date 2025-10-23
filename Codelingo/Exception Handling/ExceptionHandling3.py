#use nested while loop
#is disviable b 2
    # run infinite 
    #print "bye"
valid=False
try:
    while not valid:
        num=int(input("Enter A Number: "))
        while num % 2 == 0:
                print("bye")
        valid=True
except SyntaxError as ex:
    print("Number is Invaid")