##EXAMPLE SCRIPT
# DESCRIPTION
# Example script for performing analisys
#
# Copy .csv files of interest from one of the following locations: 
# \\vcn.ds.volvo.net\cli-sd\sd0312\041061\ClutchTest
# \\vcn.ds.volvo.net\cli-sd\sd0312\041061\TorqueTest
# \\vcn.ds.volvo.net\cli-sd\sd0312\041061\
#
# Store files locally, somewhere on c: for faster performance. 
# 
# 1. Conditioning .csv files 
# 2. Load .csv files into data set
# 3. Filter data
# 4. 
# 5. 
#
## 1. Condition .csv files
#  Condition .csv files. Conditioned files will be stored in directory
#  'directoryNameDestination'.
from conditionCSVFiles import conditionCSVFiles
if __name__ == '__main__':
   conditionCSVFiles()
##
from plot import plot


#
#
#


    