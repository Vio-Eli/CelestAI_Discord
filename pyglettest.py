import contextlib
import sys
import pyglet
import tempfile
import os
import pyaudio
import speech_recognition

from celestai import settings, tts, log
from celestai import settings, log

from requests.exceptions import HTTPError
from gtts import gTTS

from sphinxbase.sphinxbase import Config, Config_swigregister
from pocketsphinx.pocketsphinx import Decoder

del pyglet.resource.path[:]
pyglet.resource.path.append(settings.MEDIA_DIR)
pyglet.resource.reindex()

music = pyglet.resource.media('double-beep.mp3')
music.play()
def exit_callback(dt):
    pyglet.app.exit()

pyglet.clock.schedule_once(exit_callback, music.duration)
pyglet.app.run()
