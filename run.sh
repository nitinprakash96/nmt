#!/bin/bash

if [ "$1" = "train" ]; then
	CUDA_VISIBLE_DEVICES=0 python run.py train --train-src=./data/train.es --train-tgt=./data/train.en --dev-src=./data/dev.es --dev-tgt=./data/dev.en --vocab=vocab.json --cuda
elif [ "$1" = "test" ]; then
        CUDA_VISIBLE_DEVICES=0 python run.py decode model.bin ./data/test.es ./data/test.en outputs/test_outputs.txt --cuda
elif [ "$1" = "train_local" ]; then
	python run.py train --train-src=./data/train.es --train-tgt=./data/train.en --dev-src=./data/dev.es --dev-tgt=./data/dev.en --vocab=vocab.json
elif [ "$1" = "test_local" ]; then
    python run.py decode model.bin ./data/test.es ./data/test.en outputs/test_outputs.txt
elif [ "$1" = "vocab" ]; then
	python vocab.py --train-src=./data/train.es --train-tgt=./data/train.en vocab.json
else
	echo "Invalid Option Selected"
fi
