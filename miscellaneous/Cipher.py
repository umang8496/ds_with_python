
msg = input()
# msg = "All-convoYs-9-be:Alert1."    # Epp-gsrzsCw-3-fi:Epivx5.
counter = int(input())
encrypt = []

for ch in msg:
    char_val = ord(ch)
    if(char_val >= 65 and char_val <= 90):
        new_ch = counter % 26
        if((char_val + new_ch) > 90):
            encrypt.append(chr(char_val + new_ch - 26))
        else:
            encrypt.append(chr(char_val + new_ch))
    elif(char_val >= 97 and char_val <= 122):
        new_ch = counter % 26
        if((char_val + new_ch) > 122):
            encrypt.append(chr(char_val + new_ch - 26))
        else:
            encrypt.append(chr(char_val + new_ch))
    elif(char_val >= 48 and char_val <= 57):
        new_ch = counter % 10
        if((char_val + new_ch) > 57):
            encrypt.append(chr(char_val + new_ch - 10))
        else:
            encrypt.append(chr(char_val + new_ch))
    else:
        encrypt.append(chr(char_val))
    ## END
## END

print("".join(encrypt))
