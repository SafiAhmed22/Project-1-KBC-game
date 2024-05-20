questions=[['What is python symbol?','snake','monkey','snake'],['What is 2+2',2,4,4]]
lvl=[1000,2000,3000]
passed=0
amount=0
for i in questions:
    print(i[0])
    print("A. " + str(i[1]))
    print("B. " + str(i[2]))
    answer=input("Whats the answer? ")
    if( answer== str(i[-1])):
        print("---------You passed this level---------- ")
        passed+=1
        amount+=lvl[passed-1]
    else:
        print("--------you lost the game----------")
        break
    
print("you passed level: " + str(passed))
print("Your amount money is " + str(amount))