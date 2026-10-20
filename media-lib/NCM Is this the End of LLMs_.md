---
mx-uid: c262oovr7hm8p4uo6grw9s53
video: https://www.youtube.com/watch?v=vLqswKyHS64
title: NCM Is this the End of LLMs?
description: |-
  Is Stanford's Next-Concept Modeling (NCM) the end of LLMs? It writes text 31x faster, but against which model, and does any of it reach your GPU?

  Every chatbot you use, ChatGPT and Gemini included, writes one token at a time, and every token makes your GPU read the model's full weights out of memory. That is why large language models feel slow on your own machine. NCM, from Stanford and Together AI, skips that. It writes in levels, a rough sketch first and the words last, using a multiscale...
duration: 1621
creator: Kai
creator_url: https://www.youtube.com/channel/UCgUfJoPtkt7-RiiuYh4vmGA
tags:
  - next-concept-modeling
  - ncm-ai
  - hybridagents-together-ai
  - end-of-llms
  - stanford-ncm
  - latent-reasoning-ai
  - diffusion-language-models
  - meta-coconut-ai
  - openai-reasoning-tokens-bill
  - autoregressive-vs-diffusion-llm
  - cloud-codes
  - claude
  - chatgpt
  - gemini
  - kimi
view_count: 87959
cover: https://i.ytimg.com/vi/vLqswKyHS64/maxresdefault.jpg
aspect_ratio: 16 / 9
---
- [01:34](https://www.youtube.com/watch?v=vLqswKyHS64&t=95#t=01:34.70) 
- [02:15](https://www.youtube.com/watch?v=vLqswKyHS64&t=136#t=02:15.55) - basically all tokens are generated sequentially. 
- [02:55](https://www.youtube.com/watch?v=vLqswKyHS64&t=176#t=02:55.65) - this is what LLMs do, read the entire previous context before writing the next token. 
- [05:14](https://www.youtube.com/watch?v=vLqswKyHS64&t=314#t=05:14.37) - performance of NCM shows to be better than LLM. 

- [06:06](https://www.youtube.com/watch?v=vLqswKyHS64&t=366#t=06:06.02) how does NCM work?
	- NCM sketches outline first and only at end gives a proper framed sentence. 
	- [07:13](https://www.youtube.com/watch?v=vLqswKyHS64&t=434#t=07:13.62) - it has 2 components
		- [07:24](https://www.youtube.com/watch?v=vLqswKyHS64&t=445#t=07:24.82) compression network which takes input text and compresses it, when feeded to decoder we get the original sentence. 
		- [07:41](https://www.youtube.com/watch?v=vLqswKyHS64&t=462#t=07:41.72) - this component is called **multiscale residual VQ-VAE.**  
			- [07:50](https://www.youtube.com/watch?v=vLqswKyHS64&t=471#t=07:50.87) NCM tokenizer vs LLM tokenizer - here the input sentence is converted into **layers of decreasing abstraction**. 
		- [07:59](https://www.youtube.com/watch?v=vLqswKyHS64&t=480#t=07:59.87) - 2nd component:Standard transformer. 
			- takes layer inputs and outputs layers and makes improvements in every step. 
		- [09:08](https://www.youtube.com/watch?v=vLqswKyHS64&t=548#t=09:08.08) - concept here is just a numerical category which is acquired from a look up table. I don't know who created this table and why?
		- [09:50](https://www.youtube.com/watch?v=vLqswKyHS64&t=591#t=09:50.1.00) diffusion models vs NCM. 

- [10:12](https://www.youtube.com/watch?v=vLqswKyHS64&t=612#t=10:12.44) in diffusion every pass has equal cost, in NCM passes have increasing costs. 
	- diffusion writes whole draft agian and again while NCM writes outlines and details and then final drafts. 

- [11:51](https://www.youtube.com/watch?v=vLqswKyHS64&t=712#t=11:51.77) - 31x speed claim is only against the diffusion models and not LLMs

- [15:37](https://www.youtube.com/watch?v=vLqswKyHS64&t=937#t=15:37.13) - NCM has tradeoffs. 
- [17:28](https://www.youtube.com/watch?v=vLqswKyHS64&t=1048#t=17:28.32) this is how NCM can be faster. 
- [24:32](https://www.youtube.com/watch?v=vLqswKyHS64&t=1473#t=24:32.80) diffusion gemma can be run right now, but it shows tradeoff between 