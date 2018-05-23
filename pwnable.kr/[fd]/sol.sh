#!/bin/bash
#Call the fd binary with fd=0 (STDIN) plus the magic number and pipe in the 
#answer
echo "LETMEWIN" | ./fd $(python -c 'print(0+0x1234)')
