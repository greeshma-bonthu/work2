import math
low=0
upp=100
count=1
print("hi, what is your name")
name=input()
print("hello" +str(name), "lets play a game")
print("Think of random number from 1 to 100, and I'll try to guess it!")
def guess_search(mid,low,upp,count):
      print("Is it" +str(mid)+ "?" "yes or no")
      ans=input()
      if(ans.lower()=="yes"):
         print("Yaay I got it in" +str(count)+  "try")
      else:
         print("Is the number larger than" +str(mid)+ "? yes or no")
         ans1=input()
         if(ans1.lower()=="yes"):
             guess_search(math.ceil((mid+upp)/2), mid, upp, count+1)
         else:
             guess_search(math.ceil((low+mid)/2), low, mid, count+1)


while True:
    answer = input("do you want to play?")
    if answer.lower() == 'yes':
        guess_search(upp // 2, low, upp, count)
    elif answer == 'no':
        break
    else:
        print("Enter correct input")




