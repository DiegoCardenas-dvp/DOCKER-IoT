set terminal png size 800,800
set output 'output/julia_grafica.png'
set view map
set title "Conjunto de Julia - ESCOM IoT"
set pm3d map
splot 'julia_set.txt' using 1:2:3 with pm3d