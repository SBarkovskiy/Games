import random

def get_sentences(player_name, num_sentences):
    sentences = []
    print(f"{player_name}, please write {num_sentences} sentences:")
    for i in range(num_sentences):
        sentence = input(f"Sentence {i + 1}: ")
        sentences.append(sentence)
    return sentences

def main():
    print("Welcome to the Desires Revealer Game!")

    # Get players' names
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")

    # Get sentences from players
    player1_sentences = get_sentences(player1_name, 10)
    player2_sentences = get_sentences(player2_name, 10)

    # Ask if players are ready to reveal desires
    ready = input("Are you ready to reveal desires? (Yes/No): ").lower()

    if ready == "yes":
        print(f"\n{player1_name}, here are 3 random sentences from {player2_name}:")
        random.shuffle(player2_sentences)
        for sentence in player2_sentences[:3]:
            print("- " + sentence)

        print(f"\n{player2_name}, here are 3 random sentences from {player1_name}:")
        random.shuffle(player1_sentences)
        for sentence in player1_sentences[:3]:
            print("- " + sentence)
    else:
        print("Maybe next time!")

if __name__ == "__main__":
    main()
