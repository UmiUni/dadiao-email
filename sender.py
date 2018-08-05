import yagmail
import keyring

class EmailSender:

    _yag = None
    _host = None
    _subject = None
    _content = None

    def __init__(self, host_email, password):
        yagmail.register(host_email, password)
        self._yag = yagmail.SMTP(host_email)
        self._host = host_email
        self._subject = "What the fuck!"
        self._content = "Are you fucking stupid???"

    def compose(self, subject, content):
        self._subject = subject
        self._content = content

    def send(self, target_email):
        self._yag.send(self._host, subject=self._subject, contents=self._content)

    def groupSend(self, email_list):
        for email in email_list:
            self.send(email)


## Usage:
if __name__ == "__main__":
    host_email = "zeboli1@illinois.edu"
    password = "12345"
    sender = EmailSender(host_email, password)
    subject = "Da diao"
    content = "Da diao"
    sender.compose(subject, content)
    email_list = ['pkulizebo@gmail.com', 'pkuitachi@gmail.com']
    sender.groupSend(email_list)
