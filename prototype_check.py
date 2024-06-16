letion(id='chatcmpl-9aYfEyQonTZFHlLXzTtNm4U5lvAZS', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    sy = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += sy[i]
            num -= val[i]
        i += 1
    return roman_num

# Getting input from user
num = int(input("Enter a number: "))
print("Roman numeral: ", int_to_Roman(num))', role='assistant', function_call=None, tool_calls=None))], created=1718500084, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=187, prompt_tokens=20, total_tokens=207)