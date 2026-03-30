def two_sum(nums, target):
    prev_map = {} 
    for i, n in enumerate(nums):
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []

# 測試資料
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(f"結果索引: {result}") # 輸出: [0, 1]
