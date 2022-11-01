class Codec:
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        startIndex = longUrl.find(".com")
        
        normalUrl =  longUrl[0:startIndex+5];
        toBeHashed = longUrl[startIndex+5:]
        
        combinedHashed = toBeHashed.split("/")
        tinyurl = "*".join(combinedHashed)
        
        finalHash = normalUrl+tinyurl
        
        return finalHash

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        startIndex = shortUrl.find(".com")
        
        normalUrl =  shortUrl[0:startIndex+5];
        hashedUrl = shortUrl[startIndex+5:]
        
        splitHashed = hashedUrl.split("*")
        longHashed = "/".join(splitHashed)
        
        return normalUrl+longHashed
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



