class TimeMap:

    def __init__(self):
        self.structure = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.structure:
            self.structure[key].append({"val": value, "ts": timestamp})
        else:
            self.structure[key] = [{"val": value, "ts": timestamp}]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.structure:
            return ""
        data = self.structure[key]
        l, r = 0, len(data) - 1

        while l <= r:
            mid = (l+r) // 2

            if data[mid]["ts"] == timestamp:
                return data[mid]["val"]
            elif data[mid]["ts"] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        if r == -1:
            return ""
        else:
            return data[r]["val"]


obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo", 1)
print(param_2)
