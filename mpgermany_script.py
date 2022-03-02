import pandas as pd
import numpy as np
import math

df = pd.read_excel("mpgermany.xlsx", "Foglio1", header = 0)

# Possible coalitions:
coalitions = []
# C1 "TRAFFIC LIGHT" - SPD + G + FDP
c1_parties = ["SPD", "G", "FDP"]
coalitions.append(c1_parties)
# C2 "JAMAICA" - CDU + G + FDP
c2_parties = ["CDU", "G", "FDP"]
coalitions.append(c2_parties)
# C3 "GRAND COALITION" - CDU + SPD
c3_parties = ["CDU", "SPD"]
coalitions.append(c3_parties)
# C4 LEFT-WING COALITION - SPD + G + LINKE (No absolute majority!)
c4_parties = ["SPD", "G", "LINKE"]
coalitions.append(c4_parties)

#PARTY VECTORS

spd = df[df["partyabbrev"]=="SPD"].loc[:, "per101":"per706"].to_numpy()
g = df[df["partyabbrev"]=="G"].loc[:, "per101":"per706"].to_numpy()
fdp = df[df["partyabbrev"]=="FDP"].loc[:, "per101":"per706"].to_numpy()
cdu = df[df["partyabbrev"]=="CDU"].loc[:, "per101":"per706"].to_numpy()
linke = df[df["partyabbrev"]=="LINKE"].loc[:, "per101":"per706"].to_numpy()

#COALITION MATRICES

c1 = df[df["partyabbrev"].isin(c1_parties)].loc[:,"per101":"per706"].to_numpy()
c2 = df[df["partyabbrev"].isin(c2_parties)].loc[:,"per101":"per706"].to_numpy()
c3 = df[df["partyabbrev"].isin(c3_parties)].loc[:,"per101":"per706"].to_numpy()
c4 = df[df["partyabbrev"].isin(c4_parties)].loc[:,"per101":"per706"].to_numpy()

#IDEOLOGICAL CENTERS (Avg)

b1 = c1.mean(axis = 0)
b2 = c2.mean(axis = 0)
b3 = c3.mean(axis = 0)
b4 = c4.mean(axis = 0)

#DISTANCES FROM CENTER ( d_[party]_b[n] ) AND OVERALL DISTANCE ( d[n] )

distances = []

d_spd_b1 = math.sqrt(np.sum((b1-spd)**2))
d_g_b1 = math.sqrt(np.sum((b1-g)**2))
d_fdp_b1 = math.sqrt(np.sum((b1-fdp)**2))
d1 = d_spd_b1 + d_g_b1 + d_fdp_b1
distances.append(d1)

d_cdu_b2 = math.sqrt(np.sum((b2-cdu)**2))
d_g_b2 = math.sqrt(np.sum((b2-g)**2))
d_fdp_b2 = math.sqrt(np.sum((b2-fdp)**2))
d2 = d_cdu_b2 + d_g_b2 + d_fdp_b2
distances.append(d2)

d_cdu_b3 = math.sqrt(np.sum((b3-cdu)**2))
d_spd_b3 = math.sqrt(np.sum((b3-spd)**2))
d3 = d_cdu_b3 + d_spd_b3
distances.append(d3)

d_spd_b4 = math.sqrt(np.sum((b4-spd)**2))
d_g_b4 = math.sqrt(np.sum((b4-g)**2))
d_linke_b4 = math.sqrt(np.sum((b4-linke)**2))
d4 = d_spd_b4 + d_g_b4 + d_linke_b4
distances.append(d4)

for c,d in zip(coalitions, distances):
    print(c, ": ", d, "\n")



