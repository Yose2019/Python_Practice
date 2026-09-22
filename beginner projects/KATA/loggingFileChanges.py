'''
this tells difference in the new and old config file
'''

def compare_config_files(old_config, new_config):
    if not old_config or not new_config:
        return {}

    added, deleted, changed = ([], [], [])

    for key in new_config.keys():
        if key not in old_config:
            added.append(key)
        elif old_config[key] != new_config[key]:
            changed.append(key)

    if len(changed) != len(old_config.keys()):
        for key in old_config.keys():
            if key not in new_config:
                deleted.append(key)

    return {
        "added": added,
        "deleted": deleted,
        "changed": changed
    }


old_config = {
    "timeout": 30,
    "retries": 3,
    "logging": True,
    "mode": "normal",
    "buffer_size": 4096,
    "debug": False,
    "port": 8080
}

new_config = {
    "timeout": 60,          # changed
    "retries": 3,           # unchanged
    "logging": False,       # changed
    "mode": "normal",       # unchanged
    "thread_count": 8,      # added
    "debug": False,         # unchanged
    "port": 9090            # changed
}

print(compare_config_files(old_config, new_config))



    