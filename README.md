

# OpenHands: Complete Installation and Java Evaluation Guide

## Step 1: Install Mamba (Miniforge)
Mamba is used as a faster alternative to Conda for environment management.
```bash
curl -L -O "[https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname) -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh

```

## Step 2: Create and Activate the OpenHands Environment

Initialize a clean Python 3.12 environment.

```bash
mamba create -n openhands python=3.12 -y
mamba activate openhands

```

## Step 3: Install Core Dependencies

Install the necessary tools for the OpenHands ecosystem including Node.js and Poetry.

```bash
mamba install python=3.12 conda-forge::nodejs conda-forge::poetry -y

```

## Step 4: Build and Setup the Local Configuration

Prepare the project binaries and generate the configuration file.

```bash
make build
make setup-config

```

## Step 5: Configure Application Settings

Edit the `config.toml` file to include your API keys and specific workspace settings.

```bash
# Open and edit the configuration file
nano config.toml

```

## Step 6: Running the OpenHands Application

Start the main application process.

```bash
make run

```

## Step 7: Docker Base Image Preparation

Ensure you have the correct Docker image for your specific Java project.

> **Naming Convention:** `java/project_name:pr_number`

## Step 8: Data Format Transformation

Modify the input and output paths in the Python script to match your local data structure.

* **Script:** `.OpenHands/evaluation/benchmarks/multi_swe_bench/data/data_change.py`

```python
# Change the following variables inside the script:
input_file = "tmp/java_examples.jsonl"
output_file = 'tmp/new/java_examples.jsonl'

```

## Step 9: Configure the Inference Script

Update the bash script variables in `evaluation/benchmarks/multi_swe_bench/infer.sh` to define the model and agent behavior.

```bash
MODELS=("gpt")
GIT_VERSION="HEAD"
AGENT_NAME="CodeActAgent"
EVAL_LIMIT="500"
MAX_ITER="50"
NUM_WORKERS="1"
LANGUAGE="java"
DATASET="[your_dataset_directory]"

```

## Step 10: Run the Multi-SWE-Bench Evaluation

Execute the inference process.

```bash
bash evaluation/benchmarks/multi_swe_bench/infer.sh 

```

## Step 11: Install SWE-bench-Live for Java

Clone the benchmark repository and install the required modules in editable mode.

```bash
git clone --recurse-submodules https://github.com/microsoft/SWE-bench-Live.git
cd SWE-bench-Live
pip install -e .
pip install -e launch/.

```

## Step 12: Align Benchmark Data Formats

Update the `data_format.py` script to ensure the OpenHands output matches the SWE-bench-Live input requirements.

```python
# Edit the variables in data_format.py
input_file = "output.jsonl"
output_file = "patch.jsonl"

```

## Step 13: Execute Final Java Evaluation

Run the evaluation module to calculate the success rate and generate logs.

Dataset should be unchanged original data before used in Openhands "tmp/java_examples.jsonl"

```bash
python -m evaluation.evaluation \
    --dataset "path_to_dataset" \
    --platform linux \
    --split test \
    --patch_dir "patch.jsonl" \
    --output_dir logs/test \
    --workers 2 \
    --overwrite 0

```

## Step 14: Review Evaluation Results

Check the `logs/` directory for detailed breakdown of the test results.

```bash
ls logs/test

```