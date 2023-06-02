import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# Configurações de autenticação
scope = "playlist-modify-private"
client_id = "9045e2878da1421ab6d22ea3991627a4"
client_secret = "fe0e6a7e0e9c491db6d33b0ba750276c"
redirect_uri = "http://localhost:8888/callback"

# Criação do objeto SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

# IDs das playlists que você deseja misturar
playlist_id1 = "6tpobp0RQ2f1hboe7XRaez"
playlist_id2 = "51PU6fMHLzWu1W2Je2NWgT"

# Obtendo as faixas das playlists
playlist1 = sp.playlist_items(playlist_id1)
playlist2 = sp.playlist_items(playlist_id2)

# Embaralhando as faixas de ambas as playlists
random.shuffle(playlist1["items"])
random.shuffle(playlist2["items"])

# Criando uma nova playlist para as músicas combinadas
new_playlist = sp.user_playlist_create(user=sp.me()["id"], name="ROCK MAIS FODASE AINDA", public=False)

# Adicionando as músicas da primeira playlist à nova playlist
tracks1 = [track["track"]["id"] for track in playlist1["items"]]
sp.playlist_add_items(new_playlist["id"], tracks1)

# Adicionando as músicas da segunda playlist à nova playlist
tracks2 = [track["track"]["id"] for track in playlist2["items"]]
sp.playlist_add_items(new_playlist["id"], tracks2)

print("Nova playlist criada com sucesso!")
