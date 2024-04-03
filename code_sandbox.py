letion(id='chatcmpl-99yhUJA0JAmLZxMM7w45TVIsEcGX4', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

player = {
    "name": "Player",
    "health": 100,
    "attack": 10,
    "heal": 10
}

enemy = {
    "name": "Goblin",
    "health": 50,
    "attack": 5
}

def battle(player, enemy):
    print("A wild", enemy["name"], "appeared!")

    while player["health"] > 0 and enemy["health"] > 0:
        print("\nPlayer HP:", player["health"])
        print(enemy["name"], "HP:", enemy["health"])

        action = input("\nEnter 'a' to attack, 'h' to heal, or 'q' to quit: ")

        if action == 'a':
            enemy["health"] -= player["attack"]
            print("You attack the", enemy["name"], "for", player["attack"], "damage!")

            player["health"] -= enemy["attack"]
            print("The", enemy["name"], "attacks you for", enemy["attack"], "damage!")

        elif action == 'h':
            player["health"] += player["heal"]
            print("You heal yourself for", player["heal"], "HP!")

            player["health"] -= enemy["attack"]
            print("The", enemy["name"], "attacks you for", enemy["attack"], "damage!")

        elif action == 'q':
            print("You ran away from the battle!")
            break

        else:
            print("Invalid action! Try again.")

    if player["health"] <= 0:
        print("Game over! You have been defeated by the", enemy["name"])

    elif enemy["health"] <= 0:
        print("Victory! You have defeated the", enemy["name"])

# Start the battle
battle(player, enemy)', role='assistant', function_call=None, tool_calls=None))], created=1712165312, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=377, prompt_tokens=21, total_tokens=398)