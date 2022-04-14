import functions as func
import argparse
import os
from config import ROOT_DIR

parser = argparse.ArgumentParser()
parser.add_argument('folder', help='nama folder tempat penyimpanan data')
args = parser.parse_args()

def load():
# Prosedur melakukan loading data dari tempat penyimpanan folder yang telah dispesifikasikan
# I.S Data belum terdefinisi, F.S Data termuat ke dalam sistem
    path = os.path.join(ROOT_DIR, args.folder)
    if func.isWhitespace(args.folder):
        print("Tidak ada nama folder yang diberikan!")
        return False
    elif not os.path.exists(path):
        print("Folder " + str(args.folder) + " tidak ditemukan.")
        return False
    else:
        print("Selamat datang di antarmuka Binomo! ヽ(o^ ^o)ﾉ")
        print("Mohon login terlebih dahulu untuk mengakses fitur penuh.")
        user = func.convertData(os.path.join(path, "user.csv"))
        game = func.convertData(os.path.join(path, "game.csv"))
        riwayat = func.convertData(os.path.join(path, "riwayat.csv"))
        kepemilikan = func.convertData(os.path.join(path, "kepemilikan.csv"))
        return (user, game, riwayat, kepemilikan)
