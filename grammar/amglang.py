from lark import Lark, Transformer, v_args

music_grammar = r"""
    ?start : stmt

    ?stmt  : msg

    msg    : "(" CHORD? SBARS NUMBER ")"       -> msg

    SBARS  : NUMBER|"."

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
        tab="    "
        if any(c.type == "CHORD" for c in tree.children):
            chord, bars, duration = tree.children
            chordsdict = {
                "majT": "major_triad",
                "minT": "minor_triad",
                "dimT": "diminished_triad",
                "augT": "augmented_triad",
                "susT": "suspended_triad"
            }
            out += minspace+"raw_note = self.agent.get(\"n_v\").split(\"-\")[0]"+"\n"
            out += minspace+"c = chords."+chordsdict[chord]+"(raw_note)"+"\n"
            if bars==".":
                out += minspace+"lstatus = ast.literal_eval(self.agent.get(\"last_know_status\"))"+"\n"
                out += minspace+"i = random.randint(0, len(lstatus[0][4])-1)"+"\n"
                out += minspace+"msg.body = \'[ \'+" +"str(c)"+ "+\', ["+"\'+str(i)+\'"+"], "+duration+" ]\'"
            else:
                out += minspace+"msg.body = \'[ \'+" +"str(c)"+ "+\', ["+bars+"], "+duration+" ]\'"
        else:
            bars, duration = tree.children
            if bars==".":
                out += minspace+"lstatus = ast.literal_eval(self.agent.get(\"last_know_status\"))"+"\n"
                out += minspace+"i = random.randint(0, len(lstatus[0][4])-1)"+"\n"
                out += minspace+"msg.body = \'[ [\"\'+" +"self.agent.get(\"n_v\")"+ "+\'\"], ["+"\'+str(i)+\'"+"], "+duration+" ]\'"
            else:
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
