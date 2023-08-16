from twilio.rest import Client
import pyotp

def generate_pin(accnt_no, cursor):

    # Twilio Account SID and Auth Token
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Generate OTP
    otp_secret = pyotp.random_base32()
    totp = pyotp.TOTP(otp_secret)
    otp = totp.now()

    # Recipient's phone number
    query = "SELECT Mob FROM details WHERE accnt_no = %s"
    values = (accnt_no,)
    cursor.execute(query, values)
    Mobile = cursor.fetchone()[0]


    # Send OTP via SMS
    message = client.messages.create(
        body=f"Your OTP is: {otp}",
        from_="your_twilio_number",  # Replace with your Twilio phone number
        to=Mobile
    )

    print("OTP sent successfully!")


def generate_pin():
    PIN = np.random.randint(1000,9999)
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "b319053@iiit-bh.ac.in"
    receiver_email = input("Enter email id : ")
    password = getpass("Enter your password : ")
    message = """\
        subject: OTP Verification


        Your OTP for verification process is {pin}.
        """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.format(pin=PIN))
    return PIN