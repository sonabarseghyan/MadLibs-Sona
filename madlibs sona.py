ml = int(input(f'''Hello, welcome to MadLibs. Please input 1,2 or 3 to choose a random scenario!'''))
if ml == 1:
    a = input("Input a number")
    b = input("Input a measure of time")
    c = input("Input a mode of transportation")
    d = input("Input an adjective")
    e = input("Input another adjective")
    f = input("Input a noun")
    g = input("Input a color")
    h = input("Input a part of the body")
    i = input("Input a verb")
    j = input("Input a another number")
    k = input("Input a random noun")
    l = input("Input another noun")
    m = input("Input another part of the body")
    n = input("Input another noun")
    o = input("Input one more adjective")
    p = input("Input a silly word")

    s1 = f'''It was about {a} {b} ago when I arrived at the hospital in a {c}.
     The hospital is a/an {d} place, there are a lot of {e} {f} here.
     There are nurses here who have {g} {h}.
     If someone wants to come into my room I told them that they have to {i} first.
     I’ve decorated my room with {j} {k}.
     Today I talked to a doctor and they were wearing a {l} on their {m}.
     I heard that all doctors {i} {n} every day for breakfast.
     The most {o} thing about being in the hospital is the {p} {f} !'''
    print(s1)
elif ml == 2:
    a2 = input("What is your favorite name?")
    b2 = input("Write a noun that comes to mind")
    c2 = input("What feeling would you have if you saw a mouse dancing on a rooftop wearing a tuxedo ?")
    d2 = input("What would you like to do right now?")
    e2 = input("What's the worst feeling (adjective) for you ?")
    f2 = input("An animal you wouldn't keep in your house")
    g2 = input("Input a verb")
    h2 = input("Your least favorite color")
    i2 = input("An activity you would like to try (verb ending with -ing)")
    j2 = input("An adverb ending in -ly")
    k2 = input("Throw in a random number")
    l2 = input("Now let's think of a measure of time")
    m2 = input("Some color please")
    n2 = input("Name one more animal")
    o2 = input("A random number (i know, i know, this will end soon lol)")
    p2 = input("Blurt out a silly word")
    q2 = input("Now, the last one, give me a noun")

    s2 = f'''This weekend I am going camping with {a2}.
    I packed my lantern, sleeping bag, and {b2}. I am so {c2} to {d2} in a tent.
    I am {e2} we might see a(n) {f2}, I hear they’re kind of dangerous.
    While we’re camping, we are going to hike, fish, and {g2}.
    I have heard that the {h2} lake is great for {i2}.
    Then we will {j2} hike through the forest for {k2} {l2}s.
    If I see a {m2} {n2} while hiking, I am going to bring it home as a pet!
    At night we will tell {o2} {p2} stories and roast {q2} around the campfire!!'''
    print(s2)
elif ml == 3:
    PersonsName = input("What is your name?")
    Adjective = input("Describe yourself in one word")
    Color = input("Choose a color")
    Animal = input("Name an animal")
    Place = input("Where would you like to be right now?")
    Adjective2 = input("Give me a random adjective")
    MagicalCreaturePlural = input("Your favorite magical creatures")
    Adjective3 = input("One more adjective")
    MagicalCreaturePlural2 = input("A magical creature which would scare you to death")
    Room = input("Now your favorite room in your house")
    Noun = input("Think of an object")
    Noun2 = input("Think of another object")
    NounPlural3 = input("Almost there! Think of a noun")
    Adjective4 = input("How would you describe your angriest teacher")
    NounPlural4 = input("What is your favorite thing?")
    Number = input("a random number")
    Measureoftime = input("A random measure of time")
    Verbing = input("Now your favorite activity (the verb should end with -ing")
    Adjective5 = input("describe your enemy in 1 word")
    Noun5 = input("The last one! I promise! Give me a noun")

    s3 = f'''Dear {PersonsName}, I am writing to you from a {Adjective} castle in an enchanted forest.
    I found myself here one day after going for a ride on a {Color} {Animal} in {Place}.
    There are {Adjective2} {MagicalCreaturePlural} and {Adjective3} {MagicalCreaturePlural2} here!
    In the {Room} in a House there is a pool full of {Noun}.
    I fall asleep each night on a {Noun2} of {NounPlural3}s and dream of {Adjective4} {NounPlural4}.
    It feels as though I have lived here for {Number} {Measureoftime}.
    I hope one day you can visit, although the only way to get here now is {Verbing} on a {Adjective5} {Noun5}!!'''
    print(s3)

print("Well done, hope you enjoyed the game mernem srtid")
