import os
import pickle

if os.path.isfile('conf.dat'):
    with open('conf.dat', 'r+b') as f:
        highscore = pickle.load(f)
else:
    with open('conf.dat', 'x+b') as f:
        highscore = []
        pickle.dump(highscore, f)
print(highscore)
