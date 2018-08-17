# Sonic RL Agent
[![License status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fhypnosapos%2Fsonic-rl-remote.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fhypnosapos%2Fsonic-rl-remote?ref=badge_shield)
![We love OpenSource](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

Requirements to train models on Mac:

 - python 3.5+
 - Sonic rom file 
 
```sh
$ brew install cmake openmpi lua51
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ cp rom.md .venv/lib/python3.5/dist-packages/retro/data/SonicTheHedgehog-Genesis/rom.md
$ python ppo/ppo_agent.py
$ python dqn/dqn_agent.py
```

Train model by docker container on localhost:
```sh
$ docker run -it -v <your_path>/rom.md:/usr/local/lib/python3.5/dist-packages/retro/data/SonicTheHedgehog-Genesis/rom.md \
  hypnosapos/sonic-rl-remote:latest python ppo/ppo_agent.py
```

## Training experiments within Polyaxon

Requirements:

 - We should have a polyaxon installation on any kubernetes cluster (you have and example at our carpole project).
 - Put sonic rom file on this project directory.

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
