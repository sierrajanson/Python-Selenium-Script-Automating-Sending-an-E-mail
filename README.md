# Python-Selenium-Script-Automating-Sending-an-E-mail
Automates sending an e-mail starting from Google's home page
------------------------------------------------------------
Created by Sierra Janson
December 2022

Purpose: Automates sending a G-mail starting from Google's home page.

User Requirements: Fork this repl.it and input your e-mail & password, and the e-mail & message for who you want to send a message to.

Notice: 
In the middle of the script, you will be prompted by the console to enter the bot-text to satisfy reCAPTCHA v3, as I have not been able to get around it yet.

PLEASE READ: you need to input information where directed in the code below in order for the script to work... as free repl.it accounts are public to all repl.it users, it is strongly recommended you use the log-in information for a g-mail that does not contain information personal to you ... I am not responsible for any harm that comes to users that resulted from not heeding the above warnings.

Made with Selenium library
------------------------------------------------------------
Future vision for this project:
- creating a simple GUI for a user to input their gmail/password & person2gmail/message instead of having to manually change it in the code
- getting around reCAPTCHA v3

More information about the project:
- website was loading too slowly for script, added time.sleep()s where necessary throughout the script to give the website time to load..if project throws an error try re-running the project again and it should be fine
  - values in time.sleep() are varied as I was experimenting to see if very specific     
  different time.sleep() values would mislead Google into thinking this session was an 
  authentic person logging in 

Shoutout: Thank you to CoopCodes in the replit Community for providing clear instructions to solve the issue of replit throwing errors for Chromedriver ... you can see the full post here: https://replit.com/talk/ask/Can-I-use-selenium/11566 
