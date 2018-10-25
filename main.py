import sentry_sdk
import requests

# Error tracking setup

## Initialize the Sentry SDK

sentry_sdk.init(
    "https://072345714651474581a92b0f9f9f2974@sentry.io/1307216",
    environment = "prod",
    send_default_pii = True,
    release = "secrecy@1.0.1"
)

## Get user IP address

try:
    user_ip = requests.get("https://api.ipify.org")
except:
    pass

## Set Sentry SDK scope with user IP address

with sentry_sdk.configure_scope() as scope:
    scope.user = {"ip_address": user_ip}

# Start secret message encoder/decoder

characters = "'qicyQX$AV?[:eRn(&g!Zk.PtvT+F<GI>\"u\\lho@zpW~KL}N){]B^`Y#*Cj/UwMxOHDfasb,m%|JES;rd_"
message = input("Message: ")
try:
    key = int(input("Key (number between 1 and {}): ".format(len(characters))))
except:
    print("Invalid key. Defaulting to 1")
    key = 1
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
