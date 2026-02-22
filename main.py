##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime, pandas, smtplib, random, os

now = datetime.datetime.now()
day = now.today().date()
email = "mettabia862@gmail.com"
password = "ljtk avnq hhuj ipyz"

data = pandas.read_csv("./birthdays.csv")
todays_month=now.month
today = now.day



year = data["year"]
month = data["month"]
day = data["day"]

for i in range(len(data)):
    #
    if month[i] == todays_month and day[i] == today:
        letter = random.choice(["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=data["email"][i], msg="Subject: Happy Birthday!! \n\n" + open(letter).read().replace("[NAME]", data["name"][i]))

