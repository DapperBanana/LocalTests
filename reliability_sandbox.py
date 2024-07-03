letion(id='chatcmpl-9h410TzuLks6ryQE0knKAOo2ZwDa2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

player_health = 100
enemy_health = 50

def player_attack():
    return random.randint(5, 15)

def enemy_attack():
    return random.randint(3, 10)

def battle():
    global player_health, enemy_health
    
    while player_health > 0 and enemy_health > 0:
        print("Player Health:", player_health)
        print("Enemy Health:", enemy_health)
        print("1. Attack")
        print("2. Heal")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            damage = player_attack()
            enemy_health -= damage
            print(f"You hit the enemy for {damage} damage!")
            
            enemy_damage = enemy_attack()
            player_health -= enemy_damage
            print(f"The enemy hits you for {enemy_damage} damage!")
            
        elif choice == "2":
            heal = random.randint(10, 20)
            player_health += heal
            print(f"You heal yourself for {heal} HP.")
            
            enemy_damage = enemy_attack()
            player_health -= enemy_damage
            print(f"The enemy hits you for {enemy_damage} damage!")
            
        else:
            print("Invalid choice. Try again.")
            
    if player_health <= 0:
        print("You have been defeated. Game over.")
    elif enemy_health <= 0:
        print("You have defeated the enemy. Congratulations!")

battle()', role='assistant', function_call=None, tool_calls=None))], created=1720050566, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=294, prompt_tokens=21, total_tokens=315)