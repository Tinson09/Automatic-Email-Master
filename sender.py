from bs4 import BeautifulSoup
from spreadsheet import SpreadSheet
from draft import Draft
from emailHandler import EmailHandler


def read_template_file(template_location):
    response = open(template_location)
    soup = BeautifulSoup(response.read(), 'html.parser')
    html_file = soup.prettify()
    return html_file


class Sender:
    def __init__(self, email_id, password, sheet_location, template_location):
        self.email_id = email_id
        self.password = password
        self.email_template = read_template_file(template_location)
        self.data = SpreadSheet(sheet_location).get_data()

    def send_emails(self):
        number_of_emails = self.data.get_count()
        draft = Draft(self.email_template)
        email = EmailHandler(self.email_id, self.password)
        for i in range(number_of_emails):
            row = self.data.get_row(i)
            email_draft = draft.get_draft(row)
            receiver_email = row.get_email()
            subject = row.get_subject()
            email.send(receiver_email, subject, email_draft)

        print("Failed Emails: {0}", email.get_failed_emails())
        print("Sucess Emails: {0}", email.get_successful_emails())
