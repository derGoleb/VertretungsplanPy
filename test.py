#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# Author: Chhaileng Peng <hello@chhaileng.com>
# GitHub: @chhaileng

import sys
import os
import time



to = "gabriel.buechner@icloud.com" 
msg = """Dein Vertrungsplan

Heute:
Stunde: 1 - 2, M L1: bei Arndt folgende Änderung: Raum-Vtr. Raum: E10
Stunde: 1 - 2, EK G1: bei Barsnick folgende Änderung: Klausur Info: EK / PA 180'
Stunde: 1 - 2, GE G1: bei Bögershausen folgende Änderung: Klausur Info: GE 180' + NachschreiberInnen
Stunde: 3 - 4, GE G1: bei Lenz folgende Änderung: Klausur Info: GE 180' + NachschreiberInnen
Stunde: 3 - 4, EK G1: bei Pack folgende Änderung: Klausur Info: EK / PA 180'

Morgen:
Stunde: 7 - 8, SW ZKZ2: bei Poschmann folgende Änderung: Vtr. ohne Lehrer"""

for i in range(5):
  print("Sending '" + msg + "' ...")
  os.system('osascript scripts/sendiMessage.scpt "' + to + '" "' + msg + '"')
  time.sleep(0.5)
