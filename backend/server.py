from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from urllib.parse import unquote
from pydub import AudioSegment
import os


app = Flask(__name__)
soc = SocketIO(app)
CORS(app,resources={r"/back":{"origins":"*"}})

@soc.on('message')
def sendrep(message):
    print(message)
    decode = unquote(message.replace("file://",""))
    audio = AudioSegment.from_file(decode, format='3gp')

    temp_file ="temp.wav"
    audio.export(temp_file,format="wav")

    os.system("start " + temp_file)

if __name__=="__main__":
    soc.run(app,debug=True,host='192.168.110.39', port='3000')