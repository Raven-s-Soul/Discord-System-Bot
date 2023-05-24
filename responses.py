import random


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
+repeat  - times string/text (10 capped)
```
"""
  if p_message == 'music':
    return """
```
Music commands:
+play    - Play a song & join the channel
+pause   - pauses the current song being played
+resume  - resumes playing the current song
+stop    - stop play & disconnect from the channel
```
"""


#  return 'Yeah, I don\'t know. Try typing "!help".'
