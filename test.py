times = []

times.append({
        "name" : "rithix",
        "time" : 10
    })

times.append({
        "name" : "santi",
        "time" : -5
    })

times = sorted(times, key=lambda x: x["time"])

print(times)