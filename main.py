import smtplib

# Email credentials
my_email = "shiwanshu1850510053@gmail.com"
my_password = "svjqwcaobpvgtvyx"

# SMTP setup and email sending
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection

        # Login
        connection.login(user=my_email, password=my_password)

        # Send email
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shiwanshu785@gmail.com",
            msg="Subject:Hello\n\nHello Shivanshu Singh thanks for update "
        )
        print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")
