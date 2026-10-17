class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_pieces = []
        for s in strs:
            encoded_pieces.append(f"{len(s)}#{s}")
        return "".join(encoded_pieces)

    def decode(self, s: str) -> list[str]:
        decoded_strs = []
        i = 0
        
        while i < len(s):
            delimiter_idx = s.find('#', i)

            length = int(s[i:delimiter_idx])
            i = delimiter_idx + 1
            decoded_strs.append(s[i:i + length])
            i += length
            
        return decoded_strs