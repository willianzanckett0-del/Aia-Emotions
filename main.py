from core.memory import Memory
from core.personality import Personality
from core.mood import Mood
from core.dialog import Dialog
from ui.chat_window import ChatWindow


memory = Memory()

personality = Personality()

mood = Mood(
    memory=memory,
    personality=personality
)


dialog = Dialog()


chat = ChatWindow()


greetings = dialog.get_greetings()
print(greetings)


chat.show_choices(greetings)


chat.start()
