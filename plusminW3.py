def plusMinus(arr):
    neg, pos, zero = 0,0,0
    for item in arr:
        if item < 0:
            neg += 1
        elif item == 0:
            zero += 1
        else:
            pos += 1
    print(f"{pos/len(arr):6f}\n{neg/len(arr):6f}\n{zero/len(arr):6f}")