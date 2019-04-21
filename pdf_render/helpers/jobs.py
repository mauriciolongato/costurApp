import base64
import barcode
from barcode.writer import ImageWriter


def create_barcode(codigo, barcode_class='code128'):
    img = barcode.get_barcode_class(barcode_class)
    img_bar = img('{}'.format(codigo), writer=ImageWriter())
    img_bar.save('static/{}'.format(codigo))
    return '{}.png'.format(codigo)


def create_barcode_64(codigo, barcode_class='code128'):
    img = barcode.get_barcode_class(barcode_class)
    img_bar = img('{}'.format(codigo), writer=ImageWriter())
    img_bar.save('static/{}'.format(codigo))
    encoded = 'data:image/png;base64,' + base64.b64encode(open('static/{}.png'.format(codigo), "rb").read())
    return encoded


if __name__ == '__main__':
    create_barcode('123456789')
