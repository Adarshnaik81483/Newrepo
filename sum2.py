#program to add digits in a given number.
class adarsh():
    def add(num):
        s=0
        while(num>0):
            rem=num%10
            s=s+rem
            num=num//10
        print("sum:",s)
          
    b=add(12345)