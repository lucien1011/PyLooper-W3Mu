from PyLooper.common.Dataset import Dataset
from PyLooper.common.Collector import Collector

from PyLooper.stat.Hist1D import Hist1D
from PyLooper.hep.plotter.Plotter import Plotter
from PyLooper.hep.plotter.Plot import Plot

from Skimmer.ZMuMuSkimmer import SignalRegionSkimmer
from Weighter.DataMCWeighter import DataMCWeighter
from Weighter.CrossSectionWeighter import CrossSectionWeighter
from Dataset.Bkg2017 import *
from Dataset.Data2017 import *

verbose = True
nblock = 1024
ngrid = 100
entrysteps = nblock*ngrid
namedecode = "utf-8" 

dataset_list = bkgSamples_2017 + [data2017]

for d in dataset_list:
    d.lumi = 41.7*1000.
merged_dataset_list = []

collector = Collector(
    output_path = "./output/2020_11_06_plot_bkg_Run2017_cfg/",
    )

plots = [
    Plot("massZ1",lambda data,dataset,cfg: data["massZ1"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,200.),),
    Plot("massZ2",lambda data,dataset,cfg: data["massZ2"],lambda data,dataset,cfg: cfg.collector.event_weight,hist=Hist1D(100,0.,200.),),
    ]

modules = [
    CrossSectionWeighter("CrossSection"),
    SignalRegionSkimmer("SignalRegion"),
    DataMCWeighter("DataMCWeighter"),
    Plotter("Plot",),
    ]

