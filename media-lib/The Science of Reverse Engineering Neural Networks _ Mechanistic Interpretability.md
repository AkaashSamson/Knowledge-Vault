---
mx-uid: qeaj3pf8e45da26x7o6yiddk
video: https://www.youtube.com/watch?v=ZCxQ_IhMHPY
title: The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability
description: |-
  A practical guide to neural nets, superposition, and expts around polysemanticity. Try Explain by Scrimba: https://scrimba.com/explain?via=avb

  Preparing a Github repo for all my experiments, will share soon.
  Follow me on X for updates about upcoming videos: https://x.com/neural_avb

  To support the channel, join our Patreon: 
  https://www.patreon.com/NeuralBreakdownwithAVB

  Members get access to everything behind-the-scenes that goes into producing my videos - including code. Plus, it supports...
duration: 4085
creator: Neural Breakdown with AVB
creator_url: https://www.youtube.com/channel/UC6MhHkSosYXAD-LTXBWyLMg
tags:
  - machine-learning
  - ai
  - deep-learning
view_count: 6148
cover: https://i.ytimg.com/vi_webp/ZCxQ_IhMHPY/maxresdefault.webp
aspect_ratio: 16 / 9
---
## Notes
##### Monosemantic and Polysemantic
-  [11:48](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=709#t=11:48.87) polysemantic neurons - one neuron can fire for cat faces, legs and cars. 
- [12:15](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=735#t=12:15.30) monosemantic neurons, one neurons fire for one feature eg: cats. 
- [14:25](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=866#t=14:25.95) another example of polysemantic neurons. 

#### Superposition
-  [15:12](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=912#t=15:12.01) - Antipodal pair: 2 different features can share one number by pointing in opposite directions. 
	- common way 2 neurons can compress information?
	- what do you mean?
- [15:36](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=936#t=15:36.06) 
- a way of storing those 2 numbers into one such that you can retrieve those 2 numbers from that one.![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt15m42_56s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 15:42]]

- [15:51](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=951#t=15:51.44) autoencoder does this same job of converting high dimensional vector to lower dimensional value, by trying to output the same input vector
- the same weights used to get h and decode h![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt16m56_28s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 16:56]]

- [19:19](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=1160#t=19:19.64) ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt19m14_00s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 19:14]]

![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt19m52_88s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 19:52]]

- [20:14](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=1215#t=20:14.74) power of Relu, it just zeroes the negative value
- [20:23](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=1224#t=20:23.87) - phase change
- [20:17](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=1218#t=20:17.87) - superposition: maintaining 2 different ideas in a single dimension. 
- this is a drawback ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt21m0_79s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 21:00]]

- [23:37](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=1417#t=23:37.19) the arrows have no pattern
	- the arrows change on every retrain, 
	- they even overlap 
- [24:11](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=1451#t=24:11.40)
	- 5 arrows of linear length spread
	- always gives same outcome![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt24m31_97s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 24:31]]

#### superposition vs interference
 - interference occurs here: <90 = +ve interference and >90  = -ve  interference
 - interference is basically when here the output should be cat 1 everything else 0 but we get some noise![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt28m28_36s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 28:28]]

- Relu helps in clearly -ve noise but the +ve remains.![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt29m27_1_00s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 29:27]]

- Bias solves the +ve interference issue![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt31m40_92s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 31:40]]

- now the problem is that if cat and car were to be given as input 50: 50 then we would get dog as output because cat and car cancel each other out, the issue we had with antipodal pairs.![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt32m57_82s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 32:57]]
- this won't be an issue with more dimensions because as there is more scope to have approx 90 degree angle among each vector and thus interference will reduce by a lot. 
- ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt34m20_35s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 34:20]]
- research more about this - #bbxn
- more dimension many more features![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt35m29_87s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 35:29]]

- [38:06](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=2286#t=38:06.19) - feature importance, some features given more priority to be detected. 
- [39:44](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=2384#t=39:44.34) ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt39m44_34s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 39:44]]

- [39:49](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=2389#t=39:49.07) sparsity increases, feature importance kicks in![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt40m25_61s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 40:25]]

- [41:46](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=2507#t=41:46.54) - with I vector multiplied with xi, we can give importance to selective features. 

#### priveleged basis vs non priveleged basis

- basis vectors - \[0,1]  \[1,0] for 2 dimensional space
- when relu is placed at the hidden layer instead of output layer which is how we normally train ANN this is what we get [46:03](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=2764#t=46:03.62) ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt46m3_62s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 46:03]]
- we can observe polysemantic neurons

- [46:32](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=2792#t=46:32.48) ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt46m28_03s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 46:28]]

- [47:17](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=2837#t=47:17.05) ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt47m9_84s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 47:09]] 
- [50:01](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=3001#t=50:01.25) - denser data leads to monosemanticity 

- ![[mx-img-qeaj3pf8e45da26x7o6yiddk-pt50m54_33s.jpg|The Science of Reverse Engineering Neural Networks | Mechanistic Interpretability - 50:54]]

- [52:42](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=3163#t=52:42.78) -  a column w gives direction of one feature and row of W is what one neuron listens to. 

- [54:12](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=3252#t=54:12.29) -  more neurons we have and more sparsity leads to more chances of monosemanticity

 - [56:34](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=3394#t=56:34.08) 
 - [1:06:01](https://www.youtube.com/watch?v=ZCxQ_IhMHPY&t=3962#t=1:06:01.69) summary of what we learnt. 