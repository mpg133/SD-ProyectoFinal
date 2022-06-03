#!/bin/bash

for vis in $(cat visitantes)
do
    gnome-terminal -t $vis --tab -- ./conecta_vis.sh $vis
done

for vis in $(cat visitantes)
do
    ./$vis.sh
done

