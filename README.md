# Arbitrary Scale Upsampling with Hybrid Attention and Fourier Analysis

This repository holds the content for the class project we carried out for EECS 504 @ University of Michigan, Ann Arbor.

It includes modifications to the LTE model, by incorporating ideas from HAT on top of the SwinIR that is used as the encoder block.

Video: https://www.youtube.com/watch?v=BBHTCdUwZ0E
Paper: Included in files

Contribution: 
- Literature review to identify components that would go well together. 
- Incorporating the modifications on SwinIR by HAT through adding CAB, OCAB, and various other operations such as shifted window masking (Encoder Section).
- Reducing the size of the model and experimenting on different comprimises (depths, num_heads, length of the list).
- Hyper-parameter changes and tuning on: Learning rate, LR scheduler, batch-size, repeat number of training dataset, number of epochs.
- Reducing the number of training images to 600 and altering the dataloader (reduce parameters to fit memory constraints).
- Loss function analysis (using our own small script) over different training regiments to understand and optimize the model.
- Final PSNR performance comparison between the baseline (Small LTE-SwinIR), and our model (Small LTE-HAT).
- Removing unnecessary components and combining everyting (except the datasets folder) under a single file (combined.ipynb) for ease of use and demonstration of understanding.

## Acknowledgements
This code is built on LTE: 
[**Local Texture Estimator for Implicit Representation Function**](https://ipl.dgist.ac.kr/LTE_cvpr.pdf) (CVPR 2022)

It also incorporates ideas and pieces of code from HAT:
[[Paper Link]](https://arxiv.org/abs/2205.04437) 

We thank the authors for sharing their codes.
