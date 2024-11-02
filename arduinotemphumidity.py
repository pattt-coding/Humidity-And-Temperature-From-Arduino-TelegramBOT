import serial
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


### Change this to your Telegram token ###
TELEGRAM_TOKEN = 'Your telegram token'

# Function for processing the /getdata command
async def get_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with serial.Serial('COM12', 9600, timeout=1) as ser: ### Change 'COM' to the port to which your Arduino is connected. You can check this by pressing WIN + R and entering 'devmgmt.msc'. ###
            ser.flush()
            ser.write(b'GET_DATA') 
            time.sleep(1)
            data = ser.readline().decode('utf-8').strip()  
            await update.message.reply_text(f'Data from the sensor: {data}')  
    except Exception as e:
        await update.message.reply_text(f'Error: {e}')

# Function for processing the /start command
async def hello_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'To get data from the sensor send /getdata')


def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler('start' , hello_message))
    application.add_handler(CommandHandler('getdata', get_data))
    
   # Starting the bot
    application.run_polling()

if __name__ == '__main__':
    main()
