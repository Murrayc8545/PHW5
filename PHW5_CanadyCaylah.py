# PHW5_CanadyCaylah

   # 7 Decemebr 2023

   # CTI-110 P5HW - Math Quiz

   # Caylah Canady

import random


def addRandom():
    
        num1=random.randint(0,100)
        
        num2=random.randint(0,100)
        
        print(f"{num1:>6}")
        print(f"+{num2:>5}")
        print("Enter answer")
        
        ans=int(input())
        while ans!=num1+num2:
        
                
                if ans<num1+num2:
                        print("Sorry, guess is too low.")
                else:
                        print("Sorry, guess is too high.")

                ans=int(input("try again : "))
        print("Congratulations!!!! your answer is correct.")

def subRandom():
    
        num1=random.randint(0,100)
        num2=random.randint(0,100)
        
        print(f"{num1:>6}")
        print(f"-{num2:>5}")
        print("Enter answer.")
        
        ans=int(input())
        
        while ans!=num1-num2:
        
                
                if ans<num1-num2:
                        print("Sorry, guess is too low.")
                else:
                        print("Sorry, guess is too high.")
                ans=int(input("try again : "))
        print("Congratulations!!!! your answer is correct.")
        
if __name__=="__main__":

        while 1:
                print("Welcome to Math Quiz")
                print("MAIN MENU")
                print("----------------------")
                print("1) Adding Random Numbers ")
                print("2) Subtracting Random Numbers")
                print("3) Exit")
                
                num=int(input("Please choose one of the menu options: "))
                
                if num==3:
                    
                        print("Thank you for playing...")
                        print("Bye!!")
                        break
                    
                if num==1:
                        addRandom()
                if num==2:
                        subRandom()
                        
