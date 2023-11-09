using DifferentialEquations, Plots
using Distributions
using LightGraphs
using PyPlot

gr()

# Set up the parameters for the SIS epidemic model
N = 1000  # Number of nodes
p = 0.05  # Probability of edge creation
beta = 0.3  # Infection rate
gamma = 0.1  # Recovery rate

# Create the configuration model network
degrees = rand(Poisson(10), N)
G = erdos_renyi(N, p)

# Initialize the state of the nodes
state = zeros(N)
state[rand(1:N, Int(0.01*N))] .= 1  # Infect a small fraction of the population

# Define the system of differential equations
function SIS_model(du, u, p, t)
    I = u[1:length(p.degrees)]
    S = u[length(p.degrees)+1:end]
    N = length(p.degrees)
    kmax = maximum(p.degrees)
    dIdt = zeros(kmax+1)
    dSdt = zeros(kmax+1)
    for k in 0:kmax
        I_k = sum(I[p.degrees .== k])
        S_k = sum(S[p.degrees .== k])
        dIdt[k+1] = p.beta * k * S_k * I_k / N - p.gamma * I_k
        dSdt[k+1] = -p.beta * k * S_k * I_k / N + p.gamma * I_k
    end
    append!(du, dIdt)
    append!(du, dSdt)
end

# Solve the system of differential equations
u0 = vcat(state, 1-state)
tspan = (0.0, 100.0)
prob = ODEProblem(SIS_model, u0, tspan, (beta=beta, gamma=gamma, degrees=degrees))
sol = solve(prob, Tsit5())

# Plot the results
function plot_results(sol)
    t = range(0, stop=100, length=1000)
    infected = sol[1:length(degrees), :]
    susceptible = sol[length(degrees)+1:end, :]
    plot(t, infected, label="Infected")
    plot!(t, susceptible, label="Susceptible")
    xlabel!("Time")
    ylabel!("Fraction of population")
    title!("SIS Epidemic Model on Configuration Model Network")
    legend!(title="")
end

plot_results(sol)