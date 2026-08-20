# Overview

My undergraduate thesis was about robust TLS encrypted traffic classification using contrastive learning. Since TLS hides payload contents, I used packet-length sequences as observable metadata. The main problem was that these sequences are not stable under transport-layer behavior, such as retransmission, sequence shift, and packet aggregation. I proposed TAC-Seq, a TCP-aware contrastive sequence framework. It generates perturbed views of the same flow and trains an encoder to learn representations that remain stable under transmission-level changes. Experiments on CESNET-TLS22 showed better robustness than a linear baseline and strong results against a Rosetta-style baseline, especially in RTO settings.

---

# Research Problem

My undergraduate thesis was about robust TLS encrypted traffic classification using a SimCLR-style contrastive learning framework. Since TLS hides payload contents, I used packet-length sequences as observable metadata. The main problem was that these sequences are not stable under transport-layer behavior, such as retransmission, sequence shift, and packet aggregation. I proposed TAC-Seq, a TCP-aware contrastive sequence method. It adapts the idea of contrastive views from SimCLR to packet-length sequences, generating perturbed views of the same flow and training an encoder to learn stable representations. Experiments on CESNET-TLS22 showed stronger robustness than the baselines.

---

# TAC-Seq Method

TAC-Seq means TCP-Aware Contrastive Sequence. It is based on a SimCLR-style contrastive learning idea, but the augmented views are designed for TLS packet-length sequences. For each original flow, I generate two perturbed views using TCP-related transformations, such as repetition, shift, and small-packet aggregation. These two views are treated as a positive pair, while views from other flows are treated as negative samples. By applying contrastive learning to these views, TAC-Seq trains the encoder to keep the application-related information of the flow while becoming less sensitive to transport-level sequence changes.

---

# Model and Training Pipeline

The model has two stages: contrastive pretraining and supervised classification. In pretraining, two perturbed views of the same packet-length sequence are encoded by a shared BiLSTM-Attention encoder. Then a projection head maps the encoded representations into the contrastive learning space, following the SimCLR-style design. The model is trained with NT-Xent loss, which pulls together two views from the same flow and separates views from different flows. After pretraining, the projection head is removed. The encoder is kept as a feature extractor, and a classifier is trained for the eight TLS application categories.

---

# Evaluation

I used the CESNET-TLS22 dataset and built an eight-class TLS traffic classification task. The classes include advertising, antivirus, file sharing, games, instant messaging, mail, music, and streaming media. To reflect an early classification setting, I used packet-length information from the first 30 packets of each flow. I tested four perturbation settings. I compared TAC-Seq with a linear packet-length baseline and a Rosetta-style reproduced baseline. The metrics included Accuracy, Macro-F1, and Weighted-F1.

---

# Result and limitation

The results showed that TAC-Seq clearly outperformed the linear baseline in all four perturbation settings. It also performed better than the Rosetta-style reproduced baseline in most settings, especially under RTO perturbations. In the RTO settings, both Accuracy and Macro-F1 reached about 0.93. The Nagle-related ablation showed that modeling small-packet aggregation improved performance, especially in FAST settings. The main limitation is that the dataset did not provide timestamps, so the Nagle-like aggregation had to be modeled as a heuristic approximation. The thesis also mainly used packet-length sequences, with limited use of timing or direction features.

---

