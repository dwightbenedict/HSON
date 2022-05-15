import json


def jsonify(headers):
    entries = headers.splitlines()
    headers_tuple = []

    for entry in entries:
        headers_list = entry.split(" ")
        key = headers_list[0]

        if key.endswith(":"):
            key = headers_list[0][:-1]

        else:
            return "Invalid HTTPS headers format"
        
        if key.startswith(":"):
            key = key[1:]

        value = " ".join(headers_list[1:])

        if '"' in value:
            value = value.replace('"', "'")

        entry_tuple = (key, value)
        headers_tuple.append(entry_tuple)

    headers_dict = dict(headers_tuple)
    request_headers = json.dumps(headers_dict, sort_keys=False, indent=4)
    return request_headers
