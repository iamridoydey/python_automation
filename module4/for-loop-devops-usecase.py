servers=("server1", "server2", "server3")
for server in servers:
    print(f"configure_monitoring_agent {server}")


databases = ("db1", "db2", "db3")
for database in databases:
    print(f"register_backup {database}")
    
    