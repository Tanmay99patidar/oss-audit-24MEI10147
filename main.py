import os
import platform
import helpers
import datetime

# Main logic for system audit report
def run_report():
    data = helpers.get_sys_info()
    print("========================================================")
    print("         OPEN SOURCE AUDIT — SYSTEM IDENTITY           ")
    print("========================================================")
    print("\n  Student   : [Tanmay Patidar]")
    print('  Roll No   : [24MEI10147]')
    print("  Software  : Linux Kernel\n")
    print("--------------------------------------------------------")
    print("  SYSTEM INFORMATION")
    print("--------------------------------------------------------")
    print(f"  Distribution : {data['distro']}")
    print(f"  Kernel Ver.  : {data['kernel']}")
    print(f"  Logged User  : {data['user']}")
    print(f"  Home Dir     : {data['home']}")
    print(f"  Uptime       : {data['uptime']}")
    print(f"  Date & Time  : {data['date']}\n")

# Inspection logic
def run_inspect():
    pkg = f"linux-image-{platform.release()}"
    print("========================================================")
    print("         FOSS PACKAGE INSPECTOR                        ")
    print("========================================================")
    ver = helpers.check_pkg(pkg)
    if ver:
        print(f"  [INSTALLED] {pkg} is installed.\n")
        print(f"  Version : {ver}")
    else:
        print(f'  [NOT FOUND] {pkg} not found via dpkg.')
    print("\n========================================================\n")

# Audit directory logic
def run_audit():
    targets = ["/etc", "/var/log", "/home", "/usr/bin", "/tmp", "/boot"]
    print("========================================================")
    print("         DISK AND PERMISSION AUDITOR                   ")
    print("========================================================")
    print(f"\n  {'DIRECTORY':<20} {'PERMISSIONS/OWNER':<25} {'SIZE':<10}")
    print("  ------------------------------------------------------------")
    # Direct iterator loop
    for path in targets:
        perms, size = helpers.get_dir_stats(path)
        if perms:
            print(f"  {path:<20} {perms:<25} {size:<10}")
        else:
            print(f"  {path:<20} [ does not exist ]")
    print("\n========================================================\n")

# Log analysis logic using helper
def run_logs(log_path="/var/log/syslog", key="error"):
    print("========================================================")
    print("         LOG FILE ANALYZER                             ")
    print("========================================================")
    if not os.path.exists(log_path):
        print(f"  ERROR: File '{log_path}' not found.")
        return
    matches = helpers.search_logs(log_path, key)
    print(f"  Keyword '{key}' found {len(matches)} times.")
    print("  Last 5 matches:")
    for match in matches[-5:]:
        print(f"  >> {match}")

# Manifesto generation using helper
def run_generator():
    print("========================================================")
    print("       OPEN SOURCE MANIFESTO GENERATOR                 ")
    print("========================================================")
    tool = input("  1. Tool: ")
    word = input("  2. Freedom: ")
    project = input("  3. Build: ")
    out = helpers.gen_manifesto(tool, word, project)
    print(f"\n  Saved to: {out}")

if __name__ == "__main__":
    run_report()
    run_inspect()
    run_audit()
    # Log analysis demo
    run_logs()
    # Generator demo
    # run_generator()
