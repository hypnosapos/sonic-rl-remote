# SONIC RL AGENT

Requirements for Mac:

```sh
$ brew install cmake openmpi lua51
```

Train a model by docker container:

```sh
$ docker run -it -v <your_path>/rom.md:/usr/local/lib/python3.5/dist-packages/retro/data/SonicTheHedgehog-Genesis/rom.md \
  hypnosapos/sonic-rl-remote:latest python ppo/ppo_agent.py
```
