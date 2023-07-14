import random
import config


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Yahallo!'

    if p_message == 'helo':
        return 'heeeelo back!'

    if p_message == 'roll':
        print('Number beetween 1 and 6 coming!!!')
        return str(random.randint(1, 6))

    if p_message == '+help':
        return """
```
General commands (type help pagename to summon the right help menu):
help music   ====>     Shows Music commands
hello        ====>     Answers back
roll         ====>     Generates a random number between 1 and 6
""" + config.global_operator + """repeat  - times string/text (10 capped)
```
"""
    if p_message == 'help music':
        return """
```
Music commands:
""" + config.global_operator + """play    - Plays a song & joins the channel
""" + config.global_operator + """pause   - Pauses the current song being played
""" + config.global_operator + """resume  - Resumes playing the current song
""" + config.global_operator + """stop    - Stops playing & disconnects from the channel
""" + config.global_operator + """join    - Joins channel
""" + config.global_operator + """leave   - Leaves & Pauses
```
"""
        
