#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install spotipy')


# In[2]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


# In[3]:


client_credentials_manager = SpotifyClientCredentials(client_id='81b7174bfde94f90ab0d7d82060e9a56', client_secret='4db4dabaa01443cab472156c9389069a')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# In[ ]:


def get_song_data(playlist_link):
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

    df2 = pd.DataFrame()
    i = 0
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        i += 1

        #URI
        track_uri = track["track"]["uri"]
        print("TRACK", i," in ", track_uri, " COMPLETED")

        #Track name
        track_name = track["track"]["name"]

        #Main Artist
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)

        #Name, popularity, genre
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]

        #Album
        album = track["track"]["album"]["name"]

        #Popularity of the track
        track_pop = track["track"]["popularity"]

        explicit_bool = track["track"]["explicit"]
        release_date = track['track']['album']['release_date']
        data = {
        "URI": track_uri,
        "TrackName": track_name,
        "ArtistURI": artist_uri,
        "ArtistName": artist_name,
        "ArtistPopularity": artist_pop,
        "ArtistGenres": artist_genres,
        "Album": album,
        "TrackPopularity": track_pop,
        "Explicit": explicit_bool,
        "ReleaseDate": release_date

    }
        data.update( sp.audio_features(track_uri)[0] )

        # Append the data as a new row to the DataFrame
        df2 = df2.append(data, ignore_index=True)
    return df2




# ## HIT SONGS

# In[22]:


# big on the internet playlist
df_hit_1 = get_song_data('https://open.spotify.com/playlist/37i9dQZF1DX5Vy6DFOcx00')
# viral hits playlist
df_hit_2 = get_song_data("https://open.spotify.com/playlist/37i9dQZF1DX2L0iB23Enbq")


# In[23]:


# TikTok Hit Songs Playlist
df_hit_3 = get_song_data('https://open.spotify.com/playlist/65LdqYCLcsV0lJoxpeQ6fW')


# In[24]:


# best tiktok songs
df_hit_4 = get_song_data('https://open.spotify.com/playlist/7Kk2Rm8vnJDqgq2Bpfhbvz')
df_hit_5 = get_song_data('https://open.spotify.com/playlist/0SRdjSDz4RsuozwHv1zhvr')


# In[25]:


df_hit_6 = get_song_data('https://open.spotify.com/playlist/7ne55gJlVJMIEWSLp4jp93')
df_hit_7 = get_song_data('https://open.spotify.com/playlist/37i9dQZF1DX7EqpAEG8F4f')


# In[26]:


df_hit_8 = get_song_data('https://open.spotify.com/playlist/1sHavJaWdEh60q88w6snL2')


# In[27]:


df_hit_9 = get_song_data('https://open.spotify.com/playlist/3triKLL9rNe7erR8xiYlkt?si=47955c50d92c4ae1')


# In[35]:


df_hit_10 = get_song_data('https://open.spotify.com/playlist/4QuKMsnW1xttSEt6qlburc?si=b17519cc089d46d0')


# In[36]:


# df_hit_total = df_hit_1.append(df_hit_2)
# df_hit_total = df_hit_total.append(df_hit_3)
# df_hit_total = df_hit_total.append(df_hit_5)
# df_hit_total = df_hit_total.append(df_hit_7)
# df_hit_total = df_hit_total.append(df_hit_8)
df_hit_total = pd.DataFrame()
df_hit_total = pd.concat([df_hit_1, df_hit_2, df_hit_3, df_hit_4, df_hit_5, df_hit_6, df_hit_7, df_hit_8,df_hit_9, df_hit_10])


# In[31]:


df_hit_total.columns


# In[37]:


df_hit_exp = df_hit_total


# In[40]:


df11 = df_hit_exp.drop_duplicates(subset=['TrackName'])


# In[41]:


df11


# In[42]:


df11.to_csv("TOPSONGS500.csv")


# ## NOT HITS

# In[44]:


l1 = ['https://open.spotify.com/playlist/546NXCbeShkJYrLnAzzVdC?si=00763a8841524599',
'https://open.spotify.com/playlist/4ldT2pgf6V7QiiH2RtKMRl?si=f0ff8d87fbb54e1d',
'https://open.spotify.com/playlist/4uc9tuc3IIeozrfsmSx2K9?si=05c0f5c9ab334f4c',
'https://open.spotify.com/playlist/4U7Cj82gdEKAkQiXA8XS1z?si=49866ae651de457e',
'https://open.spotify.com/playlist/3MLASveiNFXBjjK5QOaOnn?si=d0123866d0e1413c']


df_flop_1 = get_song_data(l1[0])
df_flop_2 = get_song_data(l1[1])
df_flop_3 = get_song_data(l1[2])
df_flop_4 = get_song_data(l1[3])
df_flop_5 = get_song_data(l1[4])


# In[46]:


df_flop_6 = get_song_data('https://open.spotify.com/playlist/2v3JI4Dp77YarWW08pEWaf?si=c68eeb6b31c1427c')


# In[49]:


df_flop_7 = get_song_data('https://open.spotify.com/playlist/5sDcMty6ybIxUo4Wvbhi4E?si=61bb9db4a1b740f1')


# In[52]:


df_flop_total = pd.concat([df_flop_1, df_flop_2, df_flop_3, df_flop_4, df_flop_5, df_flop_6, df_flop_7])
df12 = df_flop_total.drop_duplicates(subset=['TrackName'])


# In[53]:


df12


# In[54]:


df12.to_csv('NOTHITSONGS.csv')


# In[ ]:




