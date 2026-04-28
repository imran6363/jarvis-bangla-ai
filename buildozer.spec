[app]

title = Jarvis AI
package.name = jarvis
package.domain = org.test

source.dir = .
source.include_exts = py,kv

version = 0.1

requirements = python3,kivy,openai,gtts,playsound,speechrecognition

android.permissions = INTERNET,RECORD_AUDIO

orientation = portrait

fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1
