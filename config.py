DISCORD_TOKEN = ""

RPC_TYPE = "normal"  # normal / spotify / console

NORMAL_CONFIG = {
    "Title": "",
    "Description": "",
    "SubText": "",
    "Large_Image": "", # must be a link
    "Large_Image_Text": "",
    "Small_Image": "",
    "Small_Image_Text": "",
    "State": "watching", # playing / watching / streaming / competing
    "Status": "dnd",
    "Timer": True,
    "Watch_Url": "",
    "Buttons": []
}

SPOTIFY_CONFIG = {
    "SongTitle": "",
    "ArtistName": "",
    "AlbumName": "",
    "Image": "",
    "SongLength": , # seconds
    "Status": "dnd",
    "Buttons": True,
    "AlbumID": "" # https://open.spotify.com/album/(album id is here)
}

CONSOLE_CONFIG = {
    "Title": "",
    "Description": "",
    "SubText": "",
    "Large_Image": "",
    "Large_Image_Text": "",
    "Small_Image": "",
    "Small_Image_Text": "",
    "Status": "dnd",
    "Timer": True,
    "Platform": "ps5" # xbox / ps / nitendo
}
