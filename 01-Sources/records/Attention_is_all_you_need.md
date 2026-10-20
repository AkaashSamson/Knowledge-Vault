---
type: source-record
title: "Attention Is All You Need"
description: "Foundational research paper introducing the Transformer architecture, replacing recurrent and convolutional sequence models entirely with self-attention mechanisms."
resource: "/01-Sources/files/Attention_is_all_you_need.pdf"
tags:
  - "deep-learning"
  - "nlp"
  - "llm"
  - "machine-learning"
author: "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin"
published_date: "2017-06-12"
generated:
  by: "antigravity/gemini-3.8-flash"
  at: "2026-10-20T07:55:00Z"
status: active
---

# Attention Is All You Need

## Overview
"Attention Is All You Need" (Vaswani et al., 2017) is a landmark paper in artificial intelligence that introduced the **Transformer** model architecture. Prior to this work, state-of-the-art sequence transduction and language modeling relied heavily on recurrent neural networks (RNNs, LSTMs, GRUs) and convolutional networks (ByteNet, ConvS2S). These architectures suffered from a fundamental sequential computation constraint: tokens had to be processed sequentially over time steps ($O(n)$ sequential operations), hindering training parallelization across long sequences.

The Transformer dispensed with recurrence and convolution entirely, relying solely on **self-attention mechanisms** to capture global dependencies between input and output tokens in a constant number of sequential operations ($O(1)$). This allowed for unprecedented parallelization during training, significantly reduced training times, and established new state-of-the-art results on machine translation tasks (WMT 2014 English-to-German and English-to-French). It serves as the architectural foundation for modern Large Language Models (LLMs) including GPT, BERT, Claude, and Gemini.

---

## Original Asset Information
- **Original File**: [/01-Sources/files/Attention_is_all_you_need.pdf](/01-Sources/files/Attention_is_all_you_need.pdf)
- **Primary Authors**: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin (Google Brain, Google Research, University of Toronto)
- **Publication Venue**: 31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA
- **arXiv Identifier**: [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- **Release Date**: June 12, 2017 (v1), August 2, 2023 (v7)
- **Primary Domain**: Deep Learning / Natural Language Processing / Neural Machine Translation

---

## Table of Contents & Structure

### 1. Introduction
- The sequential bottleneck of recurrent language models ($h_t = f(h_{t-1}, x_t)$).
- Parallelization constraints during training across long sequence lengths.
- Proposal of the Transformer: drawing global dependencies entirely through attention without recurrence.

### 2. Background
- Comparison with parallel convolutional models: Extended Neural GPU, ByteNet, ConvS2S.
- Path length between distant positions: linear growth ($O(n)$ in ConvS2S) and logarithmic ($O(\log_k(n))$ in ByteNet) versus constant $O(1)$ in the Transformer.
- Definition of self-attention (intra-attention) within single sequences.

### 3. Model Architecture
- **Encoder and Decoder Stacks (Section 3.1)**:
  - Stack of $N = 6$ identical layers for encoder and decoder.
  - Sub-layers include multi-head attention and position-wise feed-forward networks (FFN).
  - Residual connections around every sub-layer followed by Layer Normalization: $\text{LayerNorm}(x + \text{Sublayer}(x))$.
  - Fixed model dimensionality $d_{\text{model}} = 512$.
  - Autoregressive decoder masking to prevent future position lookahead ($i < j$).
- **Attention (Section 3.2)**:
  - **Scaled Dot-Product Attention (3.2.1)**: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$.
  - Theoretical comparison: Additive vs Dot-Product attention, scaling factor $\frac{1}{\sqrt{d_k}}$ to mitigate vanishing gradients in softmax for large $d_k$.
  - **Multi-Head Attention (3.2.2)**: Linear projections of queries, keys, and values into $h = 8$ parallel representation subspaces ($d_k = d_v = 64$).
  - **Attention Applications (3.2.3)**: Encoder self-attention, masked decoder self-attention, and encoder-decoder cross-attention.
- **Position-wise Feed-Forward Networks (Section 3.3)**:
  - Two linear transformations with ReLU activation: $\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$.
  - Inner dimension $d_{ff} = 2048$.
- **Embeddings and Softmax (Section 3.4)**:
  - Learned embeddings mapping tokens to vectors of dimension $d_{\text{model}}$.
  - Weight-sharing between embedding layers and pre-softmax linear transformation, multiplied by $\sqrt{d_{\text{model}}}$.
- **Positional Encoding (Section 3.5)**:
  - Fixed sinusoidal encodings of varying frequencies ($10000^{2i/d_{\text{model}}}$) added to input embeddings to inject sequence order without recurrence.

### 4. Why Self-Attention
- Comparison of layer types (Self-Attention vs Recurrent vs Convolutional):
  - Computational complexity per layer: $O(n^2 \cdot d)$ vs $O(n \cdot d^2)$ vs $O(k \cdot n \cdot d^2)$.
  - Minimum sequential operations: $O(1)$ vs $O(n)$ vs $O(1)$.
  - Maximum path length between signals: $O(1)$ vs $O(n)$ vs $O(\log_k(n))$.
- Interpretability and attention head specialization (e.g. syntax, anaphora resolution).

### 5. Training
- Datasets: WMT 2014 English-German (4.5M sentence pairs, BPE 37K vocabulary) and English-French (36M sentence pairs, WordPiece 32K vocabulary).
- Hardware: 8 NVIDIA P100 GPUs (12 hours for base model, 3.5 days for big model).
- Optimizer: Adam ($\beta_1 = 0.9, \beta_2 = 0.98, \epsilon = 10^{-9}$) with linear warmup (4000 steps) and inverse-square-root learning rate schedule.
- Regularization: Residual dropout ($P_{\text{drop}} = 0.1$), label smoothing ($\epsilon_{ls} = 0.1$).

### 6. Results
- Machine Translation:
  - WMT 2014 En-De: 28.4 BLEU (big model), outperforming prior best ensemble by +2.0 BLEU.
  - WMT 2014 En-Fr: 41.8 BLEU (single model) at a fraction of prior training FLOP costs.
- Model variations: Impact of head count $h$, key size $d_k$, model size, and sinusoidal vs learned positional embeddings.
- Generalization: Successfully applied to English constituency parsing on WSJ Penn Treebank without task-specific tuning.

### 7. Conclusion
- Replaced recurrence with multi-head self-attention for sequence modeling.
- Outlook towards multi-modal models, restricted self-attention for long sequences, and non-sequential generation.

---

## Key Topics & Suggested Wiki Targets
Candidate concepts and topics to extract during `/process-source`:
1. `Transformer Architecture` (`concept`): The encoder-decoder self-attention paradigm.
2. `Scaled Dot-Product Attention` (`concept`): The mathematical formulation $\text{softmax}(QK^T/\sqrt{d_k})V$ and gradient scaling rationale.
3. `Multi-Head Attention` (`concept`): Multiple representation subspaces vs single-head averaging.
4. `Sinusoidal Positional Encoding` (`concept`): Parameter-free sequence ordering mechanism.
5. `Self-Attention vs Recurrence Complexity` (`topic`): Trade-offs between sequence length $n$, hidden dimension $d$, and parallelization.
6. `Encoder-Decoder Attention Masking` (`concept`): Preventing leftward information leakage in autoregressive decoders.

---

## Processing Log
- [ ] Fully Processed
- **Processed Sections**: None yet (Awaiting `/process-source` execution).
