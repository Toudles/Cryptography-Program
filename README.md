For this part you will be writing a series of functions that can be used as part of a "cryptography" program.

You are going to write an "encoder / decoder" program that makes use of your six cryptographic functions. Begin by writing a program that continually asks the user to enter in an encoding pattern and a word to encode. The user should also be able to end the program using a sentinel value.

If the user chooses to encode a word you should do the following:

Ask the user for an "encoding pattern" string. This string will contain instructions on how to encode / decode a string. The valid commands that this string can contain are the following:
  - 'A' = add 1 character in between all characters
  - 'X' = delete 1 character in between all characters
  - 'F' = flip the string
  - 'U' = ASCII shift all characters by +1
  - 'D' = ASCII shift all characters by -1
  - 'L' = Shift all characters to the left by 1
  - 'R' = Shift all characters to the right by 1
  - Next, ask them to enter in a phrase that they want to encode.
  - Finally, apply the desired encoding pattern to their string, giving them feedback during the process. Apply the pattern one operation at a time, from left to right. Any invalid or unrecognized commands should be ignored.
