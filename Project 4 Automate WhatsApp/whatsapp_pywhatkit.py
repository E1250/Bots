import pywhatkit 


phone_number = input("Enter your number")
# pywhatkit.sendwhatmsg("+201118015502", "Hello World", 9, 59) # send message to whatsapp number, message, hour, minute

# send message to whatsapp number, message, hour, minute
pywhatkit.sendwhatmsg("+201118015502", "Hello World", 10, 4,2,True ,2)


group_id = input("Enter Group Id")
pywhatkit.sendwhatmsg_to_group(group_id, "Hello World", 10, 4,2,True ,2) # send message to whatsapp group, message, hour, minute
