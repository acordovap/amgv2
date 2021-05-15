from lark import Lark, Transformer, v_args

triads = "\"m\"|\"M\"|\"dim\""
sevenths = "\"m7\"|\"M7\"|\"7\"|\"m7b5\"|\"dim7\"|\"m/M7\"|\"mM7\""
augmentedchords = "\"aug\"|\"+\"|\"7#5\"|\"M7+5\"|\"M7+\"|\"m7+\"|\"7+\""
suspendedchords = "\"sus4\"|\"sus2\"|\"sus47\"|\"sus\"|\"11\"|\"sus4b9\"|\"susb9\""
sixths = "\"6\"|\"m6\"|\"M6\"|\"6/7\"|\"67\"|\"6/9\"|\"69\""
ninths = "\"9\"|\"M9\"|\"m9\"|\"7b9\"|\"7#9\""
elevenths = "\"11\"|\"7#11\"|\"m11\""
thirteenths = "\"13\"|\"M13\"|\"m13\""
alteredchords = "\"7b5\"|\"7b9\"|\"7#9\"|\"67\"|\"6/7\""
special = "\"5\"|\"NC\"|\"hendrix\""

music_grammar = r"""
    ?start      : stmt

    ?stmt       : msg

    msg         : "(" SBARS TIME CHORD? ")"                 -> msg

    SBARS       : NUMBER|"b"

    TIME        : NUMBER|"t"|"T"

    CHORD       : {c1}|{c2}|{c3}|{c4}|{c5}|{c6}|{c7}|{c8}|{c9}|{c10}

    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
""".format(c1=triads,c2=sevenths,c3=augmentedchords,c4=suspendedchords,c5=sixths,c6=ninths,c7=elevenths,c8=thirteenths,c9=alteredchords,c10=special)
# using ontly triads for chords until migrate to Earley
music_grammar = r"""
    ?start      : stmt

    ?stmt       : msg

    msg         : "(" SBARS TIME CHORD? ")"                 -> msg

    SBARS       : NUMBER|"b"

    TIME        : NUMBER|"t"|"T"

    CHORD       : {c1}

    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
""".format(c1=triads)

class TreeToCode(Transformer):
    @v_args(tree=True)
    def msg(self, tree):
        out=""
        minspace="                    "
        tab="    "
        n, b, d = None, None, None

        if any(c.type == "CHORD" for c in tree.children):
            bars, duration, chord = tree.children
            out += minspace+"raw_note = self.agent.get(\"n_v\").split(\"-\")[0]"+"\n"
            out += minspace+"c = chords.from_shorthand(raw_note+\""+chord+"\")"+"\n"
            n = "\'+str(c)+\'"
        else:
            bars, duration = tree.children
            n = "[\"\'+self.agent.get(\"n_v\")+\'\"]"
        ### from here 'bars' and 'duration' are set, as well as 'n' ###
        if bars == "b":
            out += minspace+"lstatus = ast.literal_eval(self.agent.get(\"last_know_status\"))"+"\n"
            out += minspace+"i = random.randint(0, len(lstatus[0][4])-1)"+"\n"
            b = "\'+str(i)+\'"
        else:
            b = bars

        if duration == "t": # generate a time that matches with denominator bar
            out += minspace+"lstatus = ast.literal_eval(self.agent.get(\"last_know_status\"))"+"\n"
            out += minspace+"d = lstatus[0][3][1]"+"\n"
            d = "\'+str(d)+\'"
            pass
        elif duration == "T": # generate a time that matches with bar size
            out += minspace+"lstatus = ast.literal_eval(self.agent.get(\"last_know_status\"))"+"\n"
            out += minspace+"d = lstatus[0][3][1]/lstatus[0][3][0]"+"\n"
            d = "\'+str(d)+\'"
        else:
            d = duration
        out += minspace+"msg.body = \'[" +n+ ", [" +b+ "], " +d+ " ]\'"
        return out

parser = Lark(music_grammar, parser='lalr', propagate_positions=False, maybe_placeholders=False, transformer=TreeToCode())
parse = parser.parse

def test(test_input):
    return parse(test_input)
    # print(parse(test_input).pretty())
