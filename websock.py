import asyncio
import websockets
import youtube_dl
import os

async def hello(websocket, path):
    dlopts = dict(
        format='bestaudio', 
        postprocessors=[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        outtmpl='music/%(title)s.%(ext)s'        
    )
    while True:
        msg = await websocket.recv()
        try:
            with youtube_dl.YoutubeDL(dlopts) as ydl:
                ydl.download([msg],)
                await websocket.send(ydl.extract_info(msg, download=False).get('title', None))
        except Exception as e:
            print(e)

start_server = websockets.unix_serve(hello, '/tmp/251_ws.sock')
asyncio.get_event_loop().run_until_complete(start_server)
os.chmod('/tmp/251_ws.sock', 0o666)
asyncio.get_event_loop().run_forever()
