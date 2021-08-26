import fileinput
import sys
import subprocess


print("---------------------")  # Press Ctrl+F8 to toggle the breakpoint.
print("ENGINE RELEASE SCRIPT")
print("---------------------")  # Press Ctrl+F8 to toggle the breakpoint.

engineVersion = input("Enter current engineVersion (required): ")

if not engineVersion:
    print("engineVersion is required!")
    sys.exit()

stageVersion = input("Enter stageVersion (optional): ")


# subprocess.call(["sed", "-i", "-e", 's/engineVersion=.*/engineVersion='"$1"'/', "www.txt"])
def change_version_for_properties(filepath, field_to_replace_split, value):
    version = 0
    with fileinput.FileInput(filepath, inplace=True) as file:
        for line in file:
            if field_to_replace_split in line:
                version = line.split(field_to_replace_split)[1]
                print(line.replace(version, value), end='\n')
            else:
                print(line, end="")
        print(field_to_replace_split + version + "has been changed to: " + value)



print("Change version:")
print("---------------------")
print("engineVersion =", engineVersion)
print("stageVersion =", stageVersion)
print("---------------------")

reply = input("Are versions are correct to commit (y/n)? ")
if reply == "n" or reply == "N":
    print("Enter versions again!")
    sys.exit()

 # change the file input to ../src/main/resources/pa_engine_version.properties
change_version_for_properties("/home/rabina.shrestha/Desktop/check", "engineVersion=", engineVersion)

if stageVersion:
    change_version_for_properties("/home/rabina.shrestha/Desktop/check", "stageVersion=",
                                            stageVersion)

    subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE).stdout
#123
#123
