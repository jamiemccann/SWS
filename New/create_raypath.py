import glob
import pandas as pd


all_res_path = [filename for filename in glob.glob('/raid2/jam247/mfast/sample_data/Test_6/**/*.fb1**.res')]

frames = []

for file_path in all_res_path:
    df = pd.read_csv(f'{file_path}')
    frames.append(df)

result = pd.concat(frames)
stations = pd.read_csv("/home/tebw2/STATION_FILES/QMigrate/ASKJA_stns_QM_2007-2020_ALL.txt")
    
    
with open("/raid2/jam247/JM_Tutorials/GMT_Tutorials/BSM_Poster/askja_raypaths.xy", "w") as f:
    for i, event in result.iterrows():
        print(">", file=f)
        print(event["evlo"], event["evla"], file=f)
        print(event["slon"], event["slat"], file=f)
    print(">", file=f)    
    
    
    
    
    
    
    
