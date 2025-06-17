FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    git curl sudo zsh build-essential libgl1-mesa-glx tree ca-certificates \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /workshop
COPY pyproject.toml /workshop/

RUN curl -LsSf https://astral.sh/uv/install.sh | \
    env UV_INSTALL_DIR="/usr/local/bin" sh

RUN uv lock && uv sync --all-groups

COPY . /workshop

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true
RUN echo "source $HOME/.oh-my-zsh/oh-my-zsh.sh" >> $HOME/.zshrc

CMD ["zsh"]
