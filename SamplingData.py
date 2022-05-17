# Importing Modules
import statistics
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

# Reading Data
df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

# Creating Graph
fig = ff.create_distplot([data], ["Reading Time"], show_hist=False)
fig.layout.update({
    "title": "Reading Time Of All Population",
    "xaxis": {"title": "Reading Time"}
})
fig.show()

# Finding Mean & Standard Deviation
population_mean = statistics.mean(data)
population_std_deviation = statistics.stdev(data)
print("Mean Of The Data Is: ", population_mean)
print("Standard Deviation Of The Data Is: ", population_std_deviation)
print()

# Finding Mean & Standard Deviaiton For Sample Data (100 Times)
dataset = []
for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)

print("Mean Of Sample Data(100 Times): ", mean)
print("Standard Deviation Of Sample Data(100 TImes): ", std_deviation)
print()

# Finding Mean For Sample Data (1000 Times)
def random_set_of_mean(count):
    dataset = []
    for i in range(0, count):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(list):
    df = list
    mean = statistics.mean(df)
    figure = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.layout.update({
        "title": "Reading Time Of All Population",
        "xaxis": {"title": "Reading Time"}
    })
    figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    figure.show()

def main():
    list = []
    list1 = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(1000)
        set_of_means1 = random_set_of_mean(30)
        list.append(set_of_means)
        list1.append(set_of_means1)
    show_fig(list)
    show_fig(list1)
    
    # Mean For 1000 Times
    mean = statistics.mean(list)
    print("Mean Of Sampling Distribution(1000 Times): ", mean)
    
    # Mean For 30 Times
    mean1 = statistics.mean(list1)
    print("Mean Of Sampling Distribution(30 Times): ", mean1)
    print()

main()

# Finding Standard Deviation OF Sample Data
def std_deviation():
    list = []
    list1 = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(1000)
        set_of_means1 = random_set_of_mean(30)
        list.append(set_of_means)
        list1.append(set_of_means1)

    # Standard Deviation For Sample Data (1000 Times)
    std_deviation = statistics.stdev(list)
    print("Standard Deviation Of Sampling Distribution(1000 Times): ", std_deviation)

    # Standard Deviation For Sample Data (30 Times)
    std_deviation1 = statistics.stdev(list1)
    print("Standard Deviation Of Sampling Distribution(30 Times): ", std_deviation1)

std_deviation()