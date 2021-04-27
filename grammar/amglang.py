from lark import Lark, Transformer, v_args

music_grammar = r"""
    ?start : stmt

    ?stmt  : msg

    msg    : "(" SBARS NUMBER ")"       -> msg

    SBARS  : "."|NUMBER

    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

@v_args(inline=True)
class TreeToCode(Transformer):
    def msg(self, bars, duration):
        out=""
        if bars==".":
            print("add for all available")
        else:
            #out += "nv = self.agent.get(\"n_v\") \n"
            out += "msg.body = \'[ [\"\'+" +"self.agent.get(\"n_v\")"+ "+\'\"], ["+bars+"], "+duration+" ]\'"
        return out

parser = Lark(music_grammar, parser='lalr', propagate_positions=False, maybe_placeholders=False, transformer=TreeToCode())
parse = parser.parse

def test(test_input):
    # test_input = "(1 5)"
    return parse(test_input)
    # print(parse(test_input).pretty())

# if __name__ == '__main__':
#     test()
