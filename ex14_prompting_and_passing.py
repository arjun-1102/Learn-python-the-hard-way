# Prompting and passing


# ## In order to use username value print(f"") must be used
# Else python will jsut take in the "{user_name}" as string output
from sys import argv

script, user_name = argv
prompt = '==> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions")
print("Do you like me {user_name}")
likes = input(prompt) 

print(f"Where do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Nor sure where that is, though.
And you have a {computer} computer. Nice.
""")
