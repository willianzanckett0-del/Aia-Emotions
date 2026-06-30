from core.memory import Memory
from core.personality import Personality
from core.mood import Mood
from core.dialog import Dialog
from ui.chat_window import ChatWindow
from core.conversation import Conversation

memory = Memory()

personality = Personality()

mood = Mood(
    memory=memory,
    personality=personality
)


dialog = Dialog()


chat = ChatWindow()

def next_state(index):
    conversation.change_state("general_questions")

    chat.show_choices(
        dialog.get_choices(
            conversation.get_state()
        )
    )

chat.on_choice = next_state

conversation = Conversation()

choices = dialog.get_choices(
    conversation.get_state()
)

chat.show_choices(choices)

chat.start()