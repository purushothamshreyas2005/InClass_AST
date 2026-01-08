print("SALARY GENERATING")
sal=int(input("Enter basic salary:"))
hra=0.20*sal
da=0.10*sal
tot=sal+hra+da
tax=0.05*tot
net=tot+tax
print("Total salary is",net)