# Reading Notes: Locatello et al. (ICML 2019)
## Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations

## Objective

The paper studies unsupervised disentangled representation learning and shows that increasing disentanglement does not always improve downstream tasks. The authors argue that inductive biases and some form of supervision are needed to learn meaningful disentangled representations.

---

## Method

The authors tested different unsupervised disentanglement methods by training thousands of models with different hyperparameters and random seeds.

They analyzed whether these methods can consistently learn disentangled representations and whether better disentanglement improves performance on downstream tasks.

---

## Key Assumption I'd Challenge

One assumption I would challenge is that the datasets used in the experiments may not fully represent real-world data complexity.

---

## One Surprising Result

The surprising result is that higher disentanglement does not always lead to better performance on downstream tasks.

The paper also shows that methods can achieve what their loss functions encourage, but this does not guarantee that they learn the true hidden factors of the data.

---

## One Open Question

My question is:

If unsupervised learning needs inductive biases or supervision, how can we design better methods that learn meaningful representations with less human labeling?

---

## Understanding Summary

### Main Claim

The paper claims that unsupervised methods cannot reliably learn disentangled representations without inductive biases or some form of supervision.

### What is a Disentangled Representation?

A disentangled representation means separating the important features of data into different parts of the representation instead of mixing all features together.

### Why is Unsupervised Disentanglement Difficult?

Because unsupervised data does not have labels, the model cannot know which features should be separated or which representation is the correct one.

### Figure Reviewed

Figure 3 (Left) shows FactorVAE scores on the Cars3D dataset. The scores overlap heavily because the results change due to different hyperparameters and random seeds.

### Personal Reflection

This paper helped me understand that improving a metric does not always mean solving the actual problem. Research also requires questioning whether the evaluation methods truly measure what we want to achieve.
