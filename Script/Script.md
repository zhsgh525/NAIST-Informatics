# Ability verification

My main background is my undergraduate thesis on TLS encrypted traffic classification.

In that project, I worked with packet-length sequences, designed traffic augmentations, implemented a contrastive learning framework, and evaluated the model under different perturbation settings.

Through this work, I learned how to handle encrypted traffic data, how to design baselines, and how to evaluate robustness under changing network conditions.

These experiences are directly useful for my proposed research, because the new project also requires traffic data collection, metadata-based analysis, baseline comparison, and careful evaluation.

Of course, DoH detection has different challenges, especially private resolvers and short flows. So my first step would be to build a small reproducible testbed and reproduce a simple single-flow baseline before developing the host-level model.

---

My background is my undergraduate thesis on TLS encrypted traffic classification.

I worked with packet-length sequences, traffic augmentation, contrastive learning, and robustness evaluation.

This gives me experience with encrypted traffic data and metadata-based analysis.

For the new project, I would first build a small reproducible testbed and reproduce a simple single-flow baseline.

----

# Figure/Table

Figure 1 shows the TAC-Seq framework from my undergraduate thesis.

The input is a packet-length sequence. Two augmented views are generated from the same original flow, using TCP-related perturbations such as repetition, shift, and aggregation.

These two views are passed through the same encoder and projection head, and the model is trained with contrastive loss. The purpose is to learn a representation that is stable under transmission-level changes.

---

Figure 2 shows the main idea of my proposed research.

The left side is the single-flow baseline. It judges a candidate flow only from its own metadata.

The right side is the host-level model. It adds a short time window around the candidate flow and uses aggregated information from the same host.

This figure shows the change of observation unit from one isolated flow to a host window.

---

Table 1 defines what the experiment must prove.

RQ1 checks whether changing the observation unit is useful at all. RQ2 checks whether the result is real generalization, not just learning particular resolvers. RQ3 checks whether the method is still usable when deployment costs are considered.

So this table separates the research into three levels: effectiveness, generalization, and practicality

---

Table 2 defines how to avoid an easy but misleading experiment.

If resolver, query form, network condition, and window size are not controlled, a high score may come from an easy setting. For example, the model may recognize known resolvers, long flows, or stable network conditions.

So this table is mainly about experimental control. It forces the evaluation to test the difficult cases directly.

---

# Design defense

I chose this design because the main challenge is the amount of evidence available for detection.

For short-lived DoH traffic, one encrypted flow may be too small to support a stable decision. If I only use a more complex model on the same short flow, the input information may still be insufficient.

So I use a short host-level time window around the candidate flow. This gives the detector nearby traffic patterns from the same monitored host, while keeping the setting close to practical network monitoring.

I also start with interpretable metadata features and simple baselines. This helps me check whether the improvement really comes from the host-level context before introducing a more complex model.

---

# Reference

#### Rosetta

It studied robust TLS encrypted traffic classification under different network environments, using TCP-aware traffic augmentation.

It supports my undergraduate research background, especially the idea that transport-level behavior can change packet-length sequences and should be considered in encrypted traffic classification.

My current proposal is different because it does not focus on improving TLS classification robustness; it applies the broader idea of observable traffic evidence to short-lived DoH detection.

#### SimCLR

It proposed a simple contrastive learning framework using augmented views and a contrastive loss.

It supports the learning framework used in my undergraduate thesis, especially the idea of learning representations from two related views of the same sample.

In my proposal, SimCLR is background for my past work, not the main method of the new DoH project.

#### RFC 8484

It defines DNS over HTTPS, which sends DNS queries and responses over HTTPS.

It supports the basic definition of DoH in my proposal and explains why DNS traffic can be hidden inside HTTPS.

In my research, this protocol definition is the starting point for deciding what traffic should be generated and detected in the testbed.

#### Comparative Analysis of DoH Detectors

It compared existing DoH detection methods and discussed their strengths and limitations.

It supports my motivation that DoH detection can depend on known resolvers, traffic patterns, or evaluation conditions, and that difficult cases still remain.

My research is different because it tests a specific design choice: whether host-level context helps short-lived DoH detection for unseen private resolvers.

#### Katsura et al.

It studied host-based data aggregation for efficient intrusion detection in IoT networks.

It supports the idea that host-level aggregation can be useful in practical security monitoring.

My research is different because I apply the host-level idea to encrypted DoH traffic, especially short-lived flows where single-flow evidence may be limited.

#### RFC 9250

It defines DNS over dedicated QUIC connections, also known as DNS over QUIC.

It supports the future extension part of my proposal, showing that encrypted DNS is not limited to DoH.

My current research does not focus on DoQ; I mention it as a possible later extension after studying DoH.

#### Other

Yes. Besides the cited papers, I mainly checked two related directions.

One is DoH Insight. It uses flow-level information and machine learning to detect DoH traffic. It helped me understand what kind of metadata features are commonly used in DoH detection.

The other is CIRA-CIC-DoHBrw-2020. It is a controlled DoH dataset, so it helped me understand how DoH and non-DoH traffic can be generated and labeled in an experimental setting.

These works gave me background on DoH detection, but my proposal uses them mainly to design a stricter evaluation setting.

---

# Case value

Private resolvers and very short DoH flows are worth studying because they remove two common advantages of existing detectors.

If the resolver is public and known, an address list may already work. If the flow is long, the classifier can use richer packet statistics. But in my target case, the endpoint is unseen and the flow itself contains very limited information.

This is exactly the situation where a detector’s robustness is tested. It is also relevant to low-visibility communication, because an attacker or unauthorized client can reduce traffic volume and avoid well-known resolvers.

So I use this case to test the difficult boundary of DoH detection, rather than only evaluating easy cases.

---

# Simulation

A controlled dataset cannot represent every kind of real network traffic, but it is still useful for the first evaluation.

The reason is that this project needs clear labels and controlled variables. In real traffic, it is often hard to know exactly which flow is DoH, which resolver is used, and whether the behavior comes from the resolver, the client, or the background traffic.

With a controlled testbed, I can isolate the key factors: public or private resolver, short or ordinary query pattern, network condition, and train-test split.

After confirming the mechanism in this setting, the next step would be testing with more realistic background traffic if available. 

---

# Master outcome

In the master’s program, I want to finish a small but complete experimental study.

The first deliverable is a working data collection and analysis pipeline. I should be able to generate traffic, label it correctly, and convert packet traces into usable records.

The second deliverable is a fair comparison between the basic approach and my proposed approach.

The third deliverable is an analysis of where the approach works, where it fails, and what conditions affect the result.

If time allows, I would make the experiment closer to a real network environment by adding more background traffic or more resolver settings.
