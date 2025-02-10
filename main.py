from art import logo
from replit import clear
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def distribution(player, dealer):
  for card in range(0,2):
    player.append(cards[random.randint(0,len(cards) - 1)])
    dealer.append(cards[random.randint(0,len(cards) - 1)])

def show_cards(player, dealer):
  player_score = sum(player)
  deal_score = sum(dealer)
  print(f"Your cards: {player}, current score {player_score}")
  print(f"Computer's first card: {dealer[0]}")

def open_up(player, dealer):
  p_sum = sum(player)
  d_sum = sum(dealer)
  print(f"Your final hand: {player}, final score {p_sum}")
  print(f"Computer's final hand: {dealer}, final score {d_sum}")
  if p_sum > d_sum:
    print("You win!")
    blackjack()
  elif p_sum < d_sum and d_sum < 21:
    print("You lose!")
    blackjack()
  elif p_sum == d_sum:
    print("It's a draw.")
    blackjack()
  
def p_score(player):
  p_score = sum(player)
  return p_score

def dealer_got_card(player, dealer):
  d_score = sum(dealer)
  while d_score < 17:
    new_card = cards[random.randint(0, len(cards) - 1)]
    dealer.append(new_card)
    d_score = sum(dealer)
    if d_score > 21: 
      open_up(player,dealer)
      print("Opponent went over. You win.")
      blackjack()
    if d_score == 21:
      print("You lose.")
      blackjack()

def get_card(player,dealer):
  less_than_21 = True
  while less_than_21: 
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == "n":
      dealer_got_card(player = player, dealer = dealer)
      open_up(player,dealer) 
    elif user_choice == 'y':
      new_card = cards[random.randint(0, len(cards) - 1)]
      player.append(new_card)
      dealer_got_card(dealer, player)
      player_score = p_score(player)
      show_cards(player, dealer)
      if player_score > 21:
        open_up(player,dealer)
        print("You went over. You lose.")
        blackjack()
      if player_score == 21:
        open_up(player,dealer)
        print("You win!")
        blackjack()
  get_card()
def blackjack():
  game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
  if game == 'y':
    clear()
    print(logo)
  elif game == 'n':
    exit()

  player = []
  dealer = []

  distribution(player, dealer)
  show_cards(player, dealer)
  get_card(player, dealer)

blackjack()
