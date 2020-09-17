import flask, telebot
import bot
import os

app = flask.Flask(__name__)
index = open('static/index.html').read()


# Process index page
@app.route('/')
def root():
    print('index!')
    return index # 'xd' # flask.send_from_directory('/static', 'index.html')


# Process webhook calls
@app.route(f'/{os.environ["TELEGRAM_TOKEN"]}', methods=['POST', 'GET'])
def webhook():
    print(flask.request)
    return ''

if __name__ == "__main__":
  
  app.run(debug=True)
