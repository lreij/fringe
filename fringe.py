# -*- coding:utf-8 -*-
## Jerry Lu <lreij@163.com>
from __future__ import with_statement
import os
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "No folder specifid."
        return
    source = sys.argv[1]
    if os.path.isdir(source):
        for root, dirs, files in os.walk(source):
            for f in files:
                if f.endswith('py'):
                    file_path = os.path.join(root, f)
                    new_file = []
                    new_file.append('import fringe')
                    new_file.append('\n')
                    for line in open(file_path):
                        start =  line.find('def ')
                        if start != -1:
                            new_file.append(line[:start]+'@fringe.func_flow')
                            new_file.append('\n')
                        new_file.append(line)
                    with open(file_path, 'w') as file:
                        file.write(''.join(new_file))
    else:
        print "It is not a folder."
