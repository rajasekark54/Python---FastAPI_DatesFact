import json
import requests

def get(url: str):
  res = requests.get(url)
  return res.content
