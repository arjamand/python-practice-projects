# 2022-10-17 17:00:36
# Life Expectancy Calculator
# 004

age=(int(input("What is your Age : ")))
years_remain=(90-age)
days_remain=(years_remain*365)
weeks_remain=(years_remain*52)
months_remain=(years_remain*12)
print(f"You Have {days_remain} days , {weeks_remain} weeks and {months_remain} months remain ..")
