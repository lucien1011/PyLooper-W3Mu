import os

from PyLooper.hep.cms.dataset.CMSDataset import CMSDataset
from PyLooper.hep.root.TFile import TFile

# ____________________________________________________________________________________________________________________________________________ ||
input_dir           = "/cmsuf/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"
tree_path_in_file   = "Ana/passedEvents"

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_2017 = CMSDataset(
    "DYJetsToLL_M10To50",
    [TFile(os.path.join(input_dir,"DYJetsToLL_M10To50.root"),tree_path_in_file,),],
    xs = 15810.0,
    sumw = 37951928.0,
    plot_name = "DYJetsToLL_M10To50"
    )
# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_2017 = CMSDataset(
    "DYJetsToLL_M50",
    [TFile(os.path.join(input_dir,"DYJetsToLL_M50.root"),tree_path_in_file,),],
    xs = 5343.0,
    sumw = 18700012.0,
    plot_name = "DYJetsToLL_M50"
    )
# ____________________________________________________________________________________________________________________________________________ ||
TTJets_2017 = CMSDataset(
    "TTJets",
    [TFile(os.path.join(input_dir,"TTJets.root"),tree_path_in_file,),],
    xs = 54.23,
    sumw = 100907248.0,
    plot_name = "TTJets"
    )
# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_2017 = CMSDataset(
    "WZTo3LNu",
    [TFile(os.path.join(input_dir,"WZTo3LNu.root"),tree_path_in_file,),],
    xs = 5.052,
    sumw = 8721088.0,
    plot_name = "WZTo3LNu"
    )

# ____________________________________________________________________________________________________________________________________________ ||
bkgSamples_2017 = [
        #TTJets_2017,
        DYJetsToLL_M10To50_2017,
        DYJetsToLL_M50_2017,
        WZTo3LNu_2017,
        ]

for b in bkgSamples_2017:
    b.branches = [
        "genWeight",
        "passedFullSelection",
        "passedZXCRSelection",
        "passedZ1LSelection",
        "dataMCWeight",
        "pileupWeight",
        "massZ1",
        "massZ2",
        ]
