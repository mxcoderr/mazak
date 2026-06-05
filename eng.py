import random

mazak_letters = {
    "A": "Arial Among Alphabets",
    "B": "Businesslike Checking Calculator",
    "C": "C language Capitallike Crocodile mark",
    "D": "Dalogger Dimension",
    "E": "Electronic Arts Terminator",
    "F": "Fork like FigureMakerBisonJohnson",
    "G": "Google Giant",
    "H": "Happy Hipopotamus",
    "I": "Influencer AI",
    "J": "Jumbo Jet in my head",
    "K": "Katana Kindness",
    "L": "Lovuble ",
    "M": "Majestic Monkey",
    "N": "Nice Network Ninja",
    "O": "Open Office Operator",
    "P": "Python Programmable Penguin",
    "Q": "Quantum Query Queen",
    "R": "Recursive Robot Runner",
    "S": "Stacked System Samurai",
    "T": "Terminal Turbo Tiger",
    "U": "Universal Update Unit",
    "V": "Virtual Vision Viking",
    "W": "Web Warrior Wizard",
    "X": "Xtreme XML Xylophone",
    "Y": "Yielding Yotta Yak",
    "Z": "Zero Zenith Zebra",
    " ": "Empty Tiger",
    "!": "Heavy patcher with a lot of bugs",
    "?": "Curious Question Mark"
}


class Query:
    def __init__(self, text):
        answer = []

        for char in text:
            answer.append(mazak_letters.get(char, " "))

        if random.randint(0, 100) == 14:
            self.answer = "Error 4834802: Protocol ate your query :(" 
        else:
            self.answer = " and ".join(answer)
