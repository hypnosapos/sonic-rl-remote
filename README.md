# Sonic RL Agent

Requirements for Mac:

```sh
$ brew install cmake openmpi lua51
```

Train model by docker container on localhost:

```sh
$ docker run -it -v <your_path>/rom.md:/usr/local/lib/python3.5/dist-packages/retro/data/SonicTheHedgehog-Genesis/rom.md \
  hypnosapos/sonic-rl-remote:latest python ppo/ppo_agent.py
```

## Training experiments within Polyaxon

Launch experiment with polyaxon:

```bash
$ source .venv/bin/activate
$ pip install polyaxon-cli

## These steps are required only for bootstrap
$ polyaxon config host=<polyaxon-api-svc-ip>
$ polyaxon login --username=root --password=<xxxxx>

## These steps are required only if sonic project doesn't exist yet
$ polyaxon project create sonic
$ polyaxon init sonic

## Train Sonic experiment
$ polyaxon run -f polyaxonfile.yml -u
```

## Run model