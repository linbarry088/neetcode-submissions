class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        else:
            s_hash = {}
            t_hash = {}

            for val in s:
                if(not s_hash.get(val)):
                    s_hash[val] = 1
                else:
                    s_hash[val] += 1

            for val in t:
                if(not t_hash.get(val)):
                    t_hash[val] = 1
                else:
                    t_hash[val] += 1

            if(s_hash == t_hash):
                return True
            else:
                return False