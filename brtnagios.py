#!/usr/bin/python

from sys import exit
from optparse import OptionParser
import os
import pythoncm

def main():
    parser = OptionParser(usage="usage: %prog option",
                          version="%prog 0.1")
    parser.add_option("-o", "--occupation-rate", dest="occupation",
                action="store_true",
                default=False,
                help="Return the occupation rate of the cluster")
    parser.add_option("-d", "--down-nodes", dest="down",
                action="store_true",      
                default=False,
                help="Print number of down nodes")
    parser.add_option("-w", "--workload", dest="workload",
                action="store_true",      
                default=False,
                help="workload information")
    (options, args) = parser.parse_args()

    option_dict = vars(options)
    if sum(option_dict.values()) != 1:
       parser.error("wrong number of arguments")

    clustermanager = pythoncm.ClusterManager()

    # Add connection to your cluster using cmsh certificate
    if os.path.isfile('/root/.cm/admin.pem'):
      cluster = clustermanager.addCluster('https://localhost:8081', '/root/.cm/admin.pem', '/root/.cm/admin.key');
    elif os.path.isfile('/root/.cm/cmsh/admin.pem'):
      cluster = clustermanager.addCluster('https://localhost:8081', '/root/.cm/cmsh/admin.pem', '/root/.cm/cmsh/admin.key');
    elif os.path.isfile('/etc/nagios/cm/admin.pem'):
      cluster = clustermanager.addCluster('https://localhost:8081', '/etc/nagios/cm/admin.pem', '/etc/nagios/cm/admin.key');
    else:
      print "No certificate found"  
      exit(1)

    if not cluster.connect():
      print "Unable to connect"
      print cluster.getLastError()
      exit(1)



    overview = cluster.overview()

    if (options.occupation):
        occ = round(overview.occupationRate, 2)
        print ("OK - Occupation rate: "+str(occ)+"|rate="+str(occ))

        
    if (options.down):
        if (not(overview.nodesDown)):
            print ("OK - no node down|down=0")
        else:
            print ("WARNING - number of down nodes: "+str(overview.nodesDown)+"|down="+str(overview.nodesDown))

    if (options.workload):
        jobs = cluster.getJobs()
        print ("OK - Jobs in queue:"+str(len(jobs))+"|jobs="+str(len(jobs)))


    cluster.disconnect()



if __name__ == '__main__':
    main()
