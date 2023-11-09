using DifferentialEquations

# Parameters
beta = 0.1
gamma = 0.05
N = 1000
I0 = 10
R0 = 0
S0 = N - I0 - R0

# SIR model differential equations
function sir!(du, u, p, t)
    S, I, R = u
    du[1] = -beta * S * I / N
    du[2] = beta * S * I / N - gamma * I
    du[3] = gamma * I
end

# Initial conditions
u0 = [S0, I0, R0]

# Time span
tspan = (0.0, 200.0)

# Solve the differential equations
prob = ODEProblem(sir!, u0, tspan)
sol = solve(prob)

# Plot the results
using Plots
plot(sol, xlabel="Time", ylabel="Number of individuals", label=["Susceptible" "Infected" "Recovered"])