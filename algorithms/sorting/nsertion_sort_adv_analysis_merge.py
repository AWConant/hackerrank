def merge_sort(a):
    inv = 0

    if len(a) > 1:
        mid = len(a)//2
        left, right = a[:mid], a[mid:]

        inv += merge_sort(left)
        inv += merge_sort(right)

        i = j = k = 0
        left_len, right_len = len(left), len(right)

        while i < left_len and j < right_len:
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
                inv += mid-i
            k += 1

        while i < left_len:
            a[k] = left[i]
            i += 1
            k += 1

        while j < right_len:
            a[k] = right[j]
            j += 1
            k += 1

    return inv

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(merge_sort(a))
