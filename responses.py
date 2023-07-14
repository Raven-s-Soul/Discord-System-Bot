import random
import config


def handle_response(message) -> str:
  p_message = message.lower()

  if p_message == 'hello':
    return 'Yahallo!'

  if p_message == 'helo':
    return 'helo a te <3!'

  if p_message == 'roll':
    return str(random.randint(1, 6))

  if p_message == 'help':
    return """
```
General commands:
music    - Show Music commands
hello    - Answer back
roll     - Random number from 1 to 6
""" + config.global_operator + """repeat  - times string/text (10 capped)
```
"""
  if p_message == 'music':
    return """
```
Music commands:
""" + config.global_operator + """play    - Play a song & join the channel
""" + config.global_operator + """pause   - Pauses the current song being played
""" + config.global_operator + """resume  - Resumes playing the current song
""" + config.global_operator + """stop    - Stop play & disconnect from the channel
""" + config.global_operator + """join    - Join channel
""" + config.global_operator + """leave   - Leave & Pause
```
"""


#  return 'Yeah, I don\'t know. Try typing "!help".'
