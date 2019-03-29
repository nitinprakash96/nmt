#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from typing import List

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

# read_corpus() taken from https://github.com/pcyin/pytorch_nmt


def pad_sents(sents, pad_token):
    """ Pad list of sentences according to the longest sentence in the batch.
    @param sents (list[list[str]]): list of sentences, where each sentence
                                    is represented as a list of words
    @param pad_token (str): padding token
    @returns sents_padded (list[list[str]]): list of sentences where sentences shorter
        than the max length sentence are padded out with the pad_token, such that
        each sentences in the batch now has equal length.
    """
    sents_padded = []

    max_len = max(len(s) for s in sents)
    batch_size = len(sents)

    for i in range(max_len):
        sents_padded.append([
            sents[k][i] if len(sents[k]) > i else pad_token
            for k in range(batch_size)
        ])

    return sents_padded


def read_corpus(file_path, source):
    """ Read file, where each sentence is dilineated by a `\n`.
    @param file_path (str): path to file containing corpus
    @param source (str): "tgt" or "src" indicating whether text
        is of the source language or target language
    """
    data = []
    for line in open(file_path):
        sent = line.strip().split(' ')
        if source == 'tgt':
            sent = ['<s>'] + sent + ['</s>']
        data.append(sent)

    return data

