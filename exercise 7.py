# D1
a= "SRV-01"
b= "srv-01"
print (a==b)
print(a.lower() == b.lower())

# D2
name= "record check console"
print(name.title())
print(name.upper())
original = "SRV-01"
print(original.lower())
print(original)
#original does not change because strings are irreplacable or immutable
#.lower() returns a new string instead of changing the original


# D3
raw = "srv-01"
print(f"[{raw}]")
print(f"[{raw.strip()}]")


# D4
messy = "***srv-01***"
print(messy.strip("*"))
print(messy.lstrip("*"))
print(messy.rstrip("*"))

field = "SRV-01"
print(field.strip().lower())


# D5
line= "2026-09-08 ERROR failed login"
print("ERROR" in line)
print("error" in line)
print("error" in line.lower())


# D6
print(line.find("ERROR"))
print(line.find("WARNING"))

# D7
hostname = "srv_01_east"
print(hostname.replace("_","-"))

# D8
lines = ["ERROR disk full", "INFO: back up complete", "ERROR: timeout"]
for line in lines:
    if line.startswith("ERROR"):
        print("Needs attention:", line)
print("report.csv". endswith(".csv"))
print("ERROR ERROR INFO ERROR".count("ERROR"))



# D9
messy= "srv-01 used=87 total=100"
print(messy.split())

# D10
key, value = "used=87".split("=")
print(key)
print(float(value))


# D11
record="srv-01,used=87,total=100"
print(record.split(","))
print(record.split(",", 1))


# D12
parts = ["srv-01", "used=87","total=100"]
print(",".join(parts))
print(" | ".join(parts))



# D13
parts = ["srv-01", "used=87","total=100"]
key1,value1= parts[1].split
key2,value2 = parts[2].split
print([value1,value2])


# D14
.strip()=hostname_part
print(rest)



# D15
parse_line (raw_line)
parse_line("SRV-02,used=120,total=100")


# C1
srv1=OK
srv2=OVERLIMIT
srv3=OK
PRINT("SRV")


# C2
srv-07
print(srv-07)