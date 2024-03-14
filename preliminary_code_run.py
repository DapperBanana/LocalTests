letion(id='chatcmpl-92mtZlMXoiWA7TRpCr1TClcScTqwU', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

num = int(input("Enter a number: "))
print(f"Roman numeral: {int_to_roman(num)}")', role='assistant', function_call=None, tool_calls=None))], created=1710451637, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f2ebda25a', usage=CompletionUsage(completion_tokens=185, prompt_tokens=20, total_tokens=205)