letion(id='chatcmpl-9V0e4Ksty9TAtrc3XYUk5v6zfSTEz', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    
    roman_numeral = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral

number = int(input("Enter a number: "))
print("Roman numeral:", int_to_roman(number))', role='assistant', function_call=None, tool_calls=None))], created=1717177676, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=186, prompt_tokens=20, total_tokens=206)