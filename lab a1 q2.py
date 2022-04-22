print("Income must be entered to the nearest penny.")              
income=int(input("Enter your Income-"))
dep=int(input("Enter number of dependents-"))
taxinc=income-10000-(dep*3000)
print("The Taxable income is",taxinc)
tax=taxinc*0.20
print("The Tax to be paid is",tax)
