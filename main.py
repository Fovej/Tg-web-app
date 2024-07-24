from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Поменять Token на токен своего бота (если надо)
TOKEN = '6454445607:AAEytFeUFRatVoGackCsdn2Dpmg06Mu_Kcw'

async def start(update: Update, context: CallbackContext) -> None:
    # Отправляет инструкцию и ждет URL
    await update.message.reply_text(
        'Отправь URL для апки'
    )

async def handle_message(update: Update, context: CallbackContext) -> None:
    
    url = update.message.text
    if url.startswith('http://') or url.startswith('https://'):
        keyboard = [[InlineKeyboardButton("Открыть WebApp", web_app={'url': url})]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('жать сюда для апки', reply_markup=reply_markup)
    else:
        await update.message.reply_text('твой URL - хуйня')

def main() -> None:
    # Запускает бота
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
