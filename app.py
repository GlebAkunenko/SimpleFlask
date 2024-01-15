from flask import Flask
import config

app = Flask(__name__)


@app.route('/')
def handle_any():  # put application's code here
    return config.reply_message


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
