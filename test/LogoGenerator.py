from weblogolib import *
from PIL import Image

class LogoGenerator:

    def __init__(self, alignment_file):
        self.alignment = read_seq_data(open(alignment_file, 'r'))

    def generate_logo(self):
        data = LogoData.from_seqs(self.alignment)
        options = LogoOptions()
        options.title = "A logo title SAD"
        format = LogoFormat(data, options)
        eps = eps_formatter(data, format)

        w = open('shit.eps', 'wb')
        w.write(eps)
        w.close()

        img = Image.open('shit.eps')
        img.save('shit.png')
