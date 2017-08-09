def palindrom():
    s=raw_input("Enter the String :")
    s1=s[::-1]
    if s == s1:
        print(s,"is a Palindrom string !")
    else:
        print(s,"is not a Palindrom String !")


