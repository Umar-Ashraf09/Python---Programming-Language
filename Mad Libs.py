
while True:
    #hash(5)
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Welcome!")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMad Libs Generator")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose one from below.")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t1. Mad Libs about Jobs. "
          "\t\t\t3. Mad Libs about Me. "
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t2. Mad Libs Photo shoot. "
          "\t\t\t4. Mad Libs Butterflies. "
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  5. Quit")
    try:
        user_input = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSelect: "))
        if user_input in (1, 2, 3, 4, 5):
            if user_input == 1:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1. Mad Libs about Jobs.")
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tFill out these questions to generate your own silly mad libs"
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tstory instantly. This mad lib only has nouns, verbs and adjectives."
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t(Hint: a Verb is an action. A Noun is a person/place/thing."
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tAn Adjective describes a person/place/thing.)")
                occupation = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Occupation(a Job): ")
                noun_1 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Noun: ")
                adjective_1 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Adjective: ")
                noun_2 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Noun: ")
                verb_1 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Verb: ")
                adjective_2 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Adjective: ")
                noun_3 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Noun: ")
                verb_2 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Verb: ")
                noun_4 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Noun: ")
                verb_3 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Verb: ")
                print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tToday a {occupation} named {noun_4} came to our school to talk to us about her job. "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tShe said the most important skill you need to know to do her job is to be able to "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t{verb_2} around (a) {adjective_1} {noun_3}. She said it was easy for her to learn her job because she loved to "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t{verb_1} when she was my age--and that helps a lot! If you're considering her profession, "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tI hope you can be near (a) {adjective_2} {noun_1}. That's very important! If you get too distracted "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tin that situation you won't be able to {verb_3} next to (a) {noun_2}!")

            elif user_input == 2:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2. Mad Libs Photo shoot.")
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tFill out these questions to generate your own silly mad libs "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tstory instantly.(Hint: a Verb is an action. An Adverb usually "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tends in 'ly' and describes an action (like slowly). A Noun is "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\ta person/place/thing. An Adjective describes a person/place/thing.)")
                animals = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Animal: ")
                feeling = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Feeling: ")
                things_1 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Things(plural): ")
                professional = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Professional (like 'Baker'): ")
                clothing = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Piece of Clothing: ")
                things_2 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Things(plural): ")
                person = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Person: ")
                place = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Place: ")
                verb = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Verb (ending in 'ing'): ")
                food = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Food: ")
                print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tSay '{food}', the photographer said as the camera flashed! {person} and I had gone "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tto {place} to get our photos taken today. The first photo we really wanted was "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\ta picture of us dressed as {animals} pretending to be a {professional}. When we saw the proofs "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tof it, I was a bit {feeling} because it looked different than in my head. "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t(I hadn't imagined so many {things_1} behind us.) However, the second photo was "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\texactly what I wanted. We both looked like {things_2} wearing {clothing} and {verb}--exactly what I had in mind!")

            elif user_input == 3:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3. Mad Libs about Me.")
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tFill out these questions to generate your own silly mad libs "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tstory instantly.(Hint: a Verb is an action. An Adverb usually "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tends in 'ly' and describes an action (like slowly). A Noun is "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\ta person/place/thing. An Adjective describes a person/place/thing.)")
                food = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Food or A Silly Word: ")
                job = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Profession/Job: ")
                adjective = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Adjective: ")
                phrase = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Phrase/Lyrics/Saying: ")
                animal = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Animal: ")
                verb = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Verb: ")
                place = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Place: ")
                celebrity = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Celebrity: ")
                something = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Something you would buy: ")
                things = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Things(plural): ")
                print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tHi my name is {celebrity}, but my friends call me {adjective} {food}. My favorite color is the "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tcolor of {things} and my favorite thing to do is {verb}. My parents were a {animal} and {job}, "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\twhich is why we lived in {place}. You probably know me from my TV commercial for {something}. "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tI'm the one who says, '{phrase}' at the very end!")

            elif user_input == 4:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4. Mad Libs Butterflies.")
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tFill out these questions to generate your own silly mad libs "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tstory instantly.(Hint: a Verb is an action. An Adverb usually "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tends in 'ly' and describes an action (like slowly). A Noun is "
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\ta person/place/thing. An Adjective describes a person/place/thing.)")
                things = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Things(plural): ")
                insect = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter An Insect: ")
                verb = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Verb: ")
                phrase = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter A Phrase/Lyrics/Saying: ")
                color = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Color: ")
                adjective_1 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Adjective: ")
                food = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Food: ")
                person = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Person: ")
                adjective_2 = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter an Adjective: ")
                place = input("\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter a Place: ")
                print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tLast night I dreamed I was a {adjective_2} {insect} with {color} splotches that looked like {things}. "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tI flew to {place} with my best friend, {person}, who was a {adjective_1} butterfly. We ate some "
                      f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t{food} when we got there and then decided to {verb}. The dream ended when I said, '{phrase}'.")

            elif user_input == 5:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!"
                      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease come again.")
                exit()

            else:
                pass
            break
        else:
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!"
                  "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease choose a number from given list.")

    except ValueError:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!"
              "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter a number.")










