import pexpect
child=pexpect.spawn("ssh mithun@192.168.6.66")
child.expect('Password:')
child.sendline('google')
child.expect('.*')
child.sendline('ps -ef | grep "8000"')
child.expect('.*')
child.sendline('exit')
child.interact()
