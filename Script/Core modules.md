# Research significance

The main significance is to test whether the observation unit should be changed for short-lived encrypted traffic detection.

This is important because the input unit decides what kind of evidence a detector can use. If the unit is only one short flow, useful behavior around that flow may be ignored.

The study can show whether changing the input unit is a meaningful research direction before designing a more complex model.

If it works, it shows a practical direction for encrypted traffic monitoring. If it does not work, it still clarifies the limitation of metadata-based DoH detection.

---

The significance is that my proposal tests a different observation unit.

It asks whether one isolated flow is enough for short-lived DoH detection, or whether the input unit itself should be reconsidered.

This can clarify the practical limit of metadata-based encrypted traffic monitoring.

---

# Existing methods defect

Existing methods are useful, but they are not enough for the difficult case I focus on.

Many DoH detection methods work well when the resolver is known, the flow is long enough, or the training and test conditions are similar.

But in my target case, the DoH flow is short and the resolver is private and unseen during training. An IP address list cannot detect such a resolver. Also, a single-flow classifier may have too little information for a stable decision.

So the key gap is reliability under a stricter and more realistic test setting.

---

Existing methods are not enough for my target case because they often depend on known resolvers or enough information inside one flow.

For short-lived DoH traffic to unseen private resolvers, an IP address list does not work, and a single flow may be too short.

So the key gap is reliability under a stricter test setting.

---

# Proposed method

My proposed method is to change the observation unit from a single TLS flow to a host-level time window.

First, I take a candidate encrypted flow that may be DoH. I then look at nearby encrypted traffic from the same host within a short time window.

The method uses traffic metadata, such as packet size, direction, timing, flow counts, and repeated short-flow patterns. It does not read the communication content or simply identify a known resolver.

Then I build a host-level model using these context features, and compare it with a single-flow baseline under the same metadata restriction.

The purpose is to see whether surrounding host behavior improves the decision when the candidate DoH flow itself is too short.

---

My method is to use a host-level time window around a candidate encrypted flow.

I use nearby traffic from the same host, such as timing gaps and repeated short-flow patterns, while keeping the input limited to metadata.

Then I compare this host-level model with a single-flow baseline.

---

# Dataset

I plan to build a controlled testbed for data collection.

In this testbed, I will generate ordinary HTTPS traffic, benign DoH traffic to public resolvers, and low-volume DoH traffic to private resolvers. This is important because I need clear labels and control over the resolver type and query pattern.

I will repeat the collection in separate sessions and under different network conditions. Then I will split the data by resolver and collection session, so the test data is not almost the same as the training data.

This dataset is not meant to cover all Internet traffic at the first stage. It is a controlled setting to evaluate whether the proposed idea works in the difficult case.

---

I will collect data using a controlled testbed.

The data will include ordinary HTTPS traffic, DoH traffic to public resolvers, and short low-volume DoH traffic to private resolvers.

I will repeat the collection in different sessions and split the data by resolver and session, so that the evaluation is not too optimistic.

---

# Metrics/Evaluation

I will evaluate the method by comparing three settings.

The first one is an address-list detector, which is a simple reference for known resolvers. The second one is a single-flow metadata classifier. The third one is my host-level model using time-window features.

The main target is short-lived DoH traffic to private resolvers that are not seen during training. I want to see whether the host-level model improves detection in this setting.

At the same time, I will measure false positives on ordinary HTTPS traffic, F1 score, detection latency, memory use, and processing time.

I will also change the window size and network conditions, and remove feature groups one by one to see which context features actually contribute.

---

I will compare an address-list detector, a single-flow baseline, and my host-level model.

The main test is whether the host-level model improves detection for short-lived DoH traffic to unseen private resolvers.

I will also measure false positives, F1 score, latency, memory use, and processing time.

---

# Related work basis/Reference

My proposal is based on three lines of related work.

First, my undergraduate work was related to robust TLS encrypted traffic classification. Rosetta is important here because it uses TCP-aware traffic augmentation to improve robustness under network variation.

Second, for DoH detection, I refer to a comparative analysis of DoH detectors. It shows that some detectors depend on known resolvers, traffic burstiness, or stable training conditions, and that short DoH flows to private resolvers are still difficult.

Third, I refer to host-level aggregation in network security. Katsura et al. showed that host-level aggregation can be useful for efficient IDS in IoT networks.

My proposal connects these ideas and tests whether host-level context can help in short-lived encrypted DNS detection.

---

There are three main related works.

Rosetta is related to my undergraduate work because it studies robust TLS traffic classification with TCP-aware augmentation.

The DoH detector comparison motivates my target problem, especially short flows and private resolvers.

Host-level aggregation work motivates the idea of using information around the same monitored host.

---

# Connection

My undergraduate research gives me the technical background for this proposal.

In my thesis, I worked with TLS traffic, packet-length sequences, and network perturbations. Through that work, I learned how encrypted traffic can still be analyzed from external traffic patterns, and also why those patterns can be unstable.

This experience is useful for the DoH project because DoH is also encrypted traffic, and I cannot rely on the content of communication.

The difference is that my past work focused on making a single flow representation more robust. In the new project, I focus on cases where one short flow may not be enough, so I extend the observation to a host-level time window.

---

My undergraduate research gives me the technical background for this proposal.

I studied TLS traffic classification using packet-length sequences and considered how network behavior can change those sequences.

This is useful for DoH detection because DoH is also encrypted traffic.

The main difference is that I move from improving a single-flow representation to using a host-level time window.

---

# Lab fitness

I chose this lab because my proposal is closely related to practical network systems and network security.

My research topic is about encrypted traffic monitoring. It requires understanding real network behavior, collecting traffic data, designing evaluation settings, and measuring practical costs such as latency and processing time.

I think this matches the Internet Architecture and Systems Laboratory because the lab has a strong focus on networked systems, measurement, and practical evaluation.

Also, my proposal is experimental. I want to build a reproducible testbed, compare baselines, and clarify the limitation of the method. I believe this kind of research fits the lab environment.

---

I chose this lab because my topic is related to practical network systems and network security.

My proposal needs traffic data collection, realistic evaluation, and analysis of latency and processing cost.

I think this fits the Internet Architecture and Systems Laboratory because the project is close to network measurement and practical system evaluation.

---

# Pre-application change

In the pre-application, my topic was robust QUIC traffic classification under congestion.

It was closely connected to my undergraduate thesis, because it tried to extend my TLS traffic classification work to QUIC. But after reconsidering it, I felt that the plan was too smooth as an extension of my past work.

The research question was not new enough, and the feasibility was also unclear because QUIC-specific augmentation would require many protocol assumptions and controlled traffic generation.

I also felt that a topic closer to practical encrypted traffic monitoring would fit the laboratory better.

So I refined the plan to short-lived DoH detection using host-level context.

---

My pre-application topic was robust QUIC traffic classification under congestion.

It was connected to my undergraduate thesis, but later I felt it was too close to a direct extension of my past work.

The novelty and feasibility were not clear enough, and I wanted a topic closer to practical encrypted traffic monitoring.

So I refined the plan to short-lived DoH detection using host-level context.

---

# Limitation/Failure

The main limitation is that host-level context may not always provide useful information.

If a host has many unrelated HTTPS connections in the same time window, the context can become noisy. Also, if the DoH activity is very sparse, the window may still not contain enough signal.

I will handle this by testing multiple window sizes, query frequencies, and network conditions. I will also report false positives and latency together with detection performance.

If the improvement is limited, the result is still useful. It can show where metadata-based DoH detection reaches its practical boundary, and under what conditions this approach is not enough.

---

The main limitation is that host-level context can be noisy.

A host may have many unrelated HTTPS connections, and very sparse DoH activity may still be hard to detect.

I will test different window sizes and report false positives and latency.

If the improvement is small, it still shows the practical boundary of metadata-based DoH detection.
