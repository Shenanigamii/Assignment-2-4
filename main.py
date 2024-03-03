# input statements
salary = float(input("Enter your salary: $"))
numdependents = float(input("Enter number of dependents: "))

# calculate taxes here

#dependentDeduction comes out of gross income before taxable income is calculated
  #example in assignment didn't calculate taxes correctly
  #if example numbers are needed, remove " - dependentDeduction" from associated lines

#Deduction for dependents
dependentDeduction = .025 * numdependents * salary
#State Tax withholding at 6.5%
stateTaxRate = .065
stateTax = (salary - dependentDeduction) * stateTaxRate
#Federal Tax withholding at 28%
federalTaxRate = .28
federalTax = (salary - dependentDeduction) * federalTaxRate
#Total Withheld
totalWithholding = stateTax + federalTax + dependentDeduction
#Total Takehome
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))