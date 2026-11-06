"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. 
def parse_line(raw_line):
    parts = raw_line.strip().lower().split()
    hostname = parts[0]
    used = float(parts[1].split("=")[1])
    total = float(parts[2].split("=")[1])
    return {
        "hostname": hostname,
        "used": used,
        "total": total
    }
raw_line = "SRV-01 USED=87 TOTAL=100"
print(parse_line(raw_line))


# ====================================================================== INPUT
# 2.
records = [
    "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
    "src=192.168.1.10, attempts=5,result=success",
    "SRC=172.16.0.2 , ATTEMPTS= 20 , RESULT=FAILED",
    "src=10.0.0.8, Attempts=3,Result=success",
    "src=192.168.0.15, Attempts=15,RESULT=failed"
]

# =============================================================== PROCESS + OUTPUT
# 3.
for raw_line in records:
    cleaned = parse_line(raw_line)
    print(cleaned)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
