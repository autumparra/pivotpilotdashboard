import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv()

EMAIL = os.getenv("GMAIL_EMAIL")
PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def fetch_recent_emails(limit=15):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()[-limit:]

        emails = []
        for eid in reversed(email_ids):
            res, msg = mail.fetch(eid, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    from_ = msg.get("From")
                    date = msg.get("Date")

                    emails.append({
                        "subject": subject,
                        "from": from_,
                        "date": date
                    })

        mail.close()
        mail.logout()
        return emails

    except Exception as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    emails = fetch_recent_emails()
    print(json.dumps(emails, indent=2))