import smtplib
import os
from email.message import EmailMessage


class TargetMailer:
    def __init__(self, targets, dry=True):
        self.targets = targets
        self.sender = "apikey"
        self.password = os.getenv("SENDGRID_API_KEY")
        self.mail_server = "smtp.sendgrid.net"
        self.port = 587
        self.FROM = "CS40 Assassin <2026scs40assassin@gmail.com>"
        self.dry = dry

    def send_target(
        self,
        assassin,
        target,
        verbose=True,
    ):
        with smtplib.SMTP(self.mail_server, self.port) as server:
            server.starttls()
            server.login(self.sender, self.password)

            if verbose:
                print(f"Sending message for {assassin} to target {target}")

            template = f"""\
Welcome to CS40 Assassin, {assassin.name}!
Your target has been selected as {target.name}, good skill!
RULES HERE
"""

            msg = EmailMessage()
            msg["From"] = self.FROM
            # msg["To"] = assassin.email
            msg["To"] = "vedantmodi@gmail.com"
            msg["Subject"] = "Welcome to CS40! (Assassin)"
            msg.set_content(template)

            if not self.dry:
                server.send_message(msg)

            print(f"{'' if not self.dry else '[DRY] '}Sent message...")

    def send_mails(self, verbose=True):
        if verbose:
            print("Sending mails...")

        for assassin, target in self.targets.items():
            self.send_target(assassin, target, verbose)
