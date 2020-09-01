#! /bin/bash    
echo "test" >> test.log
cd /home/ubuntu/cameleon
source /home/ubuntu/cameleon/venv/bin/activate

python3 ./run.py
