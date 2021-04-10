# Import the lib
import py_cui

# # create the CUI object. Will have a 3 by 3 grid with indexes from 0,0 to 2,2
# root = py_cui.PyCUI(3, 3)
#
# # Add a label to the center of the CUI in the 1,1 grid position
# root.add_label('Hello py_cui!!!', 1, 1)
#
# # Start/Render the CUI
# root.start()

class CUI:
    def __init__(self, master: py_cui.PyCUI):
        self.master = master
        pianotext =  """
│  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │   │
│  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │   │
│  │ │ │ │  │  │•│ │♦│ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │   │
│  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │   │
│   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │
│ 3 │   │   │ • │ ♦ │   │   │ 4 │   │   │   │   │   │   │ 5 │   │   │   │   │   │   │ 6 │   │   │   │   │   │   │ 7 │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘"""
        self.pt = self.master.add_text_block('alan', 0, 0, row_span=4, column_span=13)
        self.pt.set_text(pianotext)

root = py_cui.PyCUI(11, 13)
root.set_title('amgv2 - cui')

ui = CUI(root)
root.start()
