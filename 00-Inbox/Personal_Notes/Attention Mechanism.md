---
tags:
  - self_note
---
### Defn
- Attention mechanism is the mechanism which helps a neural network to focus on the most relevant information when processing some information. 


---
## AI Responses

Attention is a mechanism that helps a neural network focus on the most relevant information when processing something.

Imagine reading this sentence:

> "The cat sat on the mat because it was tired."

To understand what it refers to, you pay more attention to the cat than to the mat.

That's the basic idea of attention!

### How does it work in a Transformer?

1. Compare: Each word looks at other words in the sentence.
2. Assign importance: The model calculates how relevant each word is to the current word.
3. Combine information: More relevant words contribute more strongly to the representation of the current word.


### The key idea

Without attention, a model might struggle to connect information across a long sentence. With attention, each word can use relevant information from other words to build a better understanding of context.

In one line: Attention lets a model decide what information matters most, and how much it should matter.

The equation
$$
 \operatorname{Attention}(Q,K,V)= \operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V 

$$
was popularized by "Attention Is All You Need" (2017). It is called Scaled Dot-Product Attention.
But attention mechanisms existed before 2017, particularly in machine translation.
## Major types of attention

| Type                             | Year | Main idea                                                                        |
| -------------------------------- | ---- | -------------------------------------------------------------------------------- |
| Bahdanau (Additive) Attention    | 2014 | Uses a small neural network to calculate relevance between two states            |
| Luong (Multiplicative) Attention | 2015 | Uses dot products or learned matrices to calculate relevance                     |
| Scaled Dot-Product Attention     | 2017 | Scales dot-product scores to improve numerical behavior                          |
| Multi-Head Attention             | 2017 | Runs multiple attention operations in parallel, learning different relationships |

Two other important distinctions are:
- Global vs. Local Attention (2015): Attend to every input position versus a smaller region.
- Soft vs. Hard Attention: Assign continuous weights to multiple positions versus selecting particular positions.
    
The key takeaway: Attention existed before Transformers. The fundamental idea—calculate relevance, normalize scores, and combine information—was already present in Bahdanau attention (2014).

Transformers made scaled dot-product attention central to their architecture, allowing them to process sequences without relying on RNN recurrence.