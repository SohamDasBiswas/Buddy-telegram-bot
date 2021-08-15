from datetime import datetime
import requests
import os
import json
import pyjokes
import random
from dotenv import load_dotenv

load_dotenv()

def get_affirmations():                     #========================================Affermation  
  response=requests.get("https://www.affirmations.dev/")
  data=json.loads(response.text)
  affirmation=data['affirmation']
  return(affirmation)

def get_trivia(number):                   #========================================Trivia         
  url = "https://numbersapi.p.rapidapi.com/"+str(number)+"/trivia"
  querystring = {"fragment":"true","notfound":"floor","json":"true"}
  headers = {
    'x-rapidapi-key': os.getenv('RAPID_KEY'),
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data = json.loads(response.text)
  trivia= json_data['text']
  return(trivia)

def get_pokemon(pokemon):                 #========================================Pokemon          
  response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
  if(response.text=="Not Found"):
    return "notfound"
  json_data=json.loads(response.text)
  pokemon_image_url=json_data["sprites"]["front_default"]
  return(pokemon_image_url)


def get_quote():                            #========================================Quote           
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

def jokes():                              #========================================Buddyjokes          
  joke= pyjokes.get_joke()
  return joke

def get_dadjoke():                          #========================================Dadjoke            
  response=requests.get("https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes")
  json_data = json.loads(response.text)
  joke= json_data['setup'] + "\n" + json_data['punchline']
  return(joke)

def get_chucknorris():                    #========================================Chucknorris           
  url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
  load_dotenv() 
  headers = {
    'accept': "application/json",
    'x-rapidapi-key': os.getenv('RAPID_KEY2'),
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }
  response = requests.request("GET", url, headers=headers)
  json_data=json.loads(response.text)
  return json_data

def get_geekjoke():                       #========================================GreekJokes           
  response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
  json_data = json.loads(response.text)
  geekjoke=json_data["joke"]
  return(geekjoke)

def get_roast():                          #========================================Roast                
  response=requests.get("https://insult.mattbas.org/api/insult")
  roast=response.text
  return(roast)

def get_news():                           #========================================News                   
  url = "https://google-news1.p.rapidapi.com/top-headlines"
  load_dotenv()
  querystring = {"country":"INDIA","lang":"en","limit":"50","media":"true"}

  headers = {
      'x-rapidapi-key': os.getenv('NEWS_API'),
      'x-rapidapi-host': "google-news1.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data=json.loads(response.text)
  return json_data

# def name(message):
#   try:
#     username = message.chat.username
#   except:
#     firstname = message.chat.first_name
#     lastname = message.chat.last_name
#     username= firstname + " " + lastname
#     return username


  

def chatbot(text):
  url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
  querystring = {"bid":"178","key":os.getenv('BOT_KEY2'),"uid":"mashape","msg":text}
  headers = {
    'x-rapidapi-key': os.getenv('BOT_KEY'),
    'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com"
    }
  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data=json.loads(response.text)
  answer=json_data['cnt']
  return answer

funny_answers=["That was so funny!","Haha","\U0001F923","\U0001F606","Lol","LMAO"]
bad_answers=["Common ! No swearing!!","Oye ! Thand Rakh!!","Bruh ! We don't do that here!!","Hey ! Don't say these things!!"]
bad_bot_reply=["\U0001F62D \n Why am I here? Just to suffer."]
good_bot_reply=["\U0001F60D \n Thank You. Love you."]

def sample_responses(message):
  message=message.lower()
  if message in ("hello", "hi", "hii", "hiii"):
    return "Hey! How's it going?"

  elif message in ("/buddyjoke", "/buddyjokes"):
    joke=jokes()
    return joke

  elif message in ("/geekjoke", "/geekjokes"):
    geekjoke = get_geekjoke()
    return geekjoke

  elif message in ("/inspire"):
    quote = get_quote()
    return quote

  elif message.startswith('/pokemon'):
    list1=message.split(" ")
    pokemon=list1[1]
    if pokemon=="buddy-bot" or pokemon=="buddy" or pokemon=="buddy_bot" or pokemon=="buddy-telegram-bot" or pokemon=="buddy_telegram_bot" or pokemon=="@buddy" or pokemon=="@buddy-bot" or pokemon=="@buddy_bot" or pokemon=="@buddy-telegram-bot" or pokemon=="@buddy_telegram_bot":
      return "Fuck You"
    else:
      pokemon_image_url=get_pokemon(pokemon)
    if(pokemon_image_url=="notfound"):
      return "Pokemon Not Found"
    else:
      return pokemon_image_url

  elif message.startswith('/trivia'):  
    try:
      list1=message.split(" ")
      trivia=get_trivia(int(list1[1]))
      return trivia.capitalize()+"."
    except:
      return "There has been an error with your command.\n The correct command is '|trivia [number]'"
    
  elif message in ('/dadjoke',"/dadjokes"): 
    try:
      joke = get_dadjoke()
      return joke
    except:
      return "Sorry. There has been a server error."

  elif message in ("/chucknorris"): 
    json_data=get_chucknorris()
    # embed=Embed(
    #   title='Chuck Norris Meme',
    #   colour=Colour.blue()
    # )
    # embed.set_thumbnail(url=json_data["icon_url"])
    # embed.add_field(name=json_data["value"],value="CNJ",inline=False)
    # embed=embed
    return json_data["value"] + "\n\n" + json_data["icon_url"]

  elif message.startswith('/roast'): 
    list3=message.split(" ")
    def filter(roast):
      roast=roast+" "
      list1=roast.split(" ")
      list2=[]
      for word in list1:
        if word == "You" or word == "you":
          list2.append(list3[1])
        elif word == "are":
          list2.append("is")
        else:
          list2.append(word)
      return " ".join(list2)
    roast=get_roast()
    roast=filter(roast)
    roast=roast+".\n#roasted\n"
    roast=roast+random.choice(funny_answers)
    return roast

  elif message.startswith("/roastme"): 
    roast=get_roast()
    
    roast1=roast+".\n#roasted "+"\n"
    roast2=roast1+random.choice(funny_answers)
    return roast2

  elif message in ("/sourcecode"):
    return "https://github.com/SohamDasBiswas/Buddy-telegram-bot"

  elif message.startswith('/news'):
    data=get_news()
    list1=message.split(" ")
    try:
      num=int(list1[1])
    except:
      num=5
    i = 1
    for item in data['articles']:
      if not(item['title']):
        continue
      return str(i)+". "+item['link']
      if i == num:
          break
      i += 1

  elif message.startswith('/buddy'): 
    list1=message.split(" ")
    text=" ".join(list1[1:])
    answer=chatbot(text)
    return answer

  # elif message.startswith('/clear'): 
  #   list1=message.split(" ")
  #   try:
  #     amount=int(list1[1])
  #   except:
  #     amount=5   
  #   client.delete_message(chat_id=message.chat_id,
  #                 message_id=message.message_id,
  #                 limit=amount)
  #   # return purge(limit=amount)

  elif message in ("who are you", "who are you?","/introduce"):
    return "Hi! I am Buddy Bot. Developed by Soham."

  elif message in ("lol","lmao","haha","xd"):
    return random.choice(funny_answers)

  elif message in ("bad bot","gu bot"):
    return random.choice(bad_bot_reply)

  elif message in ("good bot"):
    return random.choice(good_bot_reply)

  elif message in ("fuck","Fuck","Asshole","asshole"):
    # print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
    # try:
    #   username = update.message.chat.username
    # except:
    #   firstname = update.message.chat.first_name
    #   lastname = update.message.chat.last_name
    #   username= firstname + " " + lastname
    # list1=random.choice(bad_answers).split(" ")
    # str2=list1[0]
    # list1.remove(list1[0])
    # res=str2+" "+username+" ".join(list1)
    # # await message.channel.send(res)
    return random.choice(bad_answers)

  elif message in ("sad", "depressed", "unhappy", "angry", "miserable", "motivate"):
    affirmation=get_affirmations()+".\nCheer up!"
    return affirmation

  elif message in ("time", "time?", "date", "date?"):
    now=datetime.now()
    date_time=now.strftime("%d/%m/%y, %H:%M:%S")
    return str(date_time)
