def threeNumberSum(array, targetSum):
    array.sort()
    results = []
    for i, _ in enumerate(array):
        left = i + 1
        right = len(array) - 1
        while left < right:
            sum_of_left_right = array[left] + array[right]
            if array[i] + sum_of_left_right == targetSum:
                results.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[i] + sum_of_left_right > targetSum:
                right -= 1
            elif array[i] + sum_of_left_right < targetSum:
                left += 1
    return results


if __name__ == '__main__':
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
