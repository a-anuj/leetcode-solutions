class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for n in strs[1:]:
            while not n.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix