def linear_search(arr, target):
    steps= 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            print("Found after", steps, "steps")
            return
    print("Not Found after", steps, "steps")

arr=[10,20,30,40,50]

linear_search(arr, 30)
linear_search(arr, 50)
linear_search(arr,99)