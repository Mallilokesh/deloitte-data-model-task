import json
from datetime import datetime


def convertFromFormat1(jsonObject):

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": jsonObject["location"].split("/")[0],
            "city": jsonObject["location"].split("/")[1],
            "area": jsonObject["location"].split("/")[2],
            "factory": jsonObject["location"].split("/")[3],
            "section": jsonObject["location"].split("/")[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }


def convertFromFormat2(jsonObject):

    dt = datetime.fromisoformat(
        jsonObject["timestamp"].replace("Z", "+00:00")
    )

    timestamp_ms = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestamp_ms,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }


# Read JSON files

with open("data-1.json", "r", encoding="utf-8") as f:
    data1 = json.load(f)

with open("data-2.json", "r", encoding="utf-8") as f:
    data2 = json.load(f)

with open("data-result.json", "r", encoding="utf-8") as f:
    expected = json.load(f)


# Convert data

result1 = convertFromFormat1(data1)
result2 = convertFromFormat2(data2)


# Print results

print("Result from Format 1:")
print(json.dumps(result1, indent=4))

print("\nResult from Format 2:")
print(json.dumps(result2, indent=4))


# Verify

print("\nChecking Results...")

print("Format 1:", result1 == expected)
print("Format 2:", result2 == expected)