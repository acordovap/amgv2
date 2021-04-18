import py_cui
import mingus.core.keys as keys

class CUI:
    def __init__(self, master: py_cui.PyCUI):
        self.master = master
        self.pianotext =  """
│  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │   │
│  │ │ │ │  │  │•│ │♦│ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │  │ │ │ │  │  │ │ │ │ │ │  │   │
│  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │  └┬┘ └┬┘  │  └┬┘ └┬┘ └┬┘  │   │
│   │   │   │ • │ ♦ │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │   │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
                                                         c-5                                                         """
        # │ • │ ♦ │
        self.prog_list = []
        self.behs_dict = {}

        #  block_label - pianotext
        self.bl_piano = self.master.add_block_label(self.pianotext, 0, 0, row_span = 2, column_span = 13)
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

        # label - progression
        self.lb_progtxt = self.master.add_label('Progression:', 2, 6, column_span=2, row_span=1)
        self.lb_prog = self.master.add_label('-'.join(self.prog_list), 2, 8, column_span=2, row_span=1)
        # button - add
        self.b_addpro = self.master.add_button('Add', 2, 10, column_span=1, command=self.show_menu_prog)
        # button - del
        self.b_delpro = self.master.add_button('Del', 2, 11, column_span=1, command=self.del_prog)

        # scroll_menu - Notes
        # TODO:  keybinding to update behaviours
        self.sm_notes = self.master.add_scroll_menu("Notes", 3, 0, column_span=2, row_span=4)
        self.sm_notes.add_item_list(keys.get_notes(self.sm_keysig.get()[0]))

        # scroll_menu - Behaviours
        self.sm_behs = self.master.add_scroll_menu("Behaviours", 3, 2, column_span=2, row_span=3)
        # self.sm_behs.add_key_command(py_cui.keys.KEY_ENTER, self.update_behdescr) # TODO
        # button - new behaviour
        self.b_newbeh = self.master.add_button('New', 6, 2, column_span=1, command=self.show_add_beh)
        # button - del behaviour
        self.b_delbeh = self.master.add_button('Delete', 6, 3, column_span=1, command=None)

    def update_notes(self):
        self.behs_dict = {}
        self.sm_notes.clear()
        self.sm_notes.add_item_list(keys.get_notes(self.sm_keysig.get()[0]))

    def show_menu_prog(self):
        menu_choices = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
        self.master.show_menu_popup('Please select a progression to add', menu_choices, self.add_prog)

    def add_prog(self, prog):
        self.prog_list.append(prog)
        self.lb_prog.set_title('-'.join(self.prog_list))

    def del_prog(self):
        if(len(self.prog_list) > 0):
            self.prog_list.pop()
            self.lb_prog.set_title('-'.join(self.prog_list))

    def show_add_beh(self):
        self.master.show_text_box_popup('Insert an expression', command=self.add_beh)

    def add_beh(self, beh):
        # TODO: sintaxt validation
        print('as')
        # TODO: revisar nota seleccionada y agregar a su dictionary de behaviours

root = py_cui.PyCUI(11, 13)
root.toggle_unicode_borders()
root.set_title('amgv2 - cui')

ui = CUI(root)
root.start()
