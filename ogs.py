#!/usr/bin/python


import requests   # Install this module with "pip install requests"
import json
'''
 ogs_credentials.py is in the same place as this script and looks like this (censored because MAH KEYS):

client_id = "0819<...>2966"
client_secret = "4ad4<..>1c23"
password = "f40d15<...>e42d5"
username = "sousys"

Obviously this needs to be changed on a case by case basis or other methods can be used to store and handle these credentials.
This is just the way i chose to handle them for this. 
The client_id and client_secret can be gotten from ogs by the dev.
The password is something every user will need to enter at initial setup of any client that would use code like this
 
 '''
from ogs_credentials import *  # imports client_id, client_secret, username, password

  
def get_token(client_id, client_secret, username, password):
  '''
  The API documentation was a bit confusing since it refered to urls that were http instead of https
  and returned an error so keep that in mind when reading the api documentation.
  Also the 'data='-part of the post-request is not really needed but i included it in the request for clarity since this is how the examples in 
  the requests documentation show it. 
  '''
  url = "https://online-go.com/oauth2/access_token"
  ogs_response = requests.post(url, data={"grant_type" : "password", "client_id" : client_id, "client_secret" : client_secret, "username" : username, "password" : password})
  return ogs_response.json()["access_token"]

  
  '''
  Below are 3 simple examples of how the token then is used to get data from the API. All very simple.
  
  '''
def get_user_vitals(token):
  url = "https://online-go.com/api/v1/me/"
  vitals = requests.get(url, headers={"Authorization" : "Bearer " + token})
  return vitals.json()

def get_user_settings(token):
  url = "https://online-go.com/api/v1/me/settings"
  settings = requests.get(url, headers={"Authorization" : "Bearer " + token})
  return settings.json()

def get_user_games(token):
  url = "https://online-go.com/api/v1/me/games"
  games = requests.get(url, headers={"Authorization" : "Bearer " + token})
  return games.json()  


  
if __name__ == "__main__":
  token = get_token(client_id, client_secret, username, password)

  print "\n--- vitals ---"
  vitals = get_user_vitals(token)
  for k in vitals.keys():
    print k, ":", vitals[k]            #prints the keys and their value in the dict returned by get_user_vitals()
  
  print "\n--- settings ---"
  settings = get_user_settings(token)
  for k in settings.keys():
    print k
    for e in settings[k]:
      print "  ", e, ":", settings[k][e]  #prints the keys and their value in the dict returned by get_user_settings().         
  
  print "\n--- games ---"
  games = get_user_games(token)
  for k in games.keys():
    print k                            #print only the keys in the dict returned by get_user_games()
    
    
    