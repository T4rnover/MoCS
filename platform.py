import platform
import psutil

# CPU information
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

# RAM information
svmem = psutil.virtual_memory()
print(f"Total: {svmem.total} bytes")
print(f"Available: {svmem.available} bytes")
print(f"Used: {svmem.used} bytes")
print(f"Percentage: {svmem.percent}%")

# System information
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")