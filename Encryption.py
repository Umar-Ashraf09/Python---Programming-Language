
def encrypt (sentence):
    translation = ""
    for element in sentence:
        if element in "0":
            translation = translation + "~"
        elif element in "1":
            translation = translation + "#"
        elif element in "2":
            translation = translation + "$"
        elif element in "3":
            translation = translation + "!"
        elif element in "4":
            translation = translation + "@"
        elif element in "5":
            translation = translation + "%"
        elif element in "6":
            translation = translation + "*"
        elif element in "7":
            translation = translation + "&"
        elif element in "8":
            translation = translation + "^"
        elif element in "9":
            translation = translation + "?"

        elif element in "A":
            translation = translation + "B"
        elif element in "B":
            translation = translation + "C"
        elif element in "C":
            translation = translation + "D"
        elif element in "D":
            translation = translation + "E"
        elif element in "E":
            translation = translation + "F"
        elif element in "F":
            translation = translation + "G"
        elif element in "G":
            translation = translation + "H"
        elif element in "H":
            translation = translation + "I"
        elif element in "I":
            translation = translation + "A"
        elif element in "J":
            translation = translation + "Q"
        elif element in "K":
            translation = translation + "J"
        elif element in "L":
            translation = translation + "K"
        elif element in "M":
            translation = translation + "L"
        elif element in "N":
            translation = translation + "M"
        elif element in "O":
            translation = translation + "N"
        elif element in "P":
            translation = translation + "O"
        elif element in "Q":
            translation = translation + "P"
        elif element in "R":
            translation = translation + "S"
        elif element in "S":
            translation = translation + "T"
        elif element in "T":
            translation = translation + "U"
        elif element in "U":
            translation = translation + "V"
        elif element in "V":
            translation = translation + "W"
        elif element in "W":
            translation = translation + "X"
        elif element in "X":
            translation = translation + "Y"
        elif element in "Y":
            translation = translation + "Z"
        elif element in "Z":
            translation = translation + "R"

        elif element in "a":
            translation = translation + "b"
        elif element in "b":
            translation = translation + "c"
        elif element in "c":
            translation = translation + "d"
        elif element in "d":
            translation = translation + "e"
        elif element in "e":
            translation = translation + "f"
        elif element in "f":
            translation = translation + "g"
        elif element in "g":
            translation = translation + "h"
        elif element in "h":
            translation = translation + "i"
        elif element in "i":
            translation = translation + "a"
        elif element in "j":
            translation = translation + "q"
        elif element in "k":
            translation = translation + "j"
        elif element in "l":
            translation = translation + "k"
        elif element in "m":
            translation = translation + "l"
        elif element in "n":
            translation = translation + "m"
        elif element in "o":
            translation = translation + "n"
        elif element in "p":
            translation = translation + "o"
        elif element in "q":
            translation = translation + "p"
        elif element in "r":
            translation = translation + "s"
        elif element in "s":
            translation = translation + "t"
        elif element in "t":
            translation = translation + "u"
        elif element in "u":
            translation = translation + "v"
        elif element in "v":
            translation = translation + "w"
        elif element in "w":
            translation = translation + "x"
        elif element in "x":
            translation = translation + "y"
        elif element in "y":
            translation = translation + "z"
        elif element in "z":
            translation = translation + "r"
        elif element in " ":
            translation = translation + " "

        else:
            print("Wrong Input!")
            break

    return translation


def decrypt (sentence):
    translation = ""
    for element in sentence:
        if element in "~":
            translation = translation + "0"
        elif element in "#":
            translation = translation + "1"
        elif element in "$":
            translation = translation + "2"
        elif element in "!":
            translation = translation + "3"
        elif element in "@":
            translation = translation + "4"
        elif element in "%":
            translation = translation + "5"
        elif element in "*":
            translation = translation + "6"
        elif element in "&":
            translation = translation + "7"
        elif element in "^":
            translation = translation + "8"
        elif element in "?":
            translation = translation + "9"

        elif element in "B":
            translation = translation + "A"
        elif element in "C":
            translation = translation + "B"
        elif element in "D":
            translation = translation + "C"
        elif element in "E":
            translation = translation + "D"
        elif element in "F":
            translation = translation + "E"
        elif element in "G":
            translation = translation + "F"
        elif element in "H":
            translation = translation + "G"
        elif element in "I":
            translation = translation + "H"
        elif element in "A":
            translation = translation + "I"
        elif element in "Q":
            translation = translation + "J"
        elif element in "J":
            translation = translation + "K"
        elif element in "K":
            translation = translation + "L"
        elif element in "L":
            translation = translation + "M"
        elif element in "M":
            translation = translation + "N"
        elif element in "N":
            translation = translation + "O"
        elif element in "O":
            translation = translation + "P"
        elif element in "P":
            translation = translation + "Q"
        elif element in "S":
            translation = translation + "R"
        elif element in "T":
            translation = translation + "S"
        elif element in "U":
            translation = translation + "T"
        elif element in "V":
            translation = translation + "U"
        elif element in "W":
            translation = translation + "V"
        elif element in "X":
            translation = translation + "W"
        elif element in "Y":
            translation = translation + "X"
        elif element in "Z":
            translation = translation + "Y"
        elif element in "R":
            translation = translation + "Z"

        elif element in "b":
            translation = translation + "a"
        elif element in "c":
            translation = translation + "b"
        elif element in "d":
            translation = translation + "c"
        elif element in "e":
            translation = translation + "d"
        elif element in "f":
            translation = translation + "e"
        elif element in "g":
            translation = translation + "f"
        elif element in "h":
            translation = translation + "g"
        elif element in "i":
            translation = translation + "h"
        elif element in "a":
            translation = translation + "i"
        elif element in "q":
            translation = translation + "j"
        elif element in "j":
            translation = translation + "k"
        elif element in "k":
            translation = translation + "l"
        elif element in "l":
            translation = translation + "m"
        elif element in "m":
            translation = translation + "n"
        elif element in "n":
            translation = translation + "o"
        elif element in "o":
            translation = translation + "p"
        elif element in "p":
            translation = translation + "q"
        elif element in "s":
            translation = translation + "r"
        elif element in "t":
            translation = translation + "s"
        elif element in "u":
            translation = translation + "t"
        elif element in "v":
            translation = translation + "u"
        elif element in "w":
            translation = translation + "v"
        elif element in "x":
            translation = translation + "w"
        elif element in "y":
            translation = translation + "x"
        elif element in "z":
            translation = translation + "y"
        elif element in "r":
            translation = translation + "z"
        elif element in " ":
            translation = translation + " "

        else:
            print("Wrong Input!")
            break

    return translation


while True:
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWELCOME\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  to")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCryptIt")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tNow coding and decoding your message become easy with CryptIt.")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tJust select Encrypt or Decrypt."
          "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tEncrypt means coding = converting your simple text message to a "
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tcomplex set of text with special characters which makes "
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tdifficult for normal people to read."
          "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tDecrypt means decoding = converting complex set of text with "
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tspecial characters to simple text message. So, anyone can read it.")
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tNOTE: CryptIt is only for English language."
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tNOTE: You can only Decrypt or Decode those messages which were"
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  Encrypted or Coded using CryptIt."
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tNOTE: You can only Encrypt English alphabets and numbers."
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  Special characters are not allowed")
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tCode, Decode or Quit")
    ans = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tSelect one: ")
    ans = ans.lower()
    if ans in ("code", "decode", "quit"):
        if ans == "code":
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWhat do you want to code: ")
            fun_call = encrypt(user_input)
            print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tThis was the message you entered: {user_input}"
                  f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnd now your message is encrypted: {fun_call}")
            ans_1 = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tIf you want to continue then enter Yes."
                          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuit to exit: ")
            ans_1 = ans_1.lower()
            if ans_1 == "yes":
                continue
            elif ans_1 == "quit":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You! Please come again.")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
        elif ans == "decode":
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWhat do you want to decode: ")
            fun_call = decrypt(user_input)
            print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tThis was the message you entered: {user_input}"
                  f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnd now your message is decrypted: {fun_call}")
            ans_1 = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tIf you want to continue then enter Yes."
                          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuit to exit: ")
            ans_1 = ans_1.lower()
            if ans_1 == "yes":
                continue
            elif ans_1 == "quit":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You! Please come again.")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
        else:
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You! Please come again.")
            break

    else:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Selection! Try Again.")
        continue
    break










