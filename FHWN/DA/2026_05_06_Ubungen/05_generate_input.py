import random
from datetime import datetime
from names import NAMES


with open(f"02_{datetime.now().isoformat()}.txt", "w") as f:
    f.write(f"{'NAME':32} | {'START':6} | {'DAYS':4} \n")
    for _ in range (random.randint(150,200)):
        f.write(f"{random.choice(NAMES):32} | {random.randint(1,360):6} | {random.randint(1,10):4} \n")
