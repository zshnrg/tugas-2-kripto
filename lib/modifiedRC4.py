class rc4:
    # Modified in KSA generation with playfair modification

    def __init__(self, key):
        self.key = key

    def KSA(self):
        key = [ord(c) for c in self.key]
        S = list(range(256))
        j = 0
        for i in range(256):
            # swapping with playfair modification
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]
        return S
    
    def PRGA(self, S, plaintext):
        i = 0
        j = 0
        key = []
        for c in plaintext:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            key.append(S[(S[i] + S[j]) % 256])
        return key
    
    def encrypt(self, plaintext):
        S = self.KSA()
        key = self.PRGA(S, plaintext)
        return bytes([p ^ k for p, k in zip(plaintext, key)])
    
    def decrypt(self, ciphertext):
        S = self.KSA()
        key = self.PRGA(S, ciphertext)
        return bytes([c ^ k for c, k in zip(ciphertext, key)])