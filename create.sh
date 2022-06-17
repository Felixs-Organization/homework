#!/usr/bin/env bash


dir_name=$1


d="homework$dir_name"
/usr/bin/env bash -c "cd /Volumes/Samsung\ USB/Python; mkdir -p homework$dir_name/hw"


cd $d
touch main.py
touch __init__.py
if [ ! -d "hw" ]; then
    mkdir hw
fi
cd hw
touch main.py
touch __init__.py
touch hw.txt
echo "Done!"
echo "Remember to do \"cd $d\"!"
echo "Also, Felix, remember to put homework in hw/hw.txt!"
exit 0
