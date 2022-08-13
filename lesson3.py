num_years=int(input("Enter years employed..."))
num_children=int(input("Enter how many children..."))
salary_for_years=20*num_years
salary_for_children=30*num_children
salary=400+(salary_for_years)+(salary_for_children)
print(f"The total amount is {salary}. 400$ minimum wage + {salary_for_years} $ for {num_years} years experience + {salary_for_children} $ for {num_children} kids")
#print(salary_for_years,salary_for_children,salary)
#print("The total amount is",salary,".400$ minimum wage +",salary_for_years,"$ for",num_years, "years experience+",salary_for_children,"$ for",num_children,"kids")