class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            sorted_words = "".join(sorted(word))
            if not sorted_words in results:
                results[sorted_words] = []
                results[sorted_words].append(word)
            else:
                results[sorted_words].append(word)
        return list(results.values())