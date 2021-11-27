import random


def main():
    incorrects = 0
    while incorrects < 5:
        incorrects += ask_question()


def ask_question():
    line = fetch_question()
    print(line[0])
    return check_answer(line)


def fetch_question():
    with open("questions.csv", "r") as file:
        questions = file.readlines()
    line = questions[random.randrange(0, len(questions))]
    line = list(filter(None, line.rstrip().split(',')))
    return line


def check_answer(line):
    correct = False
    answers = line[1:]
    response = input().lower()
    for answer in answers:
        if response == answer.lower():
            correct = True
        else:
            pass

    if correct:
        print("Correct!")
        return 0
    else:
        print("Sorry, incorrect! The correct answer was: " + line[1])
        return 1


if __name__ == "__main__":
    main()
