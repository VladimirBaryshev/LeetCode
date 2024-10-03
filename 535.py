# 535. Encode and Decode TinyURL

class Codec:

    def __init__(self):
        
        self.base_url = "https://tiny.com/"
        self.long_to_short = dict()
        self.short_to_long = dict()


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        if longUrl not in self.long_to_short.keys():
            short_url = self.base_url + str(len(self.long_to_short)) + str(1)
            self.long_to_short[longUrl] = short_url
            self.short_to_long[short_url] = longUrl
            return short_url

        else:
            return self.long_to_short[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_long[shortUrl]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"

obj = Codec();
tiny = obj.encode(url) # returns the encoded tiny url.
print(tiny)
print(obj.decode(tiny)) # returns the original url after decoding it.
