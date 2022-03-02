#My First Project
TR = 0.20 #Tax Rate
SD = 10000.0 #Standar Deduction
DD = 3000.0 #Dependent Deduction 

GrossInc = float(input('Enter the gross income:'))

NumD = int(input('Enter the number of dependents: '))

D_Deduction = DD * NumD
GI = GrossInc - SD #CurrentIncome

IncomeTax = (GI - D_Deduction) * TR

print('\n\nThe gross income:', GrossInc,
      ('\nThe number of Depedents:'), NumD, 
      ('\nThe income tax is:'), IncomeTax)

input('PRESS ENTER TO END')
