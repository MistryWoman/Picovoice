# Some resources I used to implement CTC RNN.
- https://towardsdatascience.com/intuitively-understanding-connectionist-temporal-classification-3797e43a86c
- https://distill.pub/2017/ctc/
- https://github.com/amaas/stanford-ctc/blob/master/ctc/ctc.py
- https://sikoried.github.io/sequence-learning/08-seq2seq/seq2seq.pdf


# LSTM (CIFG)
#### Instead of separately deciding what to forget and what we should add new information to, we make those decisions together. We only forget when we’re going to input something in its place. We only input new values to the state when we forget something older.
- https://gist.github.com/karpathy/d4dee566867f8291f086
- http://karpathy.github.io/2015/05/21/rnn-effectiveness/
- https://github.com/erikvdplas/gru-rnn
- https://github.com/tmatha/lstm
- http://colah.github.io/posts/2015-08-Understanding-LSTMs/
- https://cs231n.github.io/neural-networks-case-study/#grad

- https://christinakouridi.blog/2019/06/20/vanilla-lstm-numpy/

- evaluation of generated text
- https://arxiv.org/pdf/2006.14799.pdf