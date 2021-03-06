#!/usr/bin/env python
import getpass
import sys
import telnetlib

v = input("How many vlans to clean: ")
user = raw_input("Enter remote account: ")
password = getpass.getpass()

for h in range(242,247):
  HOST = "192.168.122." + str(h)
  tn = telnetlib.Telnet(HOST)
  tn.read_until("Username: ")
  tn.write(user + "\n")
  if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
  tn.write("sh vlan br\n")
  tn.write("conf t\n")
  tn.write("no vlan 2-" + str(v) + "\n")
  tn.write("end\n")
  tn.write("sh vlan br\n")
  tn.write("exit\n")

  print tn.read_all()

