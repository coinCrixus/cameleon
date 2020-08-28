FROM gitpod/workspace-postgres

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/

RUN python3 -m venv /workspace/cameleon/venv
RUN source /workspace/cameleon/venv/bin/activate
RUN pip install -r /workspace/cameleon/requirements.txt
