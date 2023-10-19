# Python3 code coming soon

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        while n>0:
            r=n%10
            sum=sum+r
            product=product*r
            n=n//10
        return product-sum
