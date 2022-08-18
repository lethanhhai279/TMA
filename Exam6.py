a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_final_a = []
list_final_b = []
def quest_a(a):
    for i in range(len(a)):
        if a[i] < 5:
            list_final_a.append(a[i])
    print(list_final_a)
quest_a(a)
def quest_b(a):
    u_in = int(input("Nhap so: "))

    for j in range(len(a)):
        if a[j] < u_in:
            list_final_b.append(a[j])
    print(list_final_b)
quest_b(a)
