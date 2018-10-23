import sentry_sdk
sentry_sdk.init("https://072345714651474581a92b0f9f9f2974@sentry.io/1307216")
characters = "'qicyQX$AV?[:eRn(&g!Zk.PtvT+F<GI>\"u\\lho@zpW~KL}N){]B^`Y#*Cj/UwMxOHDfasb,m%|JES;rd_"
message = input("Message: ")
key = int(input("Key (number between 1 and {}): ".format(len(characters))))
new_message = ""
for character in message:
    if character in characters:
        position = characters.find(character)
        new_position = (position + key) % len(characters)
        new_character = characters[new_position]
        new_message += new_character
    else:
        new_message += character
print("New message: {}".format(new_message))
