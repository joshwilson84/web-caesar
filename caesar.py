def rotate_string(text, rot):
    return "".join([x if x.isalpha() == False else
            chr(((ord(x)-97+rot)%26)+97) if x.islower() else
            chr(((ord(x)-65+rot)%26)+65) for x in text])
