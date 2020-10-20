from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import Optional, List

app = FastAPI()

class Techniques(str, Enum):
  mbott= "mbott"
  khattarbi= "khattarbi"
  soukharbi= "soukharbi"

class Mbeur(BaseModel):
  nom: str
  force: int
  techniques: Optional[List[Techniques]] = []

class Ecurie(BaseModel):
  nom: str
  adresse: str
  mbeurs: Optional[List[Mbeur]] = []

@app.get("/")
def home():
  return "Hello World"

@app.post("/mbeurs/")
def post_mbeurs(mbeur: Mbeur):
  return mbeur

@app.post("/ecurie/")
def post_ecurie(ecurie: Ecurie):
  #sauvegarde dans la base
  return ecurie
