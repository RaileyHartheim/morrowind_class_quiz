class Quiz:
    def __init__(self):
        self.quiz_data = [
            {
                "question_number": 0,
                "question": "On a clear day you chance upon a strange animal, its leg trapped in a hunter's clawsnare. Judging from the bleeding it will not survive long.",
                "answers": {
                    0: ("Draw your dagger, mercifully ending its life with a single thrust.", "Combat"),
                    1: ("Use herbs from your pack to put it to sleep.", "Magic"),
                    2: ("Do not interfere in the natural evolution of events, but rather take the opportunity to learn more about a strange animal you have never seen before.", "Stealth")
                }
            },
            {
                "question_number": 1,
                "question": "One Summer afternoon your father gives you a choice of chores.",
                "answers": {
                    0: ("Work in the forge with him casting iron for a new plow.", "Combat"),
                    1: ("Gather herbs for your mother who is preparing dinner.", "Magic"),
                    2: ("Go catch fish at the stream using a net and line.", "Stealth")
                }
            },
            {
                "question_number": 2,
                "question": "Your cousin has given you a very embarrassing nickname and, even worse, likes to call you it in front of your friends. You asked him to stop, but he finds it very amusing to watch you blush.",
                "answers": {
                    0: ("Beat up your cousin, then tell him that if he ever calls you that nickname again, you will bloody him worse than this time.", "Combat"),
                    1: ("Make up a story that makes your nickname a badge of honor instead of something humiliating.", "Magic"),
                    2: ("Make up an even more embarrassing nickname for him and use it constantly until he learns his lesson.", "Stealth")
                }
            },
            {
                "question_number": 3,
                "question": "There is a lot of heated discussion at the local tavern over a group of people called 'Telepaths'. They have been hired by certain City-State kings. Rumor has it these Telepaths read a person's mind and tell their lord whether a follower is telling the truth or not.",
                "answers": {
                    0: ("This is a terrible practice. A person's thoughts are his own and no one, not even a king, has the right to make such an invasion into another human's mind.", "Combat"),
                    1: ("Loyal followers to the king have nothing to fear from a Telepath. It is important to have a method of finding assassins and spies before it is too late.", "Magic"),
                    2: ("In these times, it is a necessary evil. Although you do not necessarily like the idea, a Telepath could have certain advantages during a time of war or in finding someone innocent of a crime.", "Stealth")
                }
            },
            {
                "question_number": 4,
                "question": "Your mother sends you to the market with a list of goods to buy. After you finish you find that by mistake a shopkeeper has given you too much money back in exchange for one of the items.",
                "answers": {
                    0: ("Return to the store and give the shopkeeper his hard-earned money, explaining to him the mistake.", "Combat"),
                    1: ("Decide to put the extra money to good use and purchase items that would help your family.", "Magic"),
                    2: ("Pocket the extra money, knowing that shopkeepers in general tend to overcharge customers anyway.", "Stealth")
                }
            },
            {
                "question_number": 5,
                "question": "While in the market place you witness a thief cut a purse from a noble. Even as he does so, the noble notices and calls for the city guards. In his haste to get away, the thief drops the purse near you. Surprisingly no one seems to notice the bag of coins at your feet.",
                "answers": {
                    0: ("Pick up the bag and signal to the guard, knowing that the only honorable thing to do is return the money to its rightful owner.", "Combat"),
                    1: ("Leave the bag there, knowing that it is better not to get involved.", "Magic"),
                    2: ("Pick up the bag and pocket it, knowing that the extra windfall will help your family in times of trouble.", "Stealth")
                }
            },
            {
                "question_number": 6,
                "question": "Your father sends you on a task which you loathe, cleaning the stables. On the way there, pitchfork in hand, you run into your friend from the homestead near your own. He offers to do it for you, in return for a future favor of his choosing.",
                "answers": {
                    0: ("Decline his offer, knowing that your father expects you to do the work, and it is better not to be in debt.", "Combat"),
                    1: ("Ask him to help you, knowing that two people can do the job faster than one, and agree to help him with one task of his choosing in the future.", "Magic"),
                    2: ("Accept his offer, reasoning that as long as the stables are cleaned, it matters not who does the cleaning.", "Stealth")
                }
            },
            {
                "question_number": 7,
                "question": "Your mother asks you to help fix the stove. While you are working, a very hot pipe slips its mooring and falls towards her.",
                "answers": {
                    0: ("Position yourself between the pipe and your mother.", "Combat"),
                    1: ("Grab the hot pipe and try to push it away.", "Magic"),
                    2: ("Push your mother out of the way.", "Stealth")
                }
            },
            {
                "question_number": 8,
                "question": "While in town the baker gives you a sweetroll. Delighted, you take it into an alley to enjoy only to be intercepted by a gang of three other kids your age. The leader demands the sweetroll, or else he and his friends will beat you and take it.",
                "answers": {
                    0: ("Drop the sweetroll and step on it, then get ready for the fight.", "Combat"),
                    1: ("Give him the sweetroll now without argument, knowing that later this afternoon you will have all your friends with you and can come and take whatever he owes you.", "Magic"),
                    2: ("Act like you're going to give him the sweetroll, but at the last minute throw it in the air, hoping that they'll pay attention to it long enough for you to get a shot in on the leader.", "Stealth")
                }
            },
            {
                "question_number": 9,
                "question": "Entering town you find that you are witness to a very well-dressed man running from a crowd. He screams to you for help. The crowd behind him seem very angry.",
                "answers": {
                    0: ("Rush to the town's aid immediately, despite your lack of knowledge of the circumstances.", "Combat"),
                    1: ("Stand aside and allow the man and the mob to pass, realizing it is probably best not to get involved.", "Magic"),
                    2: ("Rush to the man's aid immediately, despite your lack of knowledge of the circumstances.", "Stealth")
                }
            }
        ]

    def get_class_by_params(self, combat, magic, stealth):
        if combat >= 7:
            return "warrior"
        elif magic >= 7:
            return "mage"
        elif stealth >= 7:
            return "thief"
        elif combat == 6 and magic == 4 or combat == 6 and magic == 2 and stealth == 2 or combat == 6 and stealth == 4:
            return "knight"
        elif combat == 6 and magic == 3 and stealth == 1:
            return "barbarian"
        elif combat == 6 and magic == 1 and stealth == 3:
            return "crusader"
        elif combat == 5 and magic == 5 or combat == 5 and magic == 4 and stealth == 1 or combat == 5 and magic == 1 and stealth == 4:
            return "archer"
        elif combat == 5 and magic == 2 and stealth == 3 or combat == 5 and magic == 3 and stealth == 2:
            return "scout"
        elif combat == 4 and magic == 1 and stealth == 5 or combat == 4 and stealth == 6 or combat == 5 and stealth == 5:
            return "rogue"
        elif combat == 3 and magic == 6 and stealth == 1 or combat == 4 and magic == 6:
            return "healer"
        elif combat == 3 and magic == 5 and stealth == 2 or combat == 2 and magic == 5 and stealth == 3:
            return "witchhunter"
        elif combat == 3 and magic == 4 and stealth == 3 or combat == 1 and magic == 4 and stealth == 5 or magic == 4 and stealth == 6:
            return "spellsword"
        elif combat == 3 and magic == 2 and stealth == 5:
            return "pilgrim"
        elif combat == 4 and magic == 3 and stealth == 3 or combat == 4 and magic == 4 and stealth == 2:
            return "bard"
        elif combat == 2 and magic == 4 and stealth == 4:
            return "nightblade"
        elif combat == 2 and magic == 3 and stealth == 5 or combat == 3 and magic == 3 and stealth == 4:
            return "monk"
        elif combat == 2 and magic == 2 and stealth == 6:
            return "acrobat"
        elif combat == 1 and magic == 3 and stealth == 6 or magic == 5 and stealth == 5:
            return "assassin"
        elif combat == 3 and magic == 1 and stealth == 6 or combat == 4 and magic == 2 and stealth == 4:
            return "agent"
        elif combat == 2 and magic == 6 and stealth == 2 or combat == 4 and magic == 5 and stealth == 1:
            return "sorcerer"
        elif combat == 1 and magic == 6 and stealth == 3 or magic == 6 and stealth == 4 or combat == 1 and magic == 5 and stealth == 4:
            return "battlemage"
        else:
            return "Something gone wrong."


    def get_results(self, answer_data):
        combat = 0
        magic = 0
        stealth = 0
        for i, j in answer_data.items():
            if self.quiz_data[i]["answers"][j][1] == "Combat":
                combat += 1
            elif self.quiz_data[i]["answers"][j][1] == "Magic":
                magic += 1
            elif self.quiz_data[i]["answers"][j][1] == "Stealth":
                stealth += 1
        class_result = self.get_class_by_params(combat, magic, stealth)
        return class_result


if __name__ == "__main__":
    quiz = Quiz()
    answer_data = {
        0: 0,
        1: 2,
        2: 0,
        3: 2,
        4: 1,
        5: 0,
        6: 1,
        7: 0,
        8: 0,
        9: 2
    }
    results = quiz.get_results(answer_data)
    print(results)