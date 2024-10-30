def o_n3(i_range: int, j_range: int, k_range: int):
    for i in range(i_range):
        for j in range(j_range):
            for k in range(k_range):
                print(f"i: {i}, j: {j}, k: {k}")


def linear_search(arr: list[int], target: int) -> int:
    x = len(arr)
    for i in range(x):
        if arr[i] == target:
            return i
    return -1

if __name__=="__main__":
    print("Executing an O(i*j*k) function")
    o_n3(2,3,4)
    nums = [3, 2, 5, 4, 6, 7, 8, 9, 10]
    print("Executing an O(n) function")
    print(f"Linear search with target of 5: {linear_search(arr=nums, target=5)}")
    print(f"Linear search with target of 1: {linear_search(arr=nums, target=1)}")
