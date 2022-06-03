#!/bin/bash

for vis in $(cat visitantes)
do
    gnome-terminal -t $vis --tab -- echo $vis && ./conecta_vis.sh $vis
    sleep 0.5
done
