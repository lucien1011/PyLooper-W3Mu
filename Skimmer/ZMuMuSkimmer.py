import numpy as np
import pickle,os

from PyLooper.common.Module import Module

class SignalRegionSkimmer(Module):
    def analyze(self,data,dataset,cfg):
        cfg.collector.selection_weight = data["passedZ1LSelection"]
