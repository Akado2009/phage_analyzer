from weblogolib import *

class LogoGenerator:

    def __init__(self, alignment_file):
        self.alignment = read_seq_data(open(alignment_file, 'r'))

    def generate_logo(self):
        data = LogoData.from_seqs(self.alignment)
        options = LogoOptions()
        options.title = "A logo title SAD"
        format = LogoFormat(data, options)
        eps = eps_formatter(data, format)
