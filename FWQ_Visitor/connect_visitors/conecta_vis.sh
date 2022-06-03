#!/bin/bash

rm fifo_$1 2>/dev/null
mkfifo fifo_$1

echo "#!/bin/bash" > exec_$1.sh
echo "" >> exec_$1.sh
echo "echo 'cd ..' > fifo_$1" >> exec_$1.sh
echo "echo './main.py' > fifo_$1" >> exec_$1.sh
echo "echo '3' > fifo_$1" >> exec_$1.sh
echo "sleep 0.2" >> exec_$1.sh
echo "echo '$1' > fifo_$1" >> exec_$1.sh
echo "sleep 0.2" >> exec_$1.sh
echo "echo '$1' > fifo_$1" >> exec_$1.sh 

chmod +x exec_$1.sh

for i in {0..5}; do cat fifo_$1; done | bash 


