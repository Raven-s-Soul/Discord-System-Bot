from flask import Flask
import logging
from threading import Thread

app = Flask('')
# disables the connection infos
log = logging.getLogger('werkzeug')
log.disabled = True


@app.route('/')
def home():
  return "Keep the BOT alive!"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
