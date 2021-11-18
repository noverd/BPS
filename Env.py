from sys import argv
import os


class BSP:
    def __init__(self, name, env, dir, start, libs):
        self.name = name
        self.env = env
        self.dir = dir
        self.start = start
        self.libs = libs

    def MakeEnv(self):
        os.mkdir(f"usr/share/bps/{self.dir}")
        os.chdir(f"usr/share/bps/{self.dir}")
        if self.env == "python3":
            os.system("python3 -m venv env")
            os.system("source env/bin/activate")
            os.system("pip install --upgrade pip")
            os.system(f"pip install {self.libs}")
            os.system("deactivate")
        os.chdir(f"usr/share/bps")
        file = open(f"installed.txt", "a")
        file.write(self.name + self.dir)


file = open(argv[1])
for i in file:
    spl = i.split("=")
    if spl[0] == "NAME":
        name = spl[1]
    elif spl[0] == "ENV":
        env = spl[1]
    elif spl[0] == "DIR":
        dir = spl[1]
    elif spl[0] == "START":
        start = spl[1]
    elif spl[0] == "LIBS":
        libs = spl[1]
BSP = BSP(name, env, dir, start, libs)
BSP.MakeEnv()
