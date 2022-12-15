ace=11

def calculate_score(cards):
  if sum(cards) == 21:
    return 0
  elif ace in cards:
    if sum(cards)>21:
      for i in range (0,len(cards)):
        if cards[i]==ace:
          cards[i]=1
          return sum(cards)

  else:
    return sum(cards)
user_cards = [ 5, 10 ]
score = calculate_score(user_cards)
print(score)
