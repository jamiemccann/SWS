import glob
import pandas as pd


DIRECTORY_PATH = 

# --- Edit path for chosen data directory ---
all_res_path = [filename for filename in glob.glob(f'{DIRECTORY_PATH}/**/*.fb1**.res')]



# --- Create dataframe of all event-station pairs ---
frames = []

for file_path in all_res_path:
    df = pd.read_csv(f'{file_path}')
    frames.append(df)

result = pd.concat(frames)



# --- Edit path for chosen data directory ---
with open("path/raypaths.xy", "w") as f:
    for i, event in result.iterrows():
        print(">", file=f)
        print(event["evlo"], event["evla"], file=f)
        print(event["slon"], event["slat"], file=f)
    print(">", file=f)
