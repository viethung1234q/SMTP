# SMTP

# Đoàn Việt Hưng - hungdoan2712@gmail.com

Your task is to develop a simple mail client that sends email to any recipient. Your client will need to
connect to a mail server, dialogue with the mail server using the SMTP protocol, and send an email
message to the mail server. Python provides a module, called smtplib, which has built in methods to send
mail using SMTP protocol. However, we will not be using this module in this lab, because it hide the
details of SMTP and socket programming.

In order to limit spam, some mail servers do not accept TCP connection from arbitrary sources. For the
experiment described below, you may want to try connecting both to your university mail server and to a
popular Webmail server, such as a AOL mail server. You may also try making your connection both from
your home and from your university campus.

# ADDITIONAL NOTE

In some cases, the receiving mail server might classify your e-mail as junk. Make sure you check the
junk/spam folder when you look for the e-mail sent from your client.
