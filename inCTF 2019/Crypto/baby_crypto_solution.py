
# from secret import FLAG


lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab' , '_': 'bbbbb'} 

 
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if(letter != ' '): 
            cipher += lookup[letter] 
        else: 
            cipher += ' '
  
    return cipher 

def getKeysByValue(valueToFind):

    for (key,value) in lookup.items():
        if value == valueToFind:
            return key
    return ""

def decrypt(cipher):

    result = ""
    n=5
    #https://www.geeksforgeeks.org/python-split-string-in-groups-of-n-consecutive-characters/
    cipher_array = [(cipher[i:i+n]) for i in range(0, len(cipher), n)] 
    for data in cipher_array:
        result += getKeysByValue(data)
    print(result)


if __name__=='__main__':
    cipher="babbaaabaaababbaaabaabbbaabbaaaabaabbbbbbaabbabbbabbbbbaaababaaabbbaaabaabbabbbbabbbabbbbbbabbaabbbabaaabababbaaabb"
    decrypt(cipher)
    # cipher=encrypt(FLAG)

    # print 'Here take your cipher text: ',cipher
