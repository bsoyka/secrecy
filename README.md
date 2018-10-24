# Secrecy
A simple and secure secret message encoder/decoder.
## How it works
Secrecy works in a pretty simple yet secure way.  Built into each copy of the program is a "base key," which is a random string of characters.
This program uses a variation of the Caesar cipher, which you can read more about [here](https://en.wikipedia.org/wiki/Caesar_cipher).  The only difference is that when substituting letters, the alphabet used as the key is in a random order, and is known as the base key.  For each letter in the message, its position in the base key is found.  Then, using the message key, which is a random number, each character is shifted using the base key by the number of positions specified by the message key.
Basically, to decode a message, you need to have the same copy of the program as the person who encoded the message, and the correct message key along with the encoded message.
## How to use
### Encoding
1. Enter the message you would like to encode.
2. Enter a message key, which is a random number between the numbers shown on screen.
3. The encoded message will appear on screen.
4. Make sure the person you are sending the message to has the same copy of the program as you.
5. Give them the encoded message and the message key.
### Decoding
1. Make sure you have the same copy of the program as the person who sent the message to you.
2. Enter the encoded message.
3. Enter the opposite of the message key to reverse the encoding.  For example, if the message key is 37, enter -37.
4. The decoded message will appear on screen.
# Errors
Errors that occur while the program is running should be reported automatically, but if anything goes wrong, feel free to contact me by [creating a GitHub issue](https://github.com/bsoyka/secrecy/issues/new/choose).
