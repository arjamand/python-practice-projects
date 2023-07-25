# 2022-10-29 09:34:20
############### Blackjack Project #####################

def blackjack():
    from art import logo
    print(logo)
    option2=(input("Would you like to play blackjack : ")).lower()
    if option2=="no":
        exit()

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    import random
    def deal_card():
        """Choose a random card from list 'cards'"""
        return random.choice(cards)

    #cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())


    def calculate_score():
        """Find the sum of 'user cards'"""
        Sum=sum(user_cards)
        if Sum==21:
            return "BlackJack"
        # for x in user_cards():
        #     if x==11:

        elif Sum>21:
            for x in user_cards:
                if x==11:
                    user_cards.remove(11)
                else :


            # user_cards.remove(11)
            # user_cards.append(1)
                    return sum(user_cards)
        return sum(user_cards)

    # if calculate_score()==0 or calculate_score()==21:
    #     print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou win")
    # if calculate_score()>21 and (sum(computer_cards))<21:
    #     print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer win")
    # if (sum(computer_cards))>21 and calculate_score()<21:
    #     print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou win")
    def compare():
            user_cards.append(deal_card())
            calculate_score()
            if (sum(computer_cards))<17:
                computer_cards.append(deal_card())
            if calculate_score()>21 and (sum(computer_cards))<21:
                return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer win")
            elif calculate_score()>21 and (sum(computer_cards))>21 and calculate_score()==(sum(computer_cards)):
                return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nDraw !!!")
            else:
                new_score=(input(f"Your Score:{calculate_score()}\nComputer Score : card 1 = {computer_cards[0]}\nWould you like to add another card) : ")).lower()
                if new_score=="yes":
                    compare()
                elif new_score=="no":

                    # elif calculate_score()>21 and (sum(computer_cards))<21:
                    #     return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer win")
                    # elif calculate_score()>21 and (sum(computer_cards))>21:
                    #     return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nDraw !!!")
                    # if (sum(computer_cards))<17:
                    #     computer_cards.append(deal_card())
                    # if (sum(computer_cards))>21 and calculate_score()<21:
                    #     print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou wins ")
                    if calculate_score()==0 or calculate_score()==21:
                        return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou win")
                    elif calculate_score()>21 and (sum(computer_cards))<21:
                        return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer win")
                    elif (sum(computer_cards))>21 and calculate_score()<21:
                        return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou win")

                    elif calculate_score()>21 and (sum(computer_cards))<21 :
                        return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer Win !!!")
                    elif calculate_score()<(sum(computer_cards)) and (sum(computer_cards))<=21:
                        return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer Winn !!!")
                    elif calculate_score()>(sum(computer_cards))and calculate_score()<=21:
                        return (f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou Winn !!!")
                    # if calculate_score()<(sum(computer_cards)):
                    #     option=(input(f"Score : {calculate_score()}\nWould you like to add another card)\n>>> ")).lower()
                    #     if option=="yes":
                    #         user_cards.append(deal_card())
                    #         calculate_score()
                    #     elif option=="no":
                    #         print("You lose")
                    # elif 

    signal=True

    while int(calculate_score())<21 and (int(sum(computer_cards)))<21 and signal==True:
        option=(input(f"Your Score:{calculate_score()}\nComputer Score : card 1 = {computer_cards[0]}\nWould you like to add another card) : ")).lower()
        if option=="no":
            # if calculate_score()==0 or calculate_score()==21:
            #     print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou win")
            # if calculate_score()>21 and (sum(computer_cards))<21:
            #     print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer win")
            # if (sum(computer_cards))>21 and calculate_score()<21:
            #     print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou win")

            if (sum(computer_cards))<17:
                computer_cards.append(deal_card())
            if calculate_score()>(sum(computer_cards)):
                print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou wins ")
                signal=False
            elif calculate_score()==(sum(computer_cards)):
                print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nDraw !!!")
                signal=False
            elif (sum(computer_cards))>calculate_score():
                if (sum(computer_cards))>21:
                    print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nYou wins ")
                    signal=False
                else:
                    print(f"Computer Score : {(sum(computer_cards))}\nYour score : {calculate_score()}\nComputer Win !!!")
                signal=False
        elif option=="yes":
            print(compare())
            signal==False

    l_option3=(input("Would you like to play blackjack again : ")).lower()
    if l_option3=="yes":
        import clear
        clear.clear()
        blackjack()
            

        

blackjack()