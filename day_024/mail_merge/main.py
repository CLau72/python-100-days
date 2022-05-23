#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Read in recipients into a list and strip out new line character:
with open ("/home/carson/code/python-100-days/day_024/mail_merge/Input/Names/invited_names.txt", encoding="UTF-8") as f:
    invited_guests = f.readlines()
    for index, name in enumerate(invited_guests):
        invited_guests[index] = name.strip()

#Read in the letter template
with open("/home/carson/code/python-100-days/day_024/mail_merge/Input/Letters/starting_letter.txt",encoding="UTF-8") as f:
    template = f.read()

#Write invite for everyone on guestlist
for name in invited_guests:
    with open(f"/home/carson/code/python-100-days/day_024/mail_merge/Output/ReadyToSend/{name}_invite.txt",mode="w", encoding="UTF-8") as f:
        letter = template.replace("[name]", name)
        f.write(letter)
