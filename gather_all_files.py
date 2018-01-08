import os
from os import path

print("running script ..")

print("updating ./sublime files ..")

try:
    os.system("rm -rf sublime")
    print("./sublime directory removed")
except FileNotFoundError as e:
    pass

print("creating sublime directory ..")
os.mkdir("sublime")


def surround_with_single_quotes(s):
    return '\'{}\''.format(s)


os.chdir("sublime")

for f in os.listdir("/home/jigar/.config/sublime-text-3/Packages/User"):
    abs_path = path.join("/home/jigar/.config/sublime-text-3/Packages/User", f)
    if(not path.isdir(abs_path) and (abs_path.endswith(".sublime-settings") or abs_path.endswith(".sublime-build"))):
        source = surround_with_single_quotes(abs_path)
        destination = surround_with_single_quotes(f)
        os.system("cp %s %s" % (source, destination))

print("sublime files copying finished .. ")

os.chdir(path.pardir)

print("now copying .zshrc ..")

os.system("cp ~/.zshrc .zshrc")

print(".zshrc file copying complete")

print("Execution complete")
