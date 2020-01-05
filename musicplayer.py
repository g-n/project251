import flask
import requests
import os
import pygame.mixer


app = flask.Flask(__name__)
pygame.mixer.init()

@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', )
def index():
    song = flask.request.args.get('song')
    cmd = flask.request.args.get('cmd')
    if song is not None:
            pygame.mixer.music.load('music/{}.mp3'.format(song))
            pygame.mixer.music.play(0)
    if cmd == "play":      
        pygame.mixer.music.unpause()
    if cmd == "pause":              
        pygame.mixer.music.pause()

    songs = os.listdir('music/')
    songs.sort(key=lambda x: os.path.getmtime('music/' + x), reverse=True)
    songs = [song.strip('.mp3') for song in songs]
    return flask.render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
