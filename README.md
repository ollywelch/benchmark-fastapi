# Simple Benchmarking for Async vs Sync FastAPI

This repo serves as a simple example of benchmarking sync vs async FastAPI when it comes to
DB operations with sqlalchemy.

## Setup

Ensure that the prerequisite dependencies are installed

```bash
which ab  # apache benchmarking tool
which python3  # python 3 for running FastAPI
which docker-compose  # docker-compose for running the Postgres DB
```

Then install poetry, python dependencies, setup a Postgres DB, and add the required tables.
This can all be done via the *setup.sh* convenience script.

```bash
./scripts/setup.sh
```

## Running the benchmarks

Run the server you would like to benchmark with one of the following scripts

```bash
./scripts/async.sh  # start the async server
./scripts/sync.sh  # start the sync server
```

Then finally, in a separate terminal window, run

```bash
./scripts/benchmark.sh
```

and view the results!
