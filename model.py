import pandas
from sklearn.linear_model import LinearRegression
db= pandas.read_csv("Salary_Data.csv")
x= db["YearsExperience"]
x= x.values
x=x.reshape(30,1)
y= db["Salary"]
model = LinearRegression()
model.fit(x,y)
w= model.coef_
bias= model.intercept_
print()
print()
a= input("Enter your name: ")
print()
b= float(input("Enter years of experience: "))
print()
sal= float((b*w)+bias)
print("{}, your salary in our company is {:.2f} INR.".format(a,sal))

