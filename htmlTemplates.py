css = '''
<style>

.chat-message {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1.2rem;
    border-radius: 12px;
    margin-bottom: 1rem;
}

.chat-message.user {
    background-color: #2b313e;
    flex-direction: row-reverse;
}

.chat-message.bot {
    background-color: #475063;
}

.chat-message .avatar {
    width: 60px;
}

.chat-message .avatar img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    flex: 1;
    color: white;
    font-size: 16px;
    line-height: 1.5;
    word-wrap: break-word;
}

</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png">
    </div>

    <div class="message">
        {{MSG}}
    </div>
</div>
'''

user_template = '''
<div class="chat-message user">

    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png">
    </div>

    <div class="message">
        {{MSG}}
    </div>

</div>
'''
