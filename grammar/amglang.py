from lark import Lark, Transformer, v_args

music_grammar = r"""
    ?start : stmt

    ?stmt  : msg

    msg    : "(" CHORD? SBARS NUMBER ")"       -> msg

    SBARS  : NUMBER|"x"

    CHORD  : "majT"|"minT"|"dimT"|"augT"|"susT"

    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

class TreeToCode(Transformer):
    @v_args(tree=True)
    def msg(self, tree):
        chordsdict = {
            "majT": "major_triad",
            "minT": "minor_triad",
            "dimT": "diminished_triad",
            "augT": "augmented_triad",
            "susT": "suspended_triad"
        }
        out=""
        minspace="                    "
        tab="    "
        n, b, d = None, None, None

        if any(c.type == "CHORD" for c in tree.children):
            chord, bars, duration = tree.children
            out += minspace+"raw_note = self.agent.get(\"n_v\").split(\"-\")[0]"+"\n"
            out += minspace+"c = chords."+chordsdict[chord]+"(raw_note)"+"\n"
            n = "\'+str(c)+\'"
        else:
            bars, duration = tree.children
            n = "[\"\'+self.agent.get(\"n_v\")+\'\"]"
        # from here 'bars' and 'duration' are set, as well as 'n'
        if bars == "x":
            out += minspace+"lstatus = ast.literal_eval(self.agent.get(\"last_know_status\"))"+"\n"
            out += minspace+"i = random.randint(0, len(lstatus[0][4])-1)"+"\n"
            b = "\'+str(i)+\'"
        else:
            b = bars
        d = duration
        out += minspace+"msg.body = \'[" +n+ ", [" +b+ "], " +d+ " ]\'"
        return out

parser = Lark(music_grammar, parser='lalr', propagate_positions=False, maybe_placeholders=False, transformer=TreeToCode())
parse = parser.parse

def test(test_input):
    return parse(test_input)
    # print(parse(test_input).pretty())
