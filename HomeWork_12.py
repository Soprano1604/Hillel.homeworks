import time
from datetime import datetime

import string

start_time = datetime.now()
time.sleep(1)

def cesar(text, shift):

    alphabet = string.printable
    new_text = ''
    for itm in text:
        if itm in text:
            char_index = alphabet.index(itm)
            new_index = (char_index + shift) % len(alphabet)
            new_text = new_text + alphabet[new_index]
        else:
            new_text = new_text + itm
    return new_text

text_to = 'Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week.'
val1 = cesar(text_to, 5)
print(val1)
def undo_cesar(text, shift):
    alphabet = string.printable
    new_text = ''
    for itm in text:
        if itm in text:
            char_index = alphabet.index(itm)
            new_index = char_index - shift
            new_text = new_text + alphabet[new_index]
        else:
            new_text = new_text + itm
    return new_text

val2 = undo_cesar(val1, 5)
print(val2)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
