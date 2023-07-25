# 2022-10-29 14:35:36

signal=True
while signal==True:
    # def start():
    import random
    from art import logo
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards=[]
    computer_cards=[]

        # for x in range(1,3):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    
     
    def add_card():
        user_score=sum(user_cards)
        computer_score=sum(computer_cards)
        
        def compare():
            if computer_score<17:
                computer_cards.append(random.choice(cards))
                add_card()
            elif computer_score>21:
                return (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou win🤩")
            elif user_score>computer_score:
                return (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou win 🤩")
            elif user_score<computer_score:
                return (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou lose 😥")
            elif user_score==computer_score:
                return (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nDraw") 

        ace=0
        if len(user_cards)==2:
            for y in user_cards:
                if y==11:
                    ace=y
                    if user_score==21:
                        print(f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou win 🤩")
        if len(computer_cards)==2:  
            for z in computer_cards:
                if z==11:
                    if computer_score==21:
                        print(f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou lose 😥")

        if user_score>21:
            if ace==11:
                check=(user_score-ace)+1
                if check>21:
                    print(f"Computer score  = {computer_score}\nYour score {(check)}\nYou lose 😥")
                elif check<=21:
                    another_card=(input(f"Computer score (card 1) = {computer_cards[0]}\nYour score {check}\nWould you like to add another card (2): ")).lower()
                    if another_card=="yes":
                        user_score.append(random.choice(cards))
                        add_card()
                    # elif another_card=="no":
                        
            elif ace!=11:
                print(f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou lose 😥")


        elif user_score<21:
            another_card=(input(f"Computer score (card 1) = {computer_cards[0]}\nYour score {(user_score)}\nWould you like to add another card (1) : ")).lower()
            if another_card=="yes":
                user_cards.append(random.choice(cards))
                if computer_score<17:
                    computer_cards.append(random.choice(cards))
                add_card()
            if another_card=="no":
                if computer_score<17:
                    computer_cards.append(random.choice(cards))
                    computer_score=sum(computer_cards)
                if computer_score>21 and user_score<=21:
                    print (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou win🤩")
                elif user_score>computer_score:
                    print (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou win 🤩")
                elif user_score<computer_score:
                    print (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nYou lose 😥")
                elif user_score==computer_score:
                    print (f"Computer cards: {computer_cards} score = {computer_score}\nYour cards : {user_cards} Your score {user_score}\nDraw") 
                   
    add_card()   
    option=input("Would you like to play again : ")
    if option=="no":
        signal=False
    elif option=="yes":
        from clear import clear
        clear()
 

         
# add_card()