def mysplit(strng):
    # prepare a string
    word = ""
    # prepare a list to add the words
    words = []
    # remove whitespaces from the start and end of the string
    strng = strng.strip()
    # in case of empty string
    if strng == "":
        # return an empty list
        return words
    else:
        for char in strng:
            if not char.isspace():
                word = word + char          
            if char.isspace():
                words.append(word)
                word = ""
    # add last word after the end of the string
    words.append(word)
    return words

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
