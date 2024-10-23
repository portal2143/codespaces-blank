def start_game():
    print("Welcome to the Mysterious Cave Adventure!")
    print("You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears.")
    print("You have no memory of how you got here. As you get up and dust yourself off, you notice two paths ahead:")
    print("1. To your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water.")
    print("2. To your right, a wider passage seems to have some light coming from it. You hear distant whispers echoing from within.")
    
    first_choice()

def first_choice():
    choice = input("Do you want to go left or right? (left/right): ").strip().lower()
    
    if choice == 'left':
        narrow_tunnel()
    elif choice == 'right':
        wider_passage()
    else:
        print("Not a choice you can make. Please choose 'left' or 'right'.")
        first_choice()

def narrow_tunnel():
    print("\nYou brave the narrow, dark tunnel, following the sound of rushing water.")
    print("As you go deeper, the tunnel starts to slope downwards and becomes increasingly slippery.")
    print("You have two options:")
    print("1. Try to navigate carefully to avoid slipping.")
    print("2. Rush forward, eager to reach the water.")
    
    choice = input("What do you want to do? (navigate/rush): ").strip().lower()
    
    if choice == 'navigate':
        ending_safe_crossing()
    elif choice == 'rush':
        ending_slip_fall()
    else:
        print("Nope. Can't do that. Please choose 'navigate' or 'rush'.")
        narrow_tunnel()

def wider_passage():
    print("\nYou choose to investigate the wider passage, drawn by the mysterious light and whispers.")
    print("As you proceed, the light reveals a shimmering pool of water.")
    print("You can either:")
    print("1. Approach the pool to inspect it.")
    print("2. Ignore the pool and continue down the path.")
    
    choice = input("What do you want to do? (approach/continue): ").strip().lower()
    
    if choice == 'approach':
        pool_choice()
    elif choice == 'continue':
        ending_wandering_lost()
    else:
        print("That's not an option that you can take. Please choose 'approach' or 'continue'.")
        wider_passage()

def pool_choice():
    print("\nAs you approach the shimmering pool, you feel a strange energy surrounding you.")
    print("You have two options:")
    print("1. Touch the water.")
    print("2. Look for something nearby before touching it.")
    
    choice = input("What do you want to do? (touch/look): ").strip().lower()
    
    if choice == 'touch':
        ending_mysterious_pool()
    elif choice == 'look':
        ending_sparkling_gem()
    else:
        print("Nope. Please choose 'touch' or 'look'.")
        pool_choice()

def ending_safe_crossing():
    print("\nYou navigate carefully and manage to cross the slippery part of the tunnel safely.")
    print("Eventually, you find a hidden exit leading to fresh air and freedom!")
    print("Congratulations! You have escaped the cave safely.")

def ending_slip_fall():
    print("\nIn your haste, you slip on the wet rocks and fall into a dark chasm.")
    print("You try to grab onto something, but it's too late. You fall into darkness...")
    print("Unfortunately, this is the end of your adventure.")

def ending_mysterious_pool():
    print("\nYou touch the shimmering water and feel a rush of energy.")
    print("Suddenly, you are transported to a mystical land filled with magical creatures.")
    print("You have begun a new adventure in a fantastical world!")

def ending_wandering_lost():
    print("\nIgnoring the pool, you continue down the path.")
    print("However, the whispers grow louder and more disorienting, leading you deeper into the cave.")
    print("Eventually, you find yourself lost forever in the darkness...")

def ending_sparkling_gem():
    print("\nAs you look around, you find a sparkling gem hidden among the rocks.")
    print("You decide to take it with you, believing it may have magical properties.")
    print("With the gem in hand, you find a hidden exit, escaping the cave with newfound power!")
    print("Congratulations! You have escaped the cave, and your journey has just begun.")

def ending_enchanted_creature():
    print("\nAs you inspect the pool, an enchanted creature appears before you.")
    print("It offers you a choice: a safe passage out or a chance to stay and learn magic.")
    choice = input("Do you want to leave or learn? (leave/learn): ").strip().lower()
    
    if choice == 'leave':
        print("You choose to leave, grateful for the experience and the knowledge you've gained.")
        print("You escape the cave with new insights into the world.")
    elif choice == 'learn':
        print("You decide to stay and learn magic from the creature.")
        print("You become a powerful mage, never leaving the cave but mastering its mysteries.")
    else:
        print("You can't do that. Please choose 'leave' or 'learn'.")
        ending_enchanted_creature()

# Start the game
start_game()
