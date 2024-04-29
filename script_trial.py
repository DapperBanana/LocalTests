letion(id='chatcmpl-9JGwS4HfDls3ALrGneMDa58tT52n9', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Text-based spaceship game

import random

print("Space Adventure Game")
print("You are the captain of a spaceship on a dangerous mission.")
print("There are asteroids and enemy ships in your path.")
print("Navigate your way through space and reach your destination.")

health = 100
fuel = 50
distance_travelled = 0

while health > 0:
    print("\n--- Status ---")
    print("Health:", health)
    print("Fuel:", fuel)
    print("Distance Travelled:", distance_travelled)

    action = input("\nChoose an action: (1) Travel, (2) Refuel, (3) Quit\n")

    if action == "1":
        distance = random.randint(1, 10)
        health -= random.randint(1, 5)
        fuel -= random.randint(5, 10)
        distance_travelled += distance

        print("Travelled", distance, "parsecs.")
        if health <= 0:
            print("Your spaceship was destroyed by enemy ships. Game over!")
            break
        if fuel <= 0:
            print("You ran out of fuel and stranded in space. Game over!")
            break

    elif action == "2":
        fuel += random.randint(10, 20)
        print("Refueled spaceship.")
        
    elif action == "3":
        print("Thanks for playing. Goodbye!")
        break

    else:
        print("Invalid action. Please try again.")

    if distance_travelled >= 100:
        print("Congratulations! You have reached your destination.")
        print("You completed the mission. Well done!")
        break', role='assistant', function_call=None, tool_calls=None))], created=1714380384, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3b956da36b', usage=CompletionUsage(completion_tokens=338, prompt_tokens=21, total_tokens=359)