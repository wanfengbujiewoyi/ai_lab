import random
while True:
    number_answer=random.randint(1,100)
    number_of_times=0
    while number_of_times<7:
        number_of_times+=1
        number_user=input("please give me a number of 1-100")
        if number_user=="q":
            print("game over")
            exit()
        else:
            number_user=int(number_user)    
            if number_user==number_answer:
                print(f"good you are right")
                break
            elif number_user<number_answer:
                print(f"Its small")
            else:
                print(f"Its big")    
    else:
        print(f"your number of times is over,the answer is{number_answer}")        
    again=input("enter is again,q is over")
    if again=="q":
       print("game over")
       break
