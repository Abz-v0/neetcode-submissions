class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for s in strs:
            encoded_str.append(f"{len(s):04d}{s}")
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        original_list, i = [], 0

        while i < len(s):
            head_str = s[i: i + 4]
            word_len = int(head_str)

            i += 4

            actual_word = s[i: i + word_len]
            original_list.append(actual_word)

            i += word_len

        return original_list