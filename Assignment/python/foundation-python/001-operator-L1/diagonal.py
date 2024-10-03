def is_eligible_for_loan(gender, annual_income):
  if gender.lower()=="female" and annual_income<50000:
    print("Eligible")
  else:
    print("Not Eligible")
    