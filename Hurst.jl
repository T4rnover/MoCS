using CSV
using DataFrames
using Plots
using HTTP
using Statistics
using GLM
using Hurst
using MarketData

gr()

# Define the URL of the data
url = "https://people.math.sc.edu/Burkardt/datasets/csv/nile.csv"

# Download the data
HTTP.download(url, "nile.csv")

# Load the data into a DataFrame
df = CSV.read("nile.csv", DataFrame)

print(first(df, 5))

# Plot the data
p = plot(df[!, :Year], df[!, :Flood])
display(p)
savefig(p, "nile_river_data.png")

# Rescaled Range Analysis
data = df[!, :Flood]
N = length(data)
n = 10  # Set the size of the segments
segments = [data[i:min(i+n-1, N)] for i in 1:n:N]

RS_values = Float64[]  # Array to store the R/S values

for segment in segments
    mean_segment = mean(segment)
    deviations = segment .- mean_segment
    cumulative_dev = cumsum(deviations)
    R = maximum(cumulative_dev) - minimum(cumulative_dev)
    S = std(segment)
    RS = R / S
    push!(RS_values, RS)
end

# Log-log plot of R/S against n
log_RS_values = log.(RS_values)
log_n_values = log.(length.(segments))
p = plot(log_n_values, log_RS_values, xscale=:log10, yscale=:log10, xlabel="log(n)", ylabel="log(R/S)", title="Log-log plot of R/S against n")
display(p)
savefig(p, "log_RS_vs_log_n.png")

println()
println("Rescaled Range (R/S) for each segment: $RS_values")

# Perform linear regression
df_regression = DataFrame(x=log_n_values, y=log_RS_values)
model = lm(@formula(y ~ x), df_regression)
println()
println("Regression coefficients: ", coef(model))

# Calculate and display the slope
slope = coef(model)[2]
println()
println("Slope of the regression line: $slope")

yahoo(:INTC)