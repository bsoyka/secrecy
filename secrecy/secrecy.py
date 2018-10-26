import sentry_sdk
import requests

sentry_sdk.init(
    "https://072345714651474581a92b0f9f9f2974@sentry.io/1307216",
    environment="prod",
    send_default_pii=True,
    release="secrecy@1.0.1"
)


class Secrecy:
    def __init__(self):
        try:
            self.user_ip = requests.get("https://api.ipify.org")
            with sentry_sdk.configure_scope() as scope:
                scope.user = {"ip_address": self.user_ip}
        except:
            pass
        self.characters = "'qicyQX$AV?[:eRn(&g!Zk.PtvT+F<GI>\"u\\lho@zpW~KL}N){]B^`Y#*Cj/UwMxOHDfasb,m%|JES;rd_"

    def encode(self, message, key):
        if abs(key) > len(self.characters):
            key = 1

        new_message = ""
        for character in message:
            if character in self.characters:
                position = self.characters.find(character)
                new_position = (position + key) % len(self.characters)
                new_character = self.characters[new_position]
                new_message += new_character
            else:
                new_message += character

        return new_message
