def is_subset(arr1, arr2, m, n):

    # Iterate over each element in the second array
    for i in range(n):
        found = False

        # Check if the element exists in the first array
        for j in range(m):
            if arr2[i] == arr1[j]:
                found = True
                break

        # If any element is not found, return false
        if not found:
            return False

    # If all elements are found, return true
    return True


if __name__ == "__main__":
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    m = len(arr1)
    n = len(arr2)

    if is_subset(arr1, arr2, m, n):
        print("Yes")
    else:
        print("No")