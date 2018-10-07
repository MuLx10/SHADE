import pyglet
import sys
song = pyglet.media.load(sys.argv[1])
song.play()
pyglet.app.run()