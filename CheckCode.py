import os
import time
import subprocess
def check(file):
    file1 = str(file).split(".")[0]
    logfile = open(file1+'.log', 'w')
    p = subprocess.Popen("python %s" % file,stdout=logfile)
    # os.system("python %s > %s.log" % (file, file1))
    time.sleep(30)
    p.kill()
    with open(file1+'.log', "r", encoding='UTF-8') as f:
        for line in f.readlines():
            if 'loss' in line:
                return True
        return False

if __name__ == '__main__':
    result=check("test_0.py")
    print(result)