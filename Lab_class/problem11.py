text = input("Enter text: ")

text = text.lower()
character_frequency = {}

for character in text:
    if character.isalpha():
        if character in character_frequency:
            character_frequency[character] += 1
        else:
            character_frequency[character] = 1

print("\nCharacter frequencies:")

for character in sorted(character_frequency):
    print(character + ":", character_frequency[character])