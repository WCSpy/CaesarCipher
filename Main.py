# Made for Data Security Class

import os, colorama
from colorama import Fore

class Caesar():

    def __init__(self, CIPHERTEXT, PLAINTEXT, KEY) -> None:
        self.p          = Fore.MAGENTA
        self.r          = Fore.RESET
        self.g          = Fore.GREEN
        self.CIPHERTEXT = CIPHERTEXT
        self.PLAINTEXT  = PLAINTEXT
        self.KEY        = KEY
        self.shifts     = 26 # possible places to shift

    def ENCRYPT(self) -> str:
        encrypted = ""

        for character in self.PLAINTEXT:

            if character.isupper():
              characterIndex = ord(character) - ord('A') 
              shiftedChar = (characterIndex + self.KEY) % 26 + ord('A')
              char = chr(shiftedChar)
              encrypted += char              
            elif character.islower():
              characterIndex = ord(character) - ord('a') 
              shiftedChar = (characterIndex + self.KEY) % 26 + ord('a')
              char = chr(shiftedChar)
              encrypted += char
              
            elif character.isdigit():char = (int(character) + self.KEY) % 10 ; encrypted += str(char)
            else: encrypted += character

        return encrypted

    def DECRYPT_KEY(self) -> str:
        decrypted = ""

        for character in self.CIPHERTEXT:

            if character.isupper():
              characterIndex = ord(character) - ord('A') 
              shiftedChar = (characterIndex - self.KEY) % 26 + ord('A')
              char = chr(shiftedChar)
              decrypted += char
            elif character.islower():
              characterIndex = ord(character) - ord('a') 
              shiftedChar = (characterIndex - self.KEY) % 26 + ord('a')
              char = chr(shiftedChar)
              decrypted += char
  
            elif character.isdigit():char = (int(character) - self.KEY) % 10 ; decrypted += str(char)
            else: decrypted += character

        return decrypted

  
    def DECRYPT_ALL(self) -> str:
        decrypted = ""

        for shift in range(self.shifts):
          decrypted += f'[{self.g}{shift}{self.r}] '
          if shift < 10: decrypted+=' '

          for character in self.CIPHERTEXT:

              if character.isupper():
                characterIndex = ord(character) - ord('A') 
                shiftedChar = (characterIndex - shift) % 26 + ord('A')
                char = chr(shiftedChar)
                decrypted += char
              elif character.islower():
                characterIndex = ord(character) - ord('a') 
                shiftedChar = (characterIndex - shift) % 26 + ord('a')
                char = chr(shiftedChar)
                decrypted += char
  
              elif character.isdigit():char = (int(character) - shift) % 10 ; decrypted += str(char)
              else: decrypted += character
          decrypted += "\n"

        return decrypted


    def CLEAR(self): os.system('cls')

    def ASCII(self) -> None:
        self.CLEAR()
        print(f"""\n         {self.p}CAESAR CIPHER ENCRYPTION & DECRYPTION{self.r}            
            
            [{self.g}1{self.r}] Encryption (custom shift key)
            [{self.g}2{self.r}] Decryption (known shift)
            [{self.g}3{self.r}] Decryption (unknown shift)
        """)

    def SETUP(self) -> None:
        self.ASCII()
        method = str(input(f"[{self.p}*{self.r}] Method -> "))
        INPUT     = str(input(f"\n[{self.p}*{self.r}] Text -> "))
      
        if method == "1":
            KEY       = int(input(f"[{self.p}*{self.r}] Key --> "))
            Cipher    = Caesar(None, INPUT, KEY)
            TXTOUTPUT = Cipher.ENCRYPT()
            print(f"\n[{self.g}+{self.r}] Before -> {INPUT} ")
            print(f"[{self.g}+{self.r}] After  -> {TXTOUTPUT} \n\n")

        elif method == "2":
            KEY       = int(input(f"[{self.p}*{self.r}] Key --> "))
            Cipher     = Caesar(INPUT, None, KEY)
            TXTOUTPUT = Cipher.DECRYPT_KEY()
            print(f"[{self.g}+{self.r}] Decrypted -> {TXTOUTPUT} \n\n")

        elif method == "3":
            Cipher     = Caesar(INPUT, None, 0)
            TXTOUTPUT  = Cipher.DECRYPT_ALL()
            print(f"\n[{self.p}+{self.r}] All combinations (1-26) ↓\n")
            print(TXTOUTPUT)

CaesarCipher = Caesar('', '', 0)
CaesarCipher.SETUP()
