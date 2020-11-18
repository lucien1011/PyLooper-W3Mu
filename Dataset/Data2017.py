import os

from PyLooper.hep.cms.dataset.CMSDataset import CMSDataset
from PyLooper.hep.root.TFile import TFile

# ______________________________________________________________________ ||
input_dir           = "/cmsuf/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/"
tree_path_in_file   = "passedEvents"

# ______________________________________________________________________ ||
data2017 = CMSDataset(
        "Data2017",
        [TFile(os.path.join(input_dir,"skimZ1L_Data_Run2017-17Nov2017_noDuplicates.root"),tree_path_in_file,),],
        isMC = False,
        )

# ______________________________________________________________________ ||

data2017.branches = [
        #"genWeight",
        "passedFullSelection",
        "passedZXCRSelection",
        "passedZ1LSelection",
        #"dataMCWeight",
        #"pileupWeight",
        "massZ1",
        "massZ2",
        ]
