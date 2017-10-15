# Hint: wt(kg) / ht(m) * ht(m)
def bmi(wt, ht):
    return wt / ht * ht


wt, ht = float(input("Enter weight: ")), float(input("Enter height: "))
print("Body Mass Index=%.2f" % (bmi(wt, ht)))
