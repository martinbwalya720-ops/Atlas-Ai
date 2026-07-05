from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = 8977525770:AAEsqYQAOoyWqtgeisljfe9g9gMJENqYe2E

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Atlas AI is online!\n\n"
        "Commands:\n"
        "/start\n"
        "/best\n"
        "/scan\n"
        "/risk"
    )

async def best(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Best Trade\n\n"
        "Pair: EUR/USD\n"
        "Signal: BUY 🟢\n"
        "Market Strength: 91%\n"
        "Signal Confidence: 94%\n"
        "Risk: LOW\n"
        "Expiry: 3 Minutes"
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("best", best))

app.run_polling()
