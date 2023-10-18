# Python3 ,By :- Harsh Udai
# Que. Defanging an IP Address

lass Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=''
        for i in range(len(address)):
            if address[i] !=".":
                ans+=address[i]
            else:
                ans+="[.]"
        return ans
        
