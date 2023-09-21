def main():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19]
    target = 12
    low, high = 0, 1
    while(array[high] < target):
        low = high
        high = 2*high
    while(low <= high):
        mid = low + (high-low)//2
        if(target == array[mid]):
            return array[mid]
        elif(target > array[mid]):
            low = mid+1
        else:
            high = mid-1

    return -1
