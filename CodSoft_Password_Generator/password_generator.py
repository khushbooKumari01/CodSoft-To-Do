import string
import random
#code for heading
print("-------------------------------------------------------------")
print("|                 Password  Generator                        |")
print("-------------------------------------------------------------")
if __name__ == "__main__":
    #this contains only lower case character
    password1 =string.ascii_lowercase

    #this contains only uppercase
    password2=string.ascii_uppercase

    #contains special character
    password3=string.punctuation

    #this contains only digits
    password4=string.digits

    password=int(input("Enter Your Password Length\n"))
    #list
    test=[]
    test.extend(list(password1))
    test.extend(list(password2))
    test.extend(list(password3))
    test.extend(list(password4))
    random.shuffle(test)
    print("".join(test[0:password]))








