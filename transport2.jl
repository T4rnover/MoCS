using Random
using Statistics

# Parameters
max_position = 100
num_people = 1000
num_steps = 1000
car_capacity = [1, 2]
num_lanes = 2

# Initialize state
positions = zeros(Int, num_people)
lanes = zeros(Int, num_people)
cars = [car_capacity[rand(1:2)] for _ in 1:(num_people ÷ 2)]

# Run simulation
times = fill(num_steps, num_people)
for step in 1:num_steps
    # Update positions and lanes
    for i in 1:length(cars)
        if cars[i] > 0 && rand() < 0.5  # Cars move with 50% probability
            cars[i] -= 1
            positions[i*2] = min(positions[i*2] + 3, max_position)  # Cars move faster
            lanes[i*2] = rand(1:num_lanes)  # Cars change lanes at will
        end
    end
    # Calculate times
    for i in 1:num_people
        if positions[i] == max_position && times[i] == num_steps
            times[i] = step
        end
    end
end

# Analyze results
average_time = mean(times)
println("Average time: $average_time")