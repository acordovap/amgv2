from lark import Lark, Transformer, v_args

music_grammar = r"""
    ?start : stmt

    ?stmt  : msg

    msg    : "(" CHORD? SBARS NUMBER ")"       -> msg

    SBARS  : NUMBER

    CHORD  : "majT"|"minT"|"dimT"|"augT"|"susT"

    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

class TreeToCode(Transformer):
    @v_args(tree=True)
    def msg(self, tree):
        out=""
        minspace="                    "
        # if bars==".":
        #     print("add for all available")
        # else:
            # out += "nv = self.agent.get(\"n_v\") \n"
            # print("chord")
            # out += minspace+"msg.body = \'[ [\"\'+" +"self.agent.get(\"n_v\")"+ "+\'\"], ["+bars+"], "+duration+" ]\'"
        if any(c.type == "CHORD" for c in tree.children):
            chord, bars, duration = tree.children
            chordsdict = {
                "majT": "major_triad",
                "minT": "minor_triad",
                "dimT": "diminished_triad",
                "augT": "augmented_triad",
                "susT": "suspended_triad"
            }
            out += minspace+"raw_note = self.agent.get(\"n_v\").split(\"-\")[0]\n"
            out += minspace+"c = chords."+chordsdict[chord]+"(raw_note)\n"
            out += minspace+"msg.body = \'[ \'+" +"str(c)"+ "+\', ["+bars+"], "+duration+" ]\'"
        else:
            bars, duration = tree.children
            out += minspace+"msg.body = \'[ [\"\'+" +"self.agent.get(\"n_v\")"+ "+\'\"], ["+bars+"], "+duration+" ]\'"
        return out

parser = Lark(music_grammar, parser='lalr', propagate_positions=False, maybe_placeholders=False, transformer=TreeToCode())
parse = parser.parse

def test(test_input):
    # test_input = "(1 5)"
    return parse(test_input)
    # print(parse(test_input).pretty())

# if __name__ == '__main__':
#     test()
