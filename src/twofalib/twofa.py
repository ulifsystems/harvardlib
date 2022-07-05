import telnyx
import random
import smtplib
from ulifutils.config import twofa


authcode = random.randint(12345, 100000)
telnyx.api_key = twofa.TNAPI
destination_number = twofa.USRNUM

def twoFA():
    telnyx.Message.create(
        from_ = twofa.NUM,
        to = destination_number,
        text = f"Hello, {twofa.NAME}. Your {twofa.DBA} auth code is {authcode}.",
    )
    telnyx.Message.create(
        from_ = twofa.NUM,
        to = destination_number,
        text = f"Remember, no one at {twofa.DBA} or Ulif Systems will ask for this code.",
    )

def check2FA(code):
    if code == authcode:
        return "OK"
    else :
        return "INVALID"

def noPhoneAccess():
    if twofa.EMAIL != "":
        sender = 'ulifsystems@gmail.com'
        receiver = twofa.EMAIL
        SUBJECT = f'Your {twofa.DBA} 2FA code'
        TEXT = f"""
        


        <div style="text-align: center">
        <h1>{twofa.DBA}</h1>
        <h2>{authcode}</h2>
        <p>is your {twofa.DBA}code</p>
        <p>Remember, no one at {twofa.DBA} or Ulif Systems will ask for this code.</p>
        <p style="font-size: 8px">If you did not request this code you can file a report <a href="{twofa.REPORTURL}">here.</a></p>.
        </div>
        """
        message = "Subject: {}\nMIME-Version: 1.0\ncontent-type: text/html\n\n{}".format(SUBJECT, TEXT)
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls()
        s.login("ulifsystems@gmail.com", "nrzyunrdwolypvhv")
        s.sendmail(sender, receiver, message) 