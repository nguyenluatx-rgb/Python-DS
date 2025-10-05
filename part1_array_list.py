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

# BAI TAP: Tao mot game don gian

user = []
admin = []

def calculate(list):
    total = 0
    for x in list:
        total += x
    return total

def init_game():
    for i in range(2):
        user.append(random.randint(1, 10))
        admin.append(random.randint(1, 10))
    print(f"User: {user}, total: {calculate(user)}")
    print(f"Admin: {admin}, total: {calculate(admin)}")

def game_turn(user, admin):
    # For user
    while (calculate(user) < 10):
        user.append(random.randint(1, 10))
        print(f"User: {user}, total: {calculate(user)}")
    
    # For admin
    while (calculate(admin) < 10):
        admin.append(random.randint(1, 10))
        print(f"Admin: {admin}, total: {calculate(admin)}")
    
    # Check winner, if total > 15 -> lose, esle check total
    user_total = calculate(user)
    admin_total = calculate(admin)
    if user_total > 15:
        print("User lose")
    elif admin_total > 15:
        print("Admin lose")
    else:
        if user_total > admin_total:
            print("User win")
        elif user_total < admin_total:
            print("Admin win")
        else:
            print("Draw")

init_game()
game_turn(user, admin)