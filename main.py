email=input("Enter your eamil address").strip()  #    abc   =>>abc

#Slicing upto @ to find out the user Name

user_name=email[:email.index("@")]

#Slicing from the @ character 

domain_name=email[email.index("@")+1:]

print(f"The User Name is: {user_name}\nThe Domain Name is: {domain_name}")

