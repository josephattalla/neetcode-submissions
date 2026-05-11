class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        print(str1, str2)
        if len(str1) != len(str2):
            return False
        
        count = [0] * 26
        for i in range(len(str1)):
            count[ord(str1[i]) - ord('a')] += 1
            count[ord(str2[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = [] 

        for word in strs:
            if not groups:
                groups.append([word])
            else:
                grouped = False
                for i in range(len(groups)):
                    if self.isAnagram(groups[i][0], word):
                        groups[i].append(word)
                        grouped = True
                        break
                if not grouped:
                    groups.append([word]) 
        
        return groups