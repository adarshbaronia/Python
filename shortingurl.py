import random
import string


class ShortURL:

    def __init__(self):
        self.d = dict()

    def getShortURL(self, longURL):
        length = random.randint(6,10)

        chars = string.ascii_lowercase
        shortURL = ''.join(random.choice(chars) for i in range(length))

        if shortURL in self.d:
            return getShortURL(longURL)
        else:
            self.d[ShortURL] = longURL

        r = 'https://www.shortURLs.com/' + shortURL
        return r

    def getLongURL(self, ShortURL):
        k = ShortURL[30:]

        if k in self.d:
            return self.d[k]
        else:
            return None

s = ShortURL()

print(s.getShortURL("https://dilbertblog.typepad.com/the_dilbert_blog/2007/06/the_day_you_bec.html"))


