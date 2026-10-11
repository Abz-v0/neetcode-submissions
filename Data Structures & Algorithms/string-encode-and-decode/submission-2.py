class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        original_list, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])

            i = j + 1

            original_list.append(s[i: i + word_len])

            i += word_len

        return original_list
