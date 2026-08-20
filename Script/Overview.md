# Overview 180s

Thank you. I would like to explain my proposed research.

In my undergraduate thesis, I studied TLS encrypted traffic classification. Since TLS hides payload contents, I focused on packet-length sequences. But I found that these sequences can be changed by TCP-level behavior, such as retransmission, sequence shift, and packet merging. So I designed TAC-Seq, a contrastive learning framework to learn more robust representations from perturbed packet-length sequences.

At NAIST, I would like to continue this direction and study DNS over HTTPS, or DoH. DoH improves privacy by sending DNS queries over HTTPS, but it also makes network monitoring harder, because DoH traffic can look similar to ordinary HTTPS traffic.

The difficult case I want to focus on is short-lived DoH traffic to private resolvers. If a DoH flow is very short, a classifier can see only a few encrypted packets. Also, if the resolver is private and unseen during training, an IP address list is not enough.

My idea is to change the observation unit. Instead of looking only at one isolated TLS flow, I will look at a short host-level time window around the candidate flow. The method will use only metadata, such as packet size, direction, timing, and flow counts, without inspecting payloads or relying on resolver identity.

I will compare a single-flow baseline with a host-level model, using data split by resolver and collection session. I want to evaluate whether host-level context improves detection for unseen private resolvers, and also measure false positives, latency, and processing cost.

The goal is to clarify when host-level context helps, when it fails, and whether this approach is practical for encrypted traffic monitoring.

---

# Overview 60s

Thank you. My proposed research is about detecting short-lived DNS-over-HTTPS traffic.

DoH protects DNS queries by sending them over HTTPS, but it also makes network monitoring harder, because it can look like ordinary HTTPS traffic. The difficult case is short DoH traffic to private resolvers that are not seen during training.

My idea is to change the observation unit. Instead of judging only one TLS flow, I will also use a short host-level time window around it. The method will use only metadata, such as packet size, direction et cetera, without inspecting payloads or using resolver identity.

I will compare this with a single-flow baseline and evaluate detection performance and practical cost.

---

# Overview 30s/interrupted

Okay, I'll summarize the core idea briefly.

My research is about detecting short-lived DoH traffic to private resolvers.

A single encrypted flow may have too little evidence, so I use a short host-level time window around the candidate flow.

I use only metadata, such as size, direction et cetera, and compare it with a single-flow baseline.

---

# Overview 10s

The core idea is to test whether host-level temporal context can help detect short-lived DoH traffic when a single encrypted flow has too little information.