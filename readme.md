# Q1) [Python, C] Given an input string and a pattern, implement regular expression matching with support for ‘.’ and ‘*’.

[Solution](https://github.com/MistryWoman/Picovoice/blob/master/q1.py)


# Q2) Implement CTC as described in this paper. Your implementation should support both forward and backward propagation operations

- My approach for this question was to follow the data preparation and processing steps from the tensorflow implementation of CTC RNN
and then use the numpy implementation of CTC loss once I have the data in the right format. But I spent too much time learning about audio processing.
- Here I am linking the py files that I was trying to consolidate into one pipeline
    - Data set (A parallel corpus of .wav files with the corresponding text being spoken)
        - [Dataset](https://github.com/MistryWoman/Picovoice/tree/master/vctk-p225)
    - Data Preparation
        - [Reading audio files](https://github.com/MistryWoman/Picovoice/blob/master/audio_reader.py)
        - [File logging script](https://github.com/MistryWoman/Picovoice/blob/master/file_logger.py)
        - [Audio_caching (dont know exact function of this)](https://github.com/MistryWoman/Picovoice/blob/master/generate_audio_cache.py)
        - [Fitting RNN (includes tensorflow ctc which was supposed to be replaced)](https://github.com/MistryWoman/Picovoice/blob/master/ctc_tensorflow_example.py)
    - CTC Loss 
        - [Numpy CTC implementation](https://github.com/MistryWoman/Picovoice/blob/master/ctc.py)
        
        
        
### Some resources I used to implement CTC RNN.
- https://towardsdatascience.com/intuitively-understanding-connectionist-temporal-classification-3797e43a86c
- https://distill.pub/2017/ctc/
- https://github.com/amaas/stanford-ctc/blob/master/ctc/ctc.py
- https://sikoried.github.io/sequence-learning/08-seq2seq/seq2seq.pdf


# Q3)  LSTM (CIFG)
- To test out the CIFG LSTM , I used text from Alice in the Wonderland from Project Gutenberg.

- [Solution](https://github.com/MistryWoman/Picovoice/blob/master/CIFG_LSTM.ipynb)

- I referred to the following to decide evaluation metric
- https://arxiv.org/pdf/2006.14799.pdf

- But I felt that in this context, where we are not concerned with the semantic information conveyed by the sequence of outputs,
a simple Recall or ROUGE-1(Unigram) would serve the purpose. It can quantify how many words the model has learned correctly.

#### Instead of separately deciding what to forget and what we should add new information to, we make those decisions together. We only forget when we’re going to input something in its place. We only input new values to the state when we forget something older.
- https://gist.github.com/karpathy/d4dee566867f8291f086
- http://karpathy.github.io/2015/05/21/rnn-effectiveness/
- https://github.com/erikvdplas/gru-rnn
- https://github.com/tmatha/lstm
- http://colah.github.io/posts/2015-08-Understanding-LSTMs/
- https://cs231n.github.io/neural-networks-case-study/#grad
- https://christinakouridi.blog/2019/06/20/vanilla-lstm-numpy/
