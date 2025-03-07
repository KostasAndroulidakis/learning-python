income = float(input("Enter the annual income: "))

LIMIT = 85528
TAX_RELIEF = 556.02
LOW_TAX = 0.18
HIGH_TAX = 0.32

if income <= LIMIT:
    if income*LOW_TAX < TAX_RELIEF:
        tax = 0
    else:
        tax = (income*LOW_TAX)-TAX_RELIEF
else:
    tax = 14839.02+((income-LIMIT)*HIGH_TAX)

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
