import email
import imaplib
import os
from invoice import views

import ctypes
import getpass

svdir = 'c:/Users/SUMIT/Desktop'

# select mail type
mail = imaplib.IMAP4_SSL('imap.outlook.com',993)
# prompt for username/email id
unm = 'sumitsngh366@outlook.com' # input('Please enter your email id : ')
# prompt for password
pwd = 'Sumit#123.'# getpass.getpass('Password : ')
# login to email
mail.login(unm,pwd)
# select type of email to read
mail.select("INBOX")


def loop():
    mail.select("INBOX")
    n = 0
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    if retcode == 'OK':
        for num in messages[0].split():
            n = n+1
            print(n)
            typ, data = mail.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_bytes(response_part[1])
                    if original.get_content_maintype() == 'multipart':  # multipart messages only
                        for part in original.walk():
                            if part.get_content_maintype() == 'multipart': continue
                            if part.get('Content-Disposition') is None: continue
                            filename = part.get_filename()
                            if filename is not None:
                                sv_path = os.path.join(svdir, filename)
                                if not os.path.isfile(sv_path):
                                    print(sv_path)
                                    fp = open(sv_path, 'wb')
                                    fp.write(part.get_payload(decode=True))
                                    fp.close()
                    print(original['From'])
                    data = original['Subject']
                    print(data)
                    typ, data = mail.store(num, "+Flags", "\\Seen")

    print(n)

if __name__ == '__main__':
    try:
        while True:
            loop()
    finally:
        print('Thanks')