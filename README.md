# ReReEzEbSynth

W.I.P

## Installation

#### Prerequisites

- NVIDIA GPU
- CUDA Toolkit
- C++ Compiler
- uv

#### Setup

- Clone the Repository

```bash
git clone https://github.com/Haoming02/ReReEzEbSynth
cd ReReEzEbSynth
```

- Setup a Virtual Environment

```bash
uv venv venv --seed --python 3.11
venv\scripts\activate
```

- Install PyTorch

```bash
uv pip install torch==2.9.1+cu130 torchvision==0.24.1+cu130 --extra-index-url https://download.pytorch.org/whl/cu130
```

- Install Dependencies

```bash
uv pip install . --no-build-isolation
uv pip install -r requirement.txt
```
