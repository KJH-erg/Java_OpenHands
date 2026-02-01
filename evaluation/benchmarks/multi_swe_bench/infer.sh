#!/bin/bash


BASE_SCRIPT="./evaluation/benchmarks/multi_swe_bench/scripts/run_infer.sh"

MODELS=("gpt")
GIT_VERSION="HEAD"
AGENT_NAME="CodeActAgent"
EVAL_LIMIT="500"
MAX_ITER="50"
NUM_WORKERS="2"
LANGUAGE="java"
DATASET="/home/kjh/main/Java_OpenHands/evaluation/benchmarks/multi_swe_bench/data/new_java_examples.jsonl"


for MODEL in "${MODELS[@]}"; do
    echo "=============================="
    echo "Running benchmark for MODEL: $MODEL"
    echo "=============================="

    $BASE_SCRIPT \
        "$MODEL" \
        "$GIT_VERSION" \
        "$AGENT_NAME" \
        "$EVAL_LIMIT" \
        "$MAX_ITER" \
        "$NUM_WORKERS" \
        "$DATASET" \
        "$LANGUAGE"

    echo "Completed $MODEL"
done
