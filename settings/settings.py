# -*- coding: utf-8 -*-
#

# Imports
from torchlanguage import transforms as ltransforms
from torchvision import transforms


################
# Settings
################

# Settings
window_size = 20
hidden_dim = 500
voc_sizes = {'c1': 1628, 'c2': 21510}
class_to_idx = {False: 0, True: 1}
idx_to_class = {0: False, 1: True}
