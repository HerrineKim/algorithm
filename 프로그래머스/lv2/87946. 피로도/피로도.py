def permutate(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in permutate(ans, n-1):
                result.append([arr[i]]+p)

    return result


def solution(k, dungeons):
    duns = dungeons
    all_perms = permutate(duns, len(duns))
    max_dun = 0
    for perm in all_perms:
        power = k
        count = 0
        for dun in perm:
            if power >= dun[0]:
                power -= dun[1]
                count += 1
        if count > max_dun:
            max_dun = count
    return max_dun
