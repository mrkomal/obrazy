#zmiana working directory na folder zawierajacy zdjecie
import os 
os.chdir('/Users/komala/Desktop/TOM_projekt/kits19')

from starter_code.utils import load_case
from starter_code.visualize import visualize

volume, segmentation = load_case("case_00000")
visualize("case_00000","pictures")
