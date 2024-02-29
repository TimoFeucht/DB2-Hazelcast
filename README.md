# Hazelcast - Example

This is a simple example of Hazelcast usage.
It explains how to run a Hazelcast cluster using a Docker container provided by Hazelcast.
Furthermore, it explains how to connect to the cluster and how to use the Hazelcast client to store and retrieve data
with both Python and SQL.

# Usage

All information is based on the
official [Hazelcast documentation](https://docs.hazelcast.com/hazelcast/5.3/getting-started/get-started-docker).
If there are any issues, please refer to the official documentation.

1. To run the application, you need to have Docker installed and running. If you don't have Docker installed, please
   follow the instructions on the [official website](https://docs.docker.com/get-docker/).
   Please check with following command:

```bash
docker version
```

If you do not see a version number, see the [Docker docs](https://docs.docker.com/config/daemon/) for troubleshooting
information.

3. Pull the Hazelcast Docker image from Docker Hub.

```bash
docker pull hazelcast/hazelcast:5.3.6
```

4. Create a network for the Hazelcast Docker container.

```bash
docker network create hazelcast-network
```

5. Run the Hazelcast Docker container.

**WARING:** Run Docker container in PowerShell with admin rights to avoid issues!

```bash
docker run -it --network hazelcast-network --rm -e HZ_NETWORK_PUBLICADDRESS=10.0.75.1:5701 -e HZ_CLUSTERNAME=DB2 -p 5701:5701 hazelcast/hazelcast:5.3.6
```

You should see your cluster name in the console along with the IP address of the Docker host:

![platform-cluster-name.png](res%2Fplatform-cluster-name.png)

# Appendix

## Note
The project was created with [PyCharm](https://www.jetbrains.com/pycharm/) 
and tested on a Windows 11 machine with Docker Desktop 4.26.0 and Python 3.11.
Any other environment was not tested and may not work as expected.

## Authors

This example was created by Mick Eisebraun, Timo Feucht, Lea Gastgeb and Louis Schaak for the course "Datenbanken 2:
Aktuelle Datenbanken Architekturen und Technologien". The course is part of the Bachelors's program "Informatik" at the
DHBW.
The course is taught by Rykarda Heim.

## Literature

- [Hazelcast - Start a Local Cluster in Docker](https://docs.hazelcast.com/hazelcast/5.3/getting-started/get-started-docker)
- [Docker - Get Docker](https://docs.docker.com/get-docker/)
- [Get Started with SQL Over Maps](https://docs.hazelcast.com/hazelcast/5.3/sql/get-started-sql)

