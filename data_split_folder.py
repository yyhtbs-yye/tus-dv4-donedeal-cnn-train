import os
from numpy import random as rd
in_fdname = "train_types/"
out_fdname = "test_types/"
categories = ["cars", "motorbikes", "plantmachinery"]
for category in categories: 
    for fname in os.listdir(in_fdname+category+"/"):
        in_path = in_fdname + category + "/" + fname
        out_path = out_fdname + category + "/" + fname
        if rd.randint(0, 10) == 0:
            os.system(f"mv {in_path} {out_path}")