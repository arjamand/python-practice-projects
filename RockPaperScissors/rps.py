#004

# rock="x"
# paper="y"
# scissors="z"

r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
all_=[r,p,s]
random_=random.choice(all_)
#print(random_)
choice_1=(input("Choose ! (1) for rock ,(2) for paper,(3) for scissor.\n\n>>> "))
choice_1=int(choice_1)
if choice_1==1 and (random_)== s:
    print(F"your choice\n {r}\ncomputer choice {random_}\n you win")
elif choice_1==3 and random_==p:
     print(F"your choice\n {s}\ncomputer choice {random_}\n you win")
elif choice_1==2 and random_==r:
     print(F"your choice\n {p}\ncomputer choice {random_}\n you win")
else:
    print("you lose")