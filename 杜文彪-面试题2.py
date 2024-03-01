def replace_chars(input_str, k):
    output_str = ""
    for i in range(len(input_str)):
        if input_str[i] in input_str[max(0, i-k):i]:
            output_str += '-'
        else:
            output_str += input_str[i]
    return output_str

if __name__ == "__main__":
    input_str = "abcdefaxcqwertba"
    k = 10
    result = replace_chars(input_str, k)
    print(result)
