class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            sorted_words = "".join(sorted(word))
            if sorted_words not in results:
                results[sorted_words] = []
            results[sorted_words].append(word)
        return list(results.values())