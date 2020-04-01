#!/usr/bin/env python3
"""
A tiny email program to send spam to someone
"""

import os
import smtpLib

# use os to import my email address and password

EMAIL_ADDR = os.environ['EMAIL_ADDRESS']
EMAIL_PWD = os.environ['EMAIL_PWD']

# Use smtplib import to send email

with smtpLib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDR, EMAIL_PWD)

    # compose the email message
    subject = "This is a test"
    body = "Did this work? It did? Neat!"
    msg = f"Subject: {subject}\n\n{body}"

    # send the email
    smtp.sendmail(EMAIL_ADDR, 'kenzie.academy@mailinator.com', msg)
