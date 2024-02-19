def replace_duplicate_str(input_str, length=10):
    result = list(input_str)

    for i in range(len(result)):
        s = result[i]
        if s != '-':
            for j in range(max(i - length, 0), i):
                if result[j] == s:
                    result[i] = '-'
                    break

    return ''.join(result)

# 示例
input_str1 = "abcdefaxcqwertba"
output_str1 = replace_duplicate_str(input_str1)
print(f"Input: {input_str1}. Output: {output_str1}")

input_str2 = "abcdefaxcqwertba"
output_str2 = replace_duplicate_str(input_str2)
print(f"Input: {input_str2}. Output: {output_str2}")
