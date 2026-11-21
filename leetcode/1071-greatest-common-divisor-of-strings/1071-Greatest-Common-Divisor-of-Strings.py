class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while str1 != str2:
            if len(str1) < len(str2):
                str1, str2 = str2, str1

            stack1 = list(str1)
            stack2 = list(str2)

            while stack2:
                a = stack1.pop()
                b = stack2.pop()

                if a != b:
                    return ""

            str1 = "".join(stack1)

        return str1