import pexpect


output=pexpect.run("python test.py")
output=output.split("\n")
print output
