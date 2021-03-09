from shared import config as CFG
from agents.song import *

import time
from spade import quit_spade

if __name__ == "__main__":

    # init songs
    s = []
    for i in range(CFG.no_songs):
        jid1 = "s_" + str(i) + CFG.XMPP_SERVER
        passwd1 = "."
        s.append(SongAgent(jid1, passwd1) )
        s[i].start().result()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            quit_spade()
            break
