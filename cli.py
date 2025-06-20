import data_loader as dl
import analyser as anl
import visualiser as vl
import argparse

parser = argparse.ArgumentParser(description="Testing it right now")
parser.add_argument('--followers', type=str, required=True, metavar="", help="Path to the followers JSON file") # add the necessary parametres for adding the argument, metavar added to enhance the cli output
parser.add_argument('--following', type=str, required=True, metavar="", help="Path to the following JSON file")
args = parser.parse_args()