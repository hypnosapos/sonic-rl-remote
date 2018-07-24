FROM tensorflow/tensorflow:1.9.0-gpu-py3

ADD . ./

RUN apt-get update && \
    apt-get install -y --no-install-recommends libopenmpi-dev cmake git --yes && \
    apt-get clean

RUN pip install -r requirements.txt

RUN cp ./rom.md /usr/local/lib/python3.5/dist-packages/retro/data/SonicTheHedgehog-Genesis/

SHELL ["/bin/bash", "-c"]

CMD ["python", "ppo/ppo_agent.py"]