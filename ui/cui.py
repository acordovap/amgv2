import py_cui
import mingus.core.keys as keys

class CUI:
    def __init__(self, master: py_cui.PyCUI):
        self.master = master
        pianotext =  """
│  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │   │
│  │ │ │ │  │  │•│ │♦│ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │   │
│  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │   │
│   │   │   │ • │ ♦ │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
                                                         c-5                                                         """
        # │ • │ ♦ │

        #  block_label - pianotext
        self.bl_piano = self.master.add_block_label(pianotext, 0, 0, row_span = 2, column_span = 13)
        self.bl_piano.add_text_color_rule('♦', py_cui.RED_ON_BLACK, 'contains', match_type='regex', include_whitespace=True)

        # scroll_menu - Key Signature
        self.sm_keysig = self.master.add_scroll_menu("Key Signature", 2, 0, column_span=2)
        self.sm_keysig.add_item_list(keys.keys)
        self.sm_keysig.add_key_command(py_cui.keys.KEY_ENTER, self.update_notes)

        # scroll_menu - Tempo
        self.sm_tempo = self.master.add_scroll_menu("Tempo", 2, 2, column_span=2)
        self.sm_tempo.add_item_list(list(range(60, 240, 10)))

        # scroll_menu - Time Signature
        self.sm_timesig = self.master.add_scroll_menu("Time Signature", 2, 4, column_span=2)
        self.sm_timesig.add_item_list(['4/4'])

        # button - progression
        self.b_prog = self.master.add_button('progression', 2, 6, column_span=2, command=None)

        # scroll_menu - Notes
        self.sm_notes = self.master.add_scroll_menu("Notes", 3, 0, column_span=2, row_span=3)

    def update_notes(self):
        #print(str(self.sm_keysig.get))
        self.sm_notes.clear()
        self.sm_notes.add_item_list(keys.get_notes(self.sm_keysig.get()[0]))

root = py_cui.PyCUI(11, 13)
root.toggle_unicode_borders()
root.set_title('amgv2 - cui')

ui = CUI(root)
root.start()
