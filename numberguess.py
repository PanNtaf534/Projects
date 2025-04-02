import random

print("Καλως ήρθες στο παιχνίδι.Αυτό είναι ένα παιχνίδι μαντεψιάς.Έχεις 7 προσπάθειες.Ας ξεκινήσουμε.")

number_to_guess=random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("Δωσε τη μαντεψιά σου: "))

    if my_guess == number_to_guess:
        print(f"Ο αριθμός είναι {number_to_guess} και το βρήκες σωστά,στις {guess_counter} φορές.") 
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Δυστυχώς, ο αριθμός είναι {number_to_guess}, την επόμενη φορά")
    elif my_guess > number_to_guess:
        print("Μάντεψες πιο ψηλά!")
    elif my_guess < number_to_guess:
        print("Μάντεψες πιο χαμηλά!")           