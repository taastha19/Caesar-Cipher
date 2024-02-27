# Encrypted Text (En(x)=(X + n) mod 26)     x-Letter
# Decrypted Text (Dn(x)=(X - n) mod 26)     n-Shift Key
# if Dn(x) is -ve, then add 26 to it.


alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabets:
            pos=alphabets.index(char)
            new_pos=(pos+shift_key)%26
            cipher_text+=alphabets[new_pos]
        else:
             cipher_text+=char
    print('\nText  after encryption : ',cipher_text)


def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabets:
            pos=alphabets.index(char)
            new_pos=(pos-shift_key)%26
            plain_text+=alphabets[new_pos]
        else:
            plain_text+=char
    print('\nText  after decryption : ',plain_text)

flag=False
while not flag:
    inp=input("\nType 'encrypt' for Encryption, Type 'decrypt' for Decryption - \n\n")
    text=input('\nType a message - ').lower()
    key=int(input('Type shift Key - '))

    if inp=='encrypt':
        encryption(plain_text=text,shift_key=key)
    elif inp=='decrypt':
        decryption(cipher_text=text,shift_key=key)

    play_again=input("Type 'yes' to continue, type 'no' to exit \n") 
    if play_again=='no':
        flag=True
        print("Visit again to play!!!")
        print("Bye, Have a nice Dayay!!!!!")












