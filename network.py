#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()



for n in range (10,15):
    print "Telnet to host" + str(n)
    HOST = "192.168.115." + str(n)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")


    tn.write("conf t\n")
    tn.write("bann motd #Wlecome project saleh#\n")
    tn.write("username saleh password cisco123\n")
    tn.write("access-list 100 permit tcp any any eq telnet\n")
    tn.write("access-list 100 permit tcp any any eq ftp\n")
    tn.write("vtp domain saleh\n")
    tn.write("vtp mode transparent\n")
    tn.write("vtp password 12345\n")
    tn.write("spanning-tree mode rapid-pvst\n")
    tn.write("ip http server\n")
    tn.write("line con 0\n")
    tn.write("exec-timeout 0 0\n")
    tn.write("password cisco\n")
    tn.write("login\n")
    tn.write("snmp-server location CTI_HQ\n")
    tn.write("snmp-server location CTI_HQ\n")
    tn.write("snmp-server contact admin@saleh.com\n")
    tn.write("snmp-server host 192.168.1.3 version 2c ciscolab\n")
    tn.write("snmp-server enable traps\n")
    tn.write("router ospf 10\n")
    tn.write("network 0.0.0.0 0.0.0.0 area 0\n")

    for n in range (2,30):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")

    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()
