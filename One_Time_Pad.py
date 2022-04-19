
from secrets import choice   # Used to produce reliably random hex values
from string import printable # A list of printable characters to validate against
#  להדפסה קבלת רשימה של תווים
def generate_pad(length):
    """Generates a pad of random printable ASCII characters זורק באופן רנדומלי תווים הקסדצימלי באורך הפרמטר"""
    pad = ""
    for _ in range(length):
        # Choose a random printable character
        pad_letter =  choice(printable) # משתנה שתופס בתוכו רשימה רנדומלית של תווים מתוך טבלת האסקי
        pad += (pad_letter)#the length of the pad must to be same like length of the text
    save(pad, "pad.txt")
    return pad
#פונקציה שבונה קובץ טקסט בשם Pad שבתוכה יש את הטקסט שהמשתמש הזין

def save(text, path):
        with open(path, "w+") as output_file:
            output_file.write(text)

def encrypt(text, pad):
   # String variable that will contain all the shifted values
   try:
       ciphertext = ""
    #מקבלת טקסט + מפתח הצפנה שחייבת להיות באותו אורך של הטקס 
       for text_character, pad_character in zip(text, pad):
        # מרכז בתוכו ערך של כל אות בטקסט המקורי לדוגמא ('a' = 65)
           ascii_value= ord(text_character) ^ ord(pad_character)
        #מכיל בתוכו ערכים של הטקסט בטבלת האסקי ומחזירה אותו לתווים רנדומלים
           ciphertext_character = chr(ascii_value)
        # Add the generated character to the ciphertext
           ciphertext += (ciphertext_character)# משתנה זה מחזיק בתוכו את ההצפנה של הטקסט
       save(ciphertext, "ciphertext.txt")#קריאה לפונקציית סייב כדי שתפתח לנו קובץ חדש שמכיל בתוכו את הציפר
       return ciphertext     
   except ValueError: #כדוגמה טקס בעבית או כול שפה שלא נמצאת בטבלת הסקי(חריגה זו מטפלת באינפוט של המשתמש)
       print("YOUR INPUT IS INCORRECT!!! IT IS MUST TO BE IN ASCII TABLE")
   

def decrypt(pad, ciphertext):
    plaintext = ""
    for pad_character, ciphertext_number in zip(pad, ciphertext):
        ascii_value = ord(pad_character) ^ ord(ciphertext_number)
        plaintext += chr(ascii_value)
    save(plaintext, "originaltext.txt")
    return plaintext

def Security():
    try:
        print("*****************************************************")
        print("FIRST YOU HAVE TO INSERT TEXT.\nTHEN MUST CHOOSE TO ENCRYPT IT.\nONLY AFTER YOU WILL GET THE DECRIPTION TEXT")
        print("*****************************************************")
        print("WELCOME TO One-Time-Pad MENU")
        print("**************************")
        print("PRESS [1] TO GET A PAD\nPRESS [2] ENCRYPT TEXT\nPRESS [3] DECRYPT TEXT\nPRESS [0] TO EXIT PROGRAM")
        choise = 10
        while  choise!=0:
            if choise == 1:
                text=input("ENTER YOUR TEXT AND IT WILL BE ENCRYPT: ")
                pad = generate_pad(len(text))
                print(f"YOU GOT THE RANDOM PAD!!!: {pad}")
                print("---------------------------------------------------------")
            elif choise == 2:
                ciphertext = encrypt(text, pad)
                print(f"\nTHE ENCRYPTION TEXT IS: {ciphertext}")
                print("-----------------------------------------------------------")
            elif choise==3:
                plaintext = decrypt(pad, ciphertext)
                print(f"\nTHE DECRYPTION (WILL GIVE YOU BACK THE ORIGINAL TEXT): {plaintext}")
            elif choise ==0:
                print("EXIT")
            choise=int(input("CHOOSE FROM THE MENU: "))
    except ValueError:
        print("THE INPUT MUST BE A INTEGER")
    except TypeError:
        print("SORRY, WITHOUT ENCRYPTION TEXT WE CANT DO DECRYPTION...")
Security()



"dugmaot kelet pelet"
'''
***************
FIRST YOU HAVE TO INSERT TEXT.
THEN MUST CHOOSE TO ENCRYPT IT.
ONLY AFTER YOU WILL GET THE DECRIPTION TEXT
***************
WELCOME TO One-Time-Pad MENU
**********
PRESS [1] TO GET A PAD
PRESS [2] ENCRYPT TEXT
PRESS [3] DECRYPT TEXT
PRESS [0] TO EXIT PROGRAM
CHOOSE FROM THE MENU: 1
ENTER YOUR TEXT AND IT WILL BE ENCRYPT: London is in England
YOU GOT THE RANDOM PAD!!!: iE<ShY
KfW@J4]_	}MA

---------------------------------------------------------
CHOOSE FROM THE MENU: 2

THE ENCRYPTION TEXT IS: %*R7 7-"w)$1n,/n
-----------------------------------------------------------
CHOOSE FROM THE MENU: 3

THE DECRYPTION (WILL GIVE YOU BACK THE ORIGINAL TEXT): London is in England
CHOOSE FROM THE MENU: 0


'''
"dugma with error"
'''
>>> Security()
***************
FIRST YOU HAVE TO INSERT TEXT.
THEN MUST CHOOSE TO ENCRYPT IT.
ONLY AFTER YOU WILL GET THE DECRIPTION TEXT
***************
WELCOME TO One-Time-Pad MENU
**********
PRESS [1] TO GET A PAD
PRESS [2] ENCRYPT TEXT
PRESS [3] DECRYPT TEXT
PRESS [0] TO EXIT PROGRAM
CHOOSE FROM THE MENU: 1
ENTER YOUR TEXT AND IT WILL BE ENCRYPT: שלום מה קורה?
YOU GOT THE RANDOM PAD!!!: ?dO{Z ~x]<ccd
---------------------------------------------------------
CHOOSE FROM THE MENU: 2
YOUR INPUT IS INCORRECT!!! IT IS MUST TO BE IN ASCII TABLE

THE ENCRYPTION TEXT IS: None
-----------------------------------------------------------
CHOOSE FROM THE MENU: 3
SORRY, WITHOUT ENCRYPTION TEXT WE CANT DO DECRYPTION...
>>>
'''
