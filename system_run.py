letion(id='chatcmpl-9lipHQaVv8jTI0bNH53zeefsPqnTL', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def roman_numeral(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman += numerals[i]
            num -= values[i]
        i += 1
    return roman

number = int(input("Enter a number: "))
if number <= 0 or number >= 4000:
    print("Number out of range. Please enter a number between 1 and 3999.")
else:
    print("Roman numeral:", roman_numeral(number))', role='assistant', function_call=None, tool_calls=None))], created=1721160755, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=197, prompt_tokens=20, total_tokens=217)