## Neural Machine Translation

This is an attempt to learn the implementation of NMT model and achieve a BLEU score larger than 21.

### File Structure

- model.py: File containing the model structure.
- vocab.py: Script used to generate `vocab.json` vocabulary file.
- util.py: File containing helper functions.
- run.py: File to facilitate training and evaluation of the model.
- embeddings.py: Model embeddings

### Usage

- To generate vocabulary

    `sh run.sh vocab` or `python vocab.py --train-src=./data/train.es --train-tgt=./data/train.en vocab.json`

- To train the model

    `python run.py train --train-src=./data/train.es --train-tgt=./data/train.en --dev-src=./data/dev.es --dev-tgt=./data/dev.en --vocab=vocab.json`

- To test the model

    `python run.py decode model.bin ./data/test.es ./data/test.en outputs/test_outputs.txt`