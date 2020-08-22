def main():
    name={"lindsay.ward@jcu.edu.au":"Lindsay Ward","abe@gmail.com":"Abe","jimbo546@hotmail.com":"Jim Boh" }
    email = input("Email:")
    while True:
        if email in name and email != " ":
         m = email.split("@")
         print("Is your name ",m[0],"? (Y/n)")
         userchoice = input("")
         if userchoice == "n".lower():
            print("Name:",name[email])
        else:
         print("Invaild")
        email=input('Email:')

main()