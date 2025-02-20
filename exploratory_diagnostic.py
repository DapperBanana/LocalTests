
def ask_question(question):
    answer = input(question + ' (yes/no): ').lower()
    while answer not in ['yes', 'no']:
        print('Please enter yes or no.')
        answer = input(question + ' (yes/no): ').lower()
    return answer

def main():
    print('Welcome to the Personality Quiz!')

    answer1 = ask_question('Do you enjoy spending time outdoors?')
    answer2 = ask_question('Are you a social person?')
    answer3 = ask_question('Do you prefer staying at home rather than going out?')

    if answer1 == 'yes' and answer2 == 'yes':
        print('You are an outgoing and adventurous person!')
    elif answer1 == 'no' and answer3 == 'yes':
        print('You are a homebody and prefer quieter activities.')
    else:
        print('You have a balanced personality!')

if __name__ == '__main__':
    main()
