import sys
import os

for line in sys.stdin:
    file = line.split(":")[0]
    os.system(f"grep '<person' {file}")
    print(line.split(":").pop().strip("\n"))
    print(line.split(":")[0])
    print("\n")
    #sys.stdout.write( + "\n")