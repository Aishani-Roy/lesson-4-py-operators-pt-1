amount=int(input("enter amount:"))
note100=amount//100
note50=(amount%100)//50
note10=((amount%100)%50)//10
print("amount of 100 notes are",note100)
print("amount of 50 notes are",note50)
print("amount of 10 notes are",note10)