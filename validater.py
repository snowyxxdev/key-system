def validate(key: str, return_message=False):
    import requests as cloud
    key_system = "https://raw.githubusercontent.com/snowyxxdev/key-system/refs/heads/main/keys/snowycloud-key.txt" #replace the url with a different key file if needed

    # Required Modules:
    # (requests) ...

    if return_message == bool(False):
        r = cloud.request("GET", key_system)
        if str(key) == r.text:
            return True
        elif str(key) != r.text:
            return False

    elif return_message == bool(True):
        r = cloud.request("GET", key_system)
        if str(key) == r.text:
            return"Valid"
        else:
            return"Invalid"
