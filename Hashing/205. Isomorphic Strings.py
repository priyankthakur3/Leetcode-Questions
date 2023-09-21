class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map= {}
        setChar = set()
        for i in range(len(s)):
            if(s[i] in map):
                if(map[s[i]]!=t[i]):
                    return False
            else:
                
                if(t[i] in setChar):
                    return False
                else:
                    map[s[i]]=t[i]
                    setChar.add(t[i])
        return True



#class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         sMap = {}
#         tMap = {}

#         for i in range(len(s)):
#             # if(s[i] not in sMap and t[i] not in tMap):
#             #     sMap[s[i]] = t[i]
#             #     tMap[t[i]]=s[i]
#             # elif((s[i] in sMap and sMap[s[i]]!=t[i]) or (t[i] in sMap and tMap[t[i]]!=s[i])):
#             #     return False

#             if(s[i] in sMap):
#                 if(sMap[s[i]] != t[i]):
#                     return False
#             else:
#                 sMap[s[i]]=t[i]

#             if(t[i] in tMap):
#                 if(tMap[t[i]] != s[i]):
#                     return False
#             else:
#                 tMap[t[i]]=s[i]



#             # if(s[i] not in sMap):
#             #     sMap[s[i]]= t[i]
#             # elif(s[i] in sMap):
#             #     if(sMap[s[i]]! != t[i]):
#             #         return False

#             # if(t[i] not in tMap):
#             #     tMap[t[i]]= s[i]
#             # elif():
#             #     return False


#         return True
            