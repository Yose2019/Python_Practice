'''
Identify the missing requirments
'''

def missing_requirements(requirement_map: dict[str, list]):
    '''
    @Description: Identifies the requirements missing for a specific application/stack/layer
    @Author: Shristhi N Akkalkot
    @inputs: dictionary 
    @returns: report
    '''

    missing_requirements = {}

    if not requirement_map:
        return {
            "Valid" : True,
            "missing_requirements" : missing_requirements
        }

    requesters = requirement_map.keys()

    validity = True

    for app, requirements in requirement_map.items():
        missing_requirement = []
        for requirement in requirements:
            if requirement not in requesters:
                missing_requirement.append(requirement)

        if missing_requirement:
            missing_requirements[app] = missing_requirement

    if missing_requirements:
        validity = False

    return {
        "Valid" : validity,
        "missing_requirements" : missing_requirements
    }



dependencies = [{
    "application": ["database", "cache", "redis"],
    "database": ["storage", "mysql"],
    "cache": ["redis"],
    "storage": []
}, {
    "application": ["database", "cache"],
    "database": ["storage"],
    "cache": ["storage"],
    "storage": []
},{
    "application": ["database", "cache"],
    "database": ["storage"],
    "cache": ["redis"],
    "storage": []
},
{
    "storage": [],
    "database": ["storage"],
    "application": ["database"]
}]

for dependency in dependencies:
    print(missing_requirements(dependency))

