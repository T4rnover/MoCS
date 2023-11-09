using HTTP, JSON

# Your Shodan API key
api_key = "1eyndHbFQ004x9FbQHqZ7SbBXqLB0ECq"

# Prompt for a query
println("Enter the query: ")
query = readline()

# Make a request to the Shodan API
response = HTTP.get("https://api.shodan.io/shodan/host/search?key=$(api_key)&query=$(query)")

# Parse the response
data = JSON.parse(String(response.body))

# Print the results
for result in data["matches"]
    println("IP: ", result["ip_str"])
    println(result["data"], "\n")
end
