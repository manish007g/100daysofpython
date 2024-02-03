#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


####################################################################################################
with open("Input/Names/invited_names.txt") as data:
     new_data = data.readlines()
new_data1 = ""
for i in new_data:
    p = i.strip()
    with open("Input/Letters/starting_letter.txt", "r") as data:
        new_data1 = data.read().replace("[name]", p)

    with open(f"Output/ReadyToSend/letter_{p}.txt", mode="w") as data:
        data.write(new_data1)

