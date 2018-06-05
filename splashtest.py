from PIL import Image, ImageFont, ImageDraw
from numpy import array
import datetime
import cairosvg

lightgrey = '#8f8f8f'
grey = '#acacac'
darkgrey = '#1a1a1a'

def create_splash(size, data):
    splash = Image.new("RGB", (size,size), color = darkgrey)

    draw = ImageDraw.Draw(splash)
    font = ImageFont.truetype("NotoSans-Regular.ttf", 16)
    lichessfont = ImageFont.truetype("Roboto-Regular.ttf", 30)
    fontcolour = (grey)
    startx = size/8
    starty = size/15
    
    logo = Image.open('lichess_icon.png', 'r')
    logo = logo.resize((round(size/5), round(size/5)), resample=Image.BILINEAR)
    splash.paste(logo, (round(startx*4.8), round(size/2)-round(size/8)), logo)


    draw.text((startx*1.5, round(size/2)-30), "lichess", grey, font=lichessfont)
    draw.text((startx*3.6, round(size/2)-30), ".org", lightgrey, font=lichessfont)
    #draw.text((startx*4, starty*5.5), "lichess", grey, font=lichessfont)
    #draw.text((startx*6.1, starty*5.5), ".org", lightgrey, font=lichessfont)

    #draw.text((startx, starty*2.5), f"White: {data['players']['white']['userId']}" ,fontcolour,font=font)
    #draw.text((startx, starty*3.5), f"Rating: {data['players']['white']['rating']}" ,fontcolour,font=font)
    #draw.text((startx, starty*6.5), f"{data['clock']['initial']//60}+{data['clock']['increment']}" ,fontcolour,font=font)
    #draw.text((startx, starty*7.5), f"{datetime.datetime.fromtimestamp(int(str(data['createdAt'])[:-3])).strftime('%d-%m-%Y')}" ,fontcolour,font=font)
    #draw.text((startx, starty*10), f"Black: {data['players']['black']['userId']}" ,fontcolour,font=font)
    #draw.text((startx, starty*11), f"Rating: {data['players']['black']['rating']}" ,fontcolour,font=font)

    #indent = round(size/20)
    #draw.line([(indent,indent),(indent, size-indent),(size-indent,size-indent),(size-indent, indent),(indent,indent)], fill=grey, width=2)

    splash.save("splash.png")
    splash.show()
    #splash = array(Image.open("splash.png"))
    #return splash

create_splash(360,{"id":"nyMfOUDN","rated":True,"variant":"standard","speed":"rapid","perf":"rapid","createdAt":1527594943864,"lastMoveAt":1527595676785,"turns":67,"color":"black","status":"mate","clock":{"initial":600,"increment":0,"totalTime":600},"players":{"white":{"userId":"clarkey-the-smurf","rating":1819,"ratingDiff":17},"black":{"userId":"troj00","rating":1952,"ratingDiff":-15}},"winner":"white","url":"https://lichess.org/nyMfOUDN/black"})
