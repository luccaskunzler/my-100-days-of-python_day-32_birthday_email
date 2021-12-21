import random
import smtplib
import datetime as dt
import pandas


def send_letter(item):
    choice = f"letter_{random.randint(1,4)}.txt"
    # Method 1
    with open(choice) as letter:
        proc_letter = letter.readlines()
    proc_letter[0] = proc_letter[0].format(name=item[0])
    final_letter = "".join(proc_letter)

    # Method 2
    # with open(choice) as letter:
    #     proc_letter = letter.read()
    #     final_letter = proc_letter.replace("{name}", item[0])

    my_email = "****@mail.com"
    my_pass = "*********"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=item[1],
            msg=f"Subject:Happy Birthday\n\n{final_letter}",
        )


today = dt.datetime.now().day
this_month = dt.datetime.now().month

data = pandas.read_csv("birthdays.csv")

birthdays = []
for index, row in data.iterrows():
    if row.day == today and row.month == this_month:
        birthdays.append((row.person, row.email))

if len(birthdays) != 0:
    for item in birthdays:
        send_letter(item)
else:
    print("Nobody has birthday today")
