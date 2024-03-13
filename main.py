from emailmodel import EmailModel

def main():
    print("Alô SMTP")
    email = EmailModel("joao","joao@gmail.com","fofoca","a dona continha disse","oi")
    print(email)
if __name__ == "__main__":
    main()
