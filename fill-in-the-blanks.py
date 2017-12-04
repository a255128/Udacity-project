#Global Variables:
easy_quiz='''Most people think that Edison invented the first light bulb.They are wrong.
In fact, he was spectacularly late to the game.
In 1878, when the 36-year-old inventor decided to focus on building a light bulb,
23 others had already invented early versions called arc lamps.'''


medium_quiz='''Perhaps the most popular current success formula is the 10,000-hour rule
by Malcolm Gladwell. The idea is that you need 10,000 hours of deliberate
practice to become a world-class performer in any field.
Research now tells us, that this formula is woefully inadequate to explain success,
especially in the professional realm. '''

hard_quiz='''What Edison and others teach us is that we should maximize the number of experiments,
not hours. Instead of the 10,000-hour rule, we need what I call the 10,000-experiment rule.
Throughout history, the scientific method has arguably produced more human progress than
any other philosophy. At the heart of the scientific method is experimentation:
develop a hypothesis , perform a test to prove the hypothesis right or wrong, analyze the results,
and create a new hypothesis based on what you learned.'''

#the full article can find in https://medium.com/the-mission/forget-about-the-10-000-hour-rule-7b7a39343523

lunatic_quiz='''Death is nothing at all.
It does not count.
I have only slipped away into the next room.
Nothing has happened.

Everything remains exactly as it was.
I am I, and you are you,
and the old life that we lived so fondly together is untouched, unchanged.
Whatever we were to each other, that we are still.

Call me by the old familiar name.
Speak of me in the easy way which you always used.
Put no difference into your tone.
Wear no forced air of solemnity or sorrow.

Laugh as we always laughed at the little jokes that we enjoyed together.
Play, smile, think of me, pray for me.
Let my name be ever the household word that it always was.
Let it be spoken without an effort, without the ghost of a shadow upon it.'''

'''Source: https://www.familyfriendpoems.com/poem/death-is-nothing-at-all-by-henry-scott-holland'''

paragraphs = [easy_quiz, medium_quiz, hard_quiz, lunatic_quiz]

answer_of_quizs=[["Edison","late","focus","versions"], #easy_answers
["popular","deliberate","inadequate","professional"], #medium_answers
["maximize","scientific","philosophy","hypothesis"], #hard_answers
["slipped","remains","solemnity","household"] #luntic_answer

#Futctions:

def welcome(player_name):
        '''
        Inputs:
                The name of player.
        Behavior:
                Show player's name.
        Outputs:
                Introduction to game welcome.
        '''
    print "Welcome," + player_name +".This is a fill in blanks quiz. Have fun!"

def select_a_difficulty_level():
    '''
    Inputs:
            Current level.
    Behavior:
            Player can choose a level they want to play.
    Outputs:
            The specific paragraph and answers associated with that level.
    '''
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
    '''
    Inputs:
            Current level and given blank.
    Behavior:
            Replace the words in answer_of_quizs for the level from given blank.
    Outputs:
            Paragraph show the blank.
    '''
    paragraph = paragraphs[level]
        #replace all answer_of_quizs from current blank to the last one.
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
    '''
    Inputs:
            The current level.
    Behavior:
            Collect user's answer and judge it is right or wrong.
    Outputs:
            The correct answers replaced blanks in paragraph.
    '''
    blank = 0 # Given blank

    while blank < len(answer_of_quizs[level]):
        print process_paragraph(level, blank)

        question = "\n What should go in blank " + str(blank + 1) + "?"
        answer = raw_input(question).lower()

        correct_answer = answer_of_quizs[level][blank].lower()
        if correct_answer == answer:
            print "Correct!"
            blank += 1
            #The correct answers replaced blanks in paragraph.
        else:
            print "Try again!"

    print paragraphs[level]
    print "Well played!"

def main():
    '''
    Inputs:
            Click Run Module in Python.
    Behavior:
            Execute the main program.
    Outputs:
            Whole program.
    '''
    player_name = raw_input("What is your name? ")
    welcome(player_name)

    level = select_a_difficulty_level()
    max_level=4
    able_to_increase_difficult_level=3

    while level < max_level:
        play_game(level)

        if level < able_to_increase_difficult_level:
            proceed = raw_input("Too easy? Try harder quiz! (YES/NO)").upper()
            if proceed == "YES":
                level += 1
            else:
                break
        else:
            break

    print player_name + ",Thanks for playing! "

main()
