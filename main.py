import random

welcome_msg = "WELCOME TO GOPHER PY GAMES"
print("********************************")
print(f"** {welcome_msg} **")
print("********************************")

gopher_pos = random.randint(1, 4)
user_name = input("Input your name : ")

cave_shape = "|_|"
cave = [cave_shape] * 4
null_cave = cave.copy()
cave[gopher_pos - 1] = "|0_0|"

print(f'''
Hello, user {user_name}! Try to pay attention and guess where Gopher is in the cave below 👇
{null_cave}
''')

user_certainty = "n"
while user_certainty.lower() in ["n", "no"]:
    user_choice = int(input("Which cave do you think GOPHER is in? [ 1 / 2 / 3 / 4 ] => "))
    user_certainty = input("Are you sure about your guess? | Y / N | => ")

if user_certainty.lower() in ["y", "yes"]:
    if user_choice == gopher_pos:
        print(f''' 
        🎊CONGRATULATIONS YOU WON!🎊 
        Your Guess is Correct ✅ 
        {cave}
        Gopher is In Cave => {gopher_pos}
        ''')
    else:
        print(f'''
        ❗ SORRY YOU LOSE! ❗ 
        Your Guess is Incorrect ❌ 
        {cave}
        Gopher is Not In Cave {user_choice}, But In Cave {gopher_pos}
        ''')