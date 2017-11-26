#coding:utf-8

#Global Variables:
easy_quiz='''Most people think that ___1___ invented the first light bulb.They are wrong.
In fact, he was spectacularly ___2___ to the game.
In 1878, when the 36-year-old inventor decided to ___3___ on building a light bulb,
23 others had already invented early ___4___ called arc lamps.'''


medium_quiz='''Perhaps the most ___1___ current success formula is the 10,000-hour rule
by Malcolm Gladwell. The idea is that you need 10,000 hours of ___2___
practice to become a world-class performer in any field.
Research now tells us, that this formula is woefully ___3___ to explain success,
especially in the professional ___4___. '''

hard_quiz='''What Edison and others teach us is that we should ___1___ the number of experiments,
not hours. Instead of the 10,000-hour rule, we need what I call the 10,000-experiment rule.
Throughout history, the ___2___ method has arguably produced more human progress than
any other ___3___. At the heart of the scientific method is experimentation:
develop a ___4___, perform a test to prove the ___4___ right or wrong, analyze the results,
and create a new ___4___ based on what you learned.'''

#the full article can find in https://medium.com/the-mission/forget-about-the-10-000-hour-rule-7b7a39343523

lunatic_quiz='''當所屬群體的___1___越多，當中___2___的思考__3___能力就越低,所以這也解釋了網路世界為何___4___叢生。'''

paragraphs = [easy_quiz, medium_quiz, hard_quiz, lunatic_quiz]

answer_of_quizs=[["Edison","late","focus","versions"], #easy_answers
["popular","deliberate","inadequate","realm"], #medium_answers
["maximize","scientific","philosophy","hypothesis"], #hard_answers
["人群","個體","判斷","亂象"]] #luntic_answer

#Futctions:

def welcome(player_name):
    #Show player's name.
    print "Welcome," + player_name +".This is a fill in blanks quiz. Have fun!"

def select_a_difficulty_level():
    #Player can choose a level they want to play.
    level = raw_input("Enter your difficulty level(easy / medium / hard):")
    if level == "easy":
        print "You are in easy game"
        return 0
    elif level == "medium":
        print "You are in medium game"
        return 1
    elif level == "hard":
        print "You are in hard game"
        return 2
    else:
        print "You have found the sercet game!"
        return 3

def process_paragraph(level, blank):
    paragraph = paragraphs[level]
     #replace all the answer_of_quizs from current blank to the last one.
    while blank < len(answer_of_quizs[level]):
        word_to_replace = answer_of_quizs[level][blank]
        list_of_words = paragraph.split(" ")
        index = 0
         #Replace the word_to_replace with ___number___
        while index < len(list_of_words):
            if list_of_words[index] == word_to_replace:
                list_of_words[index] = "___" + str(blank + 1) + "___"
            index += 1

        blank += 1
        paragraph = " ".join(list_of_words)

    return paragraph

# play the game for the given level
def play_game(level):
    blank = 0
    # while not all answer_of_quizs are filled, keep guessing until the correct word is provided.
    while blank < len(answer_of_quizs[level]):
        print process_paragraph(level, blank)

        question = "\n What should go in blank " + str(blank + 1) + "?"
        answer = raw_input(question).lower()

        correct_answer = answer_of_quizs[level][blank].lower()
        if correct_answer == answer:
            print "Correct!"
            blank += 1
        else:
            print "Try again!"

    print paragraphs[level]
    print "Well played!"

def main():
    #Execute the main program.
    player_name = raw_input("What is your name? ")
    welcome(player_name)

    level = select_a_difficulty_level()

    while level < 4:
        play_game(level)

        if level < 3:
            proceed = raw_input("Too easy? Try harder quiz! (YES/NO)").upper()
            if proceed == "YES":
                level += 1
            else:
                break
        else:
            break

    print player_name + "Thanks for playing! "

main()
