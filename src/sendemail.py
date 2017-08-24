#-*- coding: UTF-8 -*-
#! /usr/bin/env python

from email.header import Header
from email.mime.text import MIMEText

import smtplib


def send(fromAddr, toAddr, smtpServer, content):
    msg = MIMEText('<html><body>' + content + '</body></html>', 'html', 'utf-8')
    msg['From'] = fromAddr
    msg['To'] = toAddr
    msg['Subject'] = Header('Redis Alter...', 'utf-8').encode()

    server = smtplib.SMTP(smtpServer)
    # server.set_debuglevel(1)
    # server.ehlo()
    # server.starttls()
    # server.login(from_addr, password)
    server.sendmail(fromAddr, toAddr, msg.as_string())
    server.quit()
