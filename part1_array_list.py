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