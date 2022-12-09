from PIL import Image, ImageDraw, ImageFont

im = Image.open('source.png')


draw = ImageDraw.Draw(im)

font = ImageFont.truetype("msyh.ttc", 15) 

draw.text((76,43), ('Test rack'), fill='#0000ff', font=font)
draw.text((246,43), ('A0'), fill='#0000ff', font=font)
draw.text((76,70), ('TWS1'), fill='#0000ff', font=font)
draw.text((76,104), ('EDF-ZJ-PZ-3306'), fill='#0000ff', font=font)
draw.text((76,134), ('RF'), fill='#0000ff', font=font)
draw.text((93,165), ('2019-12-31'), fill='#0000ff', font=font)
draw.text((240,165), ('engineering department'), fill='#0000ff', font=font)

qrcode =  Image.open('qr.png')
im.paste(qrcode, (313,46))

im.save('new.png',dpi = im.info['dpi'])


