import os
import sys

with open('C:/Users/andre/Uni_Documents/Dissertation/archived_websites/archived_sites.txt') as fp:
    first_line = True
    for line in fp:
        # archive url and domain seperated by a space in archived_sites file
        line = line.split(' ')
        domain = line[1]
        # archive urls obtained from wayback machine
        aurl = line[0]
        
        fpath = "C:Users/andre/Uni_Documents/Dissertation/archived_websites/results"
        
        if first_line:
            # initialises httrack project, using the first website
            # cannot init when using the --continue flag so it is excluded.
            cmd = f"httrack -O results {aurl} -* +*/{domain}/*"
            "-N1005 --depth=2 --advanced-progressinfo --can-go-up-and-down"
            "--display --keep-alive --mirror --robots=0"
            "--verbose"
        else:
            # called with continue to add to exisiting project
            cmd = f"httrack -O results {aurl} -* +*/{domain}/*"
            "-N1005 --depth=2 --advanced-progressinfo --can-go-up-and-down"
            "--display --keep-alive --mirror --robots=0"
            "--verbose --continue"
            
        print(cmd)
        os.system(cmd)
        first_line = False
        
