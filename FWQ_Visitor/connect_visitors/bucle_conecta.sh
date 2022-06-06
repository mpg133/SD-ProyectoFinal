#!/bin/bash

for vis in $(cat visitantes)
do
    gnome-terminal --tab -- echo $vis && ./conecta_vis.sh $vis
    sleep 0.6
done
