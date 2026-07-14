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

conversation = Conversation()

print("Arquivo:", conversation.get_file())

text = dialog.get_start(
    conversation.get_file()
)

choices = dialog.get_choices(
    conversation.get_file(),
    conversation.get_section()
)

chat.show_choices(choices)

def next_state(index):

    global choices

    choice = choices[index]

    if "next_file" in choice:
        conversation.change_file(
        choice["next_file"]
    )

    if "next_section" in choice:
        conversation.change_section(
        choice["next_section"]
    )

    for emotion_name, value in choice.get("effect", {}).items():
        mood.adjust(emotion_name, value)

    mood.save_emotions(memory)

    emotion = mood.conversation_state()

    if emotion != "neutral":
        conversation.change_file(emotion)

    choices = dialog.get_choices(
        conversation.get_file(),
        conversation.get_section()
    )

    chat.show_choices(choices)

    print(memory.data["emotions"])

chat.on_choice = next_state

chat.start()