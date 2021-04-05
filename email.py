import yagmail


class Email:
    def __init__(self, email_id, password):
        try:
            self.mail = yagmail.SMTP(email_id, password)
            self.is_authenticated = True
            self.successful_emails = []
            self.failed_emails = []
            print("Authenticated")
        except:
            self.is_authenticated = False
            print("Failed")

    def is_authenticated(self):
        return self.is_authenticated

    def send(self, receiver_mail, cc_mail_ids, subject, draft):
        assert (self.is_authenticated(), "Mail is not authenticated")
        try:
            self.mail.send(receiver_mail, subject, draft)
            self.successful_emails.append(receiver_mail)
        except:
            self.failed_emails.append(receiver_mail)

    def get_failed_emails(self):
        return self.failed_emails

    def get_successful_emails(self):
        return self.successful_emails
