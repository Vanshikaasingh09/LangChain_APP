css = """
<style>
    body {
        background-color: #000000;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    .stApp {
        background-color: #000000;
        padding: 2rem;
        color: white;
    }

    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }

    .stTextInput > div > div > input {
        background-color: #1e1e1e;
        border-radius: 8px;
        padding: 10px;
        color: white;
        border: 1px solid #444;
    }

    .chat-message {
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
    }

    .chat-message.user {
        background-color: #222831;
        border: 1px solid #393e46;
        color: #eeeeee;
    }

    .chat-message.bot {
        background-color: #393e46;
        border: 1px solid #00adb5;
        color: #ffffff;
    }

    .chat-message .avatar {
        font-size: 1.5rem;
    }

    .chat-message .message {
        flex: 1;
    }

    .stButton button {
        background-color: #00adb5;
        color: black;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: bold;
    }

    .stButton button:hover {
        background-color: #007b80;
        color: white;
    }
</style>
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">🤖</div>
    <div class="message">{{MSG}}</div>
</div>
"""

user_template = """
<div class="chat-message user">
    <div class="avatar">🙋‍♀️</div>
    <div class="message">{{MSG}}</div>
</div>
"""
