# Sonic RL Agent

Requirements for training models on Mac:

```sh
$ brew install cmake openmpi lua51
```

Train model by docker container on localhost:

```sh
$ docker run -it -v <your_path>/rom.md:/usr/local/lib/python3.5/dist-packages/retro/data/SonicTheHedgehog-Genesis/rom.md \
  hypnosapos/sonic-rl-remote:latest python ppo/ppo_agent.py
```

## Training experiments within Polyaxon

We should have a polyaxon installation on any kubernetes cluster.

Run experiments with polyaxon:

```bash
$ python -m venv .venv
$ pip install polyaxon-cli

## These steps are required only for bootstrap
$ polyaxon config set --host=<polyaxon-api-svc-ip>
$ polyaxon login --username=<username> --password=<xxxxx>

## These steps are required only if sonic project doesn't exist yet
$ polyaxon project create --name=sonic
$ polyaxon init sonic

## Train Sonic experiments
$ polyaxon run -f polyaxonfile_ppo.yml -u
$ polyaxon run -f polyaxonfile_dqn.yml -u
```

## Run model

WIP
