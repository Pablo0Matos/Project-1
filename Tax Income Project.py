#My First Project
TR = 0.20 #Tax Rate
SD = 10000.0 #Standar Deduction
DD = 3000.0 #Dependent Deduction 

GrossInc = float(input('Enter the gross income:'))

NumD = int(input('Enter the number of dependents: '))

D_Deduction = DD * NumD
GI = GrossInc - SD #CurrentIncome

IncomeTax = (GI - D_Deduction) * TR

print('\nThe income tax is:', IncomeTax)

print('\n\nGross income:', GrossInc,
      ('\nNumber of Depedents:'), NumD, 
      ('\nTax income:'), IncomeTax)

input('PRESS ENTER TO END')
