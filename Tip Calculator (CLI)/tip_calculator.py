# # 2022-10-17 17:00:36
# # tip calculator
# #001

# 2022-10-17 17:00:36
# tip calculator
# 001

# Welcome user
print("Welcome to the tip calculator.")

# Take required inputs from the user
total=float(input("What was the total bill ? "))
split=int(input("How many people to split the bill ? "))
tip=int(input("What percentage tip would you like to give ?"))

total2=None
if tip==0 :
    total2=total
else:    
    total2=((tip/100)*total)+total
    
total3=None
if split==0:
    total3=total2
else :
    total3=total2/split   
    
if split==1 or split==0:
    print("The total you have to pay including tip is : ",total2)
elif split>1:
    print("The equal split for",split,"people including tip is",total3)   
else :
    print("Error Please Try Again ...")   

