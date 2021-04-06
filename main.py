from sender import Sender

if __name__ == '__main__':
    email_id = input("Enter the sender Email address: ")
    password = input("Enter the sender Email Password: ")
    sheet_location = "Excel.xlsx"
    template_location = "template.html"

    sender = Sender(email_id, password, sheet_location, template_location)
    sender.send_emails()