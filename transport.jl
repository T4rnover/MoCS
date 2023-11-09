using Random
using Statistics

# Parameters
max_position = 100
num_people = 1000
num_steps = 1000
car_capacity = 2

# Initialize state
positions = zeros(Int, num_people)
cars = fill(car_capacity, num_people ÷ car_capacity)

# Run simulation
times = fill(num_steps, num_people)
for step in 1:num_steps
    # Update positions
    for i in 1:num_people
        if positions[i] < max_position
            positions[i] += rand(0:2)  # People move at random speed
        end
    end
    # Update cars
    for i in 1:length(cars)
        if cars[i] > 0 && rand() < 0.5  # Cars move with 50% probability
            cars[i] -= 1
            positions[i*car_capacity] = min(positions[i*car_capacity] + 3, max_position)  # Cars move faster
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