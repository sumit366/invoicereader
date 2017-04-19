import outlook
mail = outlook.Outlook()
mail.login('sumitsngh366@outlook.com','Sumit#123.')
mail.inbox()

print(mail.getIdswithWord())
