#!/bin/bash

rm $1 2>/dev/null
mkfifo $1

echo "#!/bin/bash" > $1.sh
echo "" >> $1.sh
echo "echo 'cd ..' > $1" >> $1.sh
echo "echo './main.py' > $1" >> $1.sh
echo "echo '3' > $1" >> $1.sh
echo "sleep 0.2" >> $1.sh
echo "echo '$1' > $1" >> $1.sh
echo "sleep 0.2" >> $1.sh
echo "echo '$1' > $1" >> $1.sh 

chmod +x $1.sh

for i in {0..5}; do cat $1; done | bash 


