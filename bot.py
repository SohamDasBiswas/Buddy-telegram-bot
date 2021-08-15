from telegram import *
from telegram.ext import *
import os
import pyjokes
import requests
import json
from dotenv import load_dotenv
from lxml import etree
from keep_alive import keep_alive
import responses as R
load_dotenv()
client= Bot(os.getenv("BOT_TOKEN"))
print("bot online.....")
updater=Updater(os.getenv("BOT_TOKEN"), use_context=True)



def start_command(update,contex):
  update.message.reply_text("Already Started.........")

def help_command(update, context):
  update.message.reply_text("******Here is a list of things I can do!******\n Some useful commands \n\n 1. /help --> Bot Send's you Commands list and its uses\n 2. /sourcecode --> Bot will send source code\n 3. /introduce --> Indroduce Myself.\n 4. /roast @ --> Bot will roast\n 5. /inspire --> A random inspirational Quote.\n 6. /dadjoke --> A random dad joke.\n 7. /buddyjoke --> A random Buddy joke.\n 8. If your message contains words like sad, depressed, unhappy, miserable- A random affirmative sentence.\n 9. /trivia [number] --> A random Trivia for a number.\n 10. /chucknorris --> Chuck Norris Joke\n 11. /roastme --> Roast yourself.\n 12. /geekjoke --> A random geekjoke.\n 13. /pokemon [name] --> Displays the given pokemon image.\n 14. /news [number] --> Displays given number of Indian News Articles.\n\n ***Last updated 10th August,2021***")

def handle_message(update, contex):
  text=str(update.message.text).lower()
  response= R.sample_responses(text)
  update.message.reply_text(response)

def error(update, contex):
  print(f"Update {update} caused error {contex.error}")

def main():
  updater=Updater(os.getenv("BOT_TOKEN"), use_context=True)
  dp=updater.dispatcher
  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("help", help_command))

  dp.add_handler(MessageHandler(Filters.text,handle_message))
  dp.add_error_handler(error)
  updater.start_polling()
  updater.idle()
keep_alive()
main()