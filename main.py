quit = ""
lingo_text = ""

english = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "?", "!", ",", ".", " "]

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-","...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", "..--..", "-.-.--", "--..--", ".-.-.-", " "]

base64 = [""]

def englishToMorse(text):
  new_text = ""
  for i in text:
    for j in range(41):
      if i == english[j]:
        new_text += morse_code[j] + " "
  return new_text


def englishToBinary(text):
  new_text = ""
  for i in text:
    new_text += bin(ord(i)) + " "
    if ord(i) < 60:
      new_text = new_text.replace("b", "0")
    else:
      new_text = new_text.replace("b", "")
  return new_text


print("Welcome to Suprose!")
while quit != "yes":
  print("What language do you want to translate from?")
  print("""English
Morse code
Binary
Base64
Quit""")
  print("---------------------------------------------------------------------")
  lingo_input = input()
  print("---------------------------------------------------------------------")
  if lingo_input == "english" or lingo_input == "English":
    print("I thought so. Now, what language do you want to translate to?")
    print("""Morse code
Binary
Base64""")
    print("---------------------------------------------------------------------")
    lingo_language = input()
    print("---------------------------------------------------------------------")
    if lingo_language == "morse code" or lingo_language == "Morse code":
      print("Morse code, eh? Alright, now enter the text that you want to translate.")
      print("---------------------------------------------------------------------")
      lingo_text = input().upper()
      lingo_output = englishToMorse(lingo_text)
      print("---------------------------------------------------------------------")
      print("This is your translated output!")
      print(lingo_output)
      print("If you used any slashes or colons or other things that aren't the alphabet, simple punctuation, or 0 to 9, then that was deleted. Sorry!")
      print("---------------------------------------------------------------------")
    elif lingo_language == "binary" or lingo_language == "Binary":
      print("I see you also like this base. Anyways, enter the text that you want to translate.")
      print("---------------------------------------------------------------------")
      lingo_text = input()
      lingo_output = englishToBinary(lingo_text)
      print("---------------------------------------------------------------------")
      print("This is your translated output!")
      print(lingo_output)
      print("---------------------------------------------------------------------")