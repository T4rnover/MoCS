using CellularAutomata, Plots

states = 2
radius = 1
generations = 50
ncells = 111
starting_val = zeros(Bool, ncells)
starting_val[Int(floor(ncells/2)+1)] = 1

rule = 18

ca = CellularAutomaton(DCA(rule), starting_val, generations)

heatmap(ca.evolution, 
    yflip=true, 
    c=cgrad([:white, :black]),
    legend = :none,
    axis=false,
    ticks=false)