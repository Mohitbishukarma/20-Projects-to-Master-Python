def get_input(word_type: str) -> str:
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_input("noun")
verb1 = get_input("verb (presnt tense)")
noun2 = get_input("noun")
verb2 = get_input("verb (present tense)")
    

story = f"""
Once upon a time, there was {noun1} who likes to {verb1} everyday.
One day {noun2} and {noun1} meet accidently.

{noun1}: Hi {noun2}, what's up?
{noun2}: Hi {noun1}, What are you doing nowaday's?
{noun1}: I am {verb1}ing nowadays. And what about you?
{noun2}: Oh! that's nice. I am just {verb2}ing nowaday's.

And so, They went to a restro and had a great breakfast.

*THE END*
"""

print(story)