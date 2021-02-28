with open(file="mailing_list.csv", mode="a") as mailing:
    while 1 > 0:
        name = input("What is your name: ")
        email = input("What is your email: ")
        confirm_email = input("Confirm your email: ")
        if email == confirm_email:
            mailing.write(f"\n{name},{email}")
            break
        else:
            print("Emails don't match, try again")