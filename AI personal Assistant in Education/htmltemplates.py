css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://fintech-ho2020.eu/wp-content/uploads/2021/10/AI.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://images.rawpixel.com/image_png_400/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsb2ZmaWNlOV8zZF9jaGFyYWN0ZXJfaWxsdXN0cmF0aW9uX2Z1bGxib2R5X2lzb2xhdGVkX2luX19mY2Q2NjZjNy1mMzJjLTQ1MzQtYmQ3NS05NTI0NzgxZjUzYmNfMi5wbmc.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''