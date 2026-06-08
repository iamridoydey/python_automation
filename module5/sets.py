
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}


def getServer(server_name):
    return server_config.get(server_name, {}).get("status", "Server Not Found!")



if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}

    print(set1)
    print(set2)

    union = set1.union(set2)

    print(union)

    inter = set1.intersection(set2)
    print(inter)


    isSubset = set1.issubset(set2)
    print(isSubset)

    isSuperset = set1.issuperset(set2)
    print(isSuperset)

    isUnionSubset = set2.issubset(union)
    print(isUnionSubset)

    isUnionSuperset = union.issuperset(set1)
    print(isUnionSuperset)
    
    
    server_name = "server1"
    serverStatus = getServer(server_name)
    print(f"{server_name} is {serverStatus}")