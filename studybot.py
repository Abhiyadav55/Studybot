from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8031754707:AAGidXtc1_ihPTTPoiEPvGc7hFppy4dOS3o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = "मैं - तुम्हारा स्टडी मास्टर! 🚀 मैं हर कदम पर तुम्हारे साथ हूँ! पढ़ाई के रॉकस्टार! 💥 नोट्स, ट्रिक्स, मोटिवेशन, या कुछ भी चाहिए - बस एक कमांड ठोक दे! 🚀 चल, पढ़ाई को बनाते हैं कूल और क्रेजी! 😍 शुरू हो जाओ, mere champion all the best! 🏆\n\nJoin our group 👉 https://t.me/mere_champion"
    await update.message.reply_text(welcome_text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
