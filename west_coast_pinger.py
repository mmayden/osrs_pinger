#This script will ping all west coast osrs worlds and return the first world
#in the dict of worlds with the lowest ping

import os
import subprocess
import re

#dictionary for assigning    key:value  world:ping
worlds = {
6 : 0,
7 : 0, 
13: 0, 
15: 0,
23: 0,
24: 0,
25: 0,
26: 0,
27: 0,
28: 0,
29: 0,
30: 0, 
31: 0,
32: 0,
33: 0,
34: 0,
31: 0,
32: 0,
38: 0,
39: 0,
40: 0,
47: 0, 
48: 0,
55: 0,
56: 0,
57: 0,
74: 0, 
78: 0,
118: 0,
119: 0, 
120: 0,
121: 0,
122: 0,
128: 0,
129: 0,
130: 0,
131: 0,
132: 0,
133: 0,
134: 0,
135: 0,
136: 0,
137: 0,
138: 0,
139: 0,
140: 0,
141: 0,
142: 0,
143: 0,
144: 0,
145: 0}

#counter used in for loop for testing
counter = 0

for x in worlds:
    world = 'oldschool' + str(x) + '.runescape.com'
    ping_result = subprocess.check_output(['ping', world])
    strip = re.search('time=(.+?)ms TTL', str(ping_result))
    worlds[x]=(int((strip).group(1)))
    #counter+=1
    #if (counter==3): break
    
print ('Use this world: ' + str(((min(worlds, key=worlds.get))) + 300))

os.system('pause')