'''
4) Get Input for variable name, score, department
Get Score for 100;
Divide 100/10
Sample Input: Aravind
78
Computer
Sample Output:
"My Name is Aravind"
"My Score is 7.8/10"
"My Department is Computer"
'''
a = str(input("name:"))
b = (int(input("score out of 100:")))/10
c = str(input("Dept:"))
print("My name is:", a)
print("My Score is:", b, "/10")
print("My Department is", c)
