from tempfile import TemporaryFile

from chess.pgn import read_game
import chess.svg

from flask import Flask, send_file, request

import requests
import argparse
import cairosvg
import imageio
from numpy import array
from PIL import Image, ImageFont, ImageDraw
import json
import datetime

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--port", dest="port", default=8080, type=int)
parser.add_argument("--bind", dest="bind", default="0.0.0.0", type=str)
parser.add_argument("--css", dest="css", type=argparse.FileType("r"), default="default.css")

settings = parser.parse_args()

app = Flask(__name__)

style = settings.css.read() if settings.css else None


@app.route('/<gameid>.gif', methods=['GET'])
def serve_gif(gameid):
    meta = request.args.get('meta')
    result = requests.get(f'https://lichess.org/game/export/{gameid}')
    data = requests.get(f'https://lichess.org/api/game/{gameid}').json()

    game = read_game(StringIO(result.text))
    size = 360
    tempfile = TemporaryFile()

    with imageio.get_writer(tempfile, mode='I', format='gif', fps=1) as writer:
        node = game
        while not node.is_end():
            nextNode = node.variation(0)
            board_svg = chess.svg.board(node.board(), coordinates=False, flipped=False, size=size, style=style)
            board_png = imageio.imread(cairosvg.svg2png(bytestring=board_svg))
            writer.append_data(board_png)
            node = nextNode
        if meta:
            splash = create_splash(size, data)
            writer.append_data(splash)

    tempfile.seek(0)

    return send_file(tempfile, mimetype='image/gif')


def create_splash(size, data):
    splash = Image.new("RGB", (size,size), color = "#929292")
    draw = ImageDraw.Draw(splash)
    font = ImageFont.truetype("Roboto-Regular.ttf", 16)
    draw.text((10, 10), "".join(("White: ",data['players']['white']['userId'],"\n","Black: ",data['players']['black']['userId'])) ,(0,0,0),font=font)
    splash.save("splash.png")
    splash = array(Image.open("splash.png"))
    return splash


if __name__ == '__main__':
    app.run(host=settings.bind, port=settings.port)