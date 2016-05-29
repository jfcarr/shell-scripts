#!/usr/bin/python
 
import imaplib
import sys
 
class MailHandler:
	def CheckUnread(self, username, password):
		imapConnection = imaplib.IMAP4_SSL('your.mailserver.com',993)
		imapConnection.login (username, password)
		imapConnection.select()
		mailCount = len(imapConnection.search(None, 'UNSEEN')[1][0].split())
		if mailCount > 0:
			print str(mailCount) + ' : ' + username
 
MyMail = MailHandler()
 
MyMail.CheckUnread('john.doe@mailserver.com','password')
