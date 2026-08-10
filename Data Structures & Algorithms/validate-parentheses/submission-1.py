class Solution:
    def isValid(self, s: str) -> bool:
        record=[]
        for ch in s:
            if ch=='(' or ch=="{" or ch=='[':
                record.append(ch)
            
            else:
                if not record:
                    return False
                top=record.pop()

                if ch==')' and top!='(':
                    return False
                if ch=='}' and top!='{':
                    return False
                if ch==']' and top!='[':
                    return False

        return len(record)==0

        