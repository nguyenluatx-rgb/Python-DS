#Bai tap ve mang va danh sach

# khoi tao mang
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tinh tong
print(sum(arr))

# in tung phan tu
for i in range(len(arr)):
    print(arr[i])

# in tung phan tu (cach 2)
for x in arr:
    print(x)

# timf phan tu lon nhat
print(f"Max element: {max(arr)}")
# timf phan tu nho nhat
print(f"Min element: {min(arr)}")

# Them phan tu vao cuoi mang
arr.append(11)
print(arr)

# them phan tu vao vi tri dau danh sach
arr.insert(0, 0)
print(arr)

# xoa phan tu cuoi cung
arr.pop()
print(arr)

# xoa phan tu o vi tri bat ki
arr.pop()
print(arr)

# ham kiem tra xem phan tu co trong mang khong
print(5 in arr)

# chuong trinh sap xep mang tang dan
arr.sort()
print(arr)

# chuong trinh sap xep mang giam dan
arr.sort(reverse=True)
print(arr)


# Tao mot list random
import random
random_list = random.sample(range(1, 100), 10)
print(random_list)

random_list.sort()
print(random_list)
random_list.sort(reverse=True)
print(random_list)

# BAI TAP: Tao mot game don gian, game xi dach
# Luat choi:
# - Moi nguoi duoc chia 2 la bai ngau nhien
# - Neu co A (1) trong tay, nguoi choi duoc quyen lua chon A la 1 hoac 11 hoac 10 tuy vao so luong bai
    # Neu co 4 bai tro len, A se tinh la 1 diem
    # Neu co it hon 4 bai, nguoi choi duoc chon A la 1 hoac 11 hoac 10
# - Neu ai co AJ hoac AQ hoac AK hoac AA se:
    # - Kiem tra doi phuong co phai la AJ hoac AQ hoac AK hoac AA khong
    # - Neu khong phai, nguoi co AJ hoac AQ hoac AK hoac AA se thang luon
    # - Neu phai, se tinh tiep:
        # - Neu AA se chac chan thang AJ hoac AQ hoac AK
        # - Neu AQ AJ AK se hoa
# - Nguoi choi co tong diem gan 21 nhat se thang
# - Neu tong diem vuot qua  21 se thua
# - Nguoi choi phai tren 15 diem moi duoc tinh la hop le
# - Dealer chi can tren 14 diem la hop le
# - Dealer se rut them bai neu duoi 17 diem
# - Dealer se khong rut them bai neu tren hoac bang 17 diem
# - Nguoi choi co the chon rut them bai de tang diem
# - Nguoi choi co the khong rut bai nua neu da hai long voi diem cua minh
# - Nguoi choi thang se duoc cong 1 diem
# - Nguoi choi thua se bi tru 1 diem
# - Neu hoa se khong cong khong tru diem

# Implementation of the game
def deal_card():
    """Return a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)
def calculate_score(hand):
    """Calculate the score of a hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
def compare(player_score, dealer_score):
    """Compare the scores of the player and the dealer."""
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"
    if player_score == dealer_score:
        return "It's a draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
def play_game():
    print("Welcome to Blackjack!")
    player_hand = []
    dealer_hand = []
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())
    game_over = False
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"   Your cards: {player_hand}, current score: {player_score}")
        print(f"   Dealer's card: {dealer_hand}")
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                player_hand.append(deal_card())
            else:
                game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    print(f"   Your final hand: {player_hand}, final score: {player_score}")
    print(f"   Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()