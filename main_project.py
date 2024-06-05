import smtplib
import datetime as dt
import random

my_email = "shiwanshu1850510053@gmail.com"
my_password = "svjqwcaobpvgtvyx"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection

            # Login
            connection.login(user=my_email, password=my_password)

            # Send email
            connection.sendmail(
                from_addr=my_email,
                to_addrs="shiwanshu785@gmail.com",
                msg=f"Subject:Wednesday Motivation\n\n{quote}"
            )
            print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

