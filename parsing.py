import numpy as np
import pandas as pd
from point import *
import os
from trajectory import *

def build_trajectory(file):
    temp = pd.read_csv("./cabspottingdata/"+str(file),header=None,sep = ' ')
    traj = [Point(temp.loc[i, 0],temp.loc[i, 1]) for i in range(len(temp))]
    return traj


def build_trajectory_set():
    return [build_trajectory(filename) for filename in os.listdir("./cabspottingdata/")  if filename.endswith(".txt") or filename.endswith(".csv")]