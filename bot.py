from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Ambil token dari Environment Variable (supaya aman)
TOKEN = os.getenv("BOT_TOKEN")

# Pesan sambutan
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋 Aku bot curhat anonim.\n"
        "Ketik apa saja, aku akan dengarkan 😊"
    )

# Balas setiap curhatan
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Aku dengar kamu bilang: {text}\nTenang, di sini aman ✨")

def main():
    app = Application.builder().token(TOKEN).build()

    # Handler command /start
    app.add_handler(CommandHandler("start", start))

    # Handler pesan teks biasa
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot berjalan... 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
