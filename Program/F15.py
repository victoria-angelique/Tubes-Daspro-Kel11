# Module Loading Data
# Kontributor : Enrique Alifio Ditya/16521253

import functions as func
import argparse
import os
from config import ROOT_DIR
import variables as var

parser = argparse.ArgumentParser()
parser.add_argument('folder', help='nama folder tempat penyimpanan data')
args = parser.parse_args()

def load():
# Prosedur untuk meloading data dari folder tertentu.
# I.S data sudah ada, F.S data loaded ke dalam program.
# KAMUS LOKAL
#   path : string
# ALGORITMA
    path = os.path.join(ROOT_DIR, args.folder)
    print()
    func.loading("Loading")
    print()
    if func.isWhitespace(args.folder):
        print("Tidak ada nama folder yang diberikan!")
        return
    elif not os.path.exists(path):
        print("Folder " + str(args.folder) + " tidak ditemukan.")
        return
    else:
        print("Selamat datang di antarmuka Binomo! ヽ(o^ ^o)ﾉ")
        print("Mohon login terlebih dahulu untuk mengakses fitur penuh.")
        print()
        var.user = func.convertData(os.path.join(path, "user.csv"))
        var.game = func.convertData(os.path.join(path, "game.csv"))
        var.riwayat = func.convertData(os.path.join(path, "riwayat.csv"))
        var.kepemilikan = func.convertData(os.path.join(path, "kepemilikan.csv"))
        var.running = True
        return