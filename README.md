# BankAssistant_ML
BankAssistant_ML
A domain-specific retail banking support assistant fine-tuned using TinyLlama (1.1B-Chat) with LoRA (PEFT).

The assistant answers customer questions strictly based on BestVerie Bank policy (savings tiers, transfer fees, ATM rules, mobile money cash-out).

 Project Overview

This project demonstrates:

Creation of a synthetic policy-based dataset (2000+ examples)

Supervised fine-tuning of a pre-trained LLM

Parameter-Efficient Fine-Tuning (LoRA)

Evaluation using ROUGE metrics

Deployment via Gradio + Hugging Face Spaces

Domain: Retail Banking / Finance

 Base Model

TinyLlama/TinyLlama-1.1B-Chat-v1.0

Fine-tuned using PEFT LoRA

Trained on Google Colab (T4 GPU)

 Dataset

The dataset was generated from structured BestVerie Bank policy rules:

Savings interest tiers (boundary-focused)

External transfer fees (percentage + min/max cap)

ATM withdrawal rules (free count + limits)

Mobile money cash-out fee cap

Out-of-domain refusal examples

Format: JSONL (chat-style instruction-response)

 Fine-Tuning Configuration

Learning Rate: 1e-4 (best run)

LoRA Rank: 8

Max Steps: 600

Batch Size: 2 (with gradient accumulation)

Optimizer: AdamW

Quantization: 4-bit (QLoRA)

Evaluation: ROUGE

 Results

Fine-tuned model outperforms base model in:

Policy consistency

Tier boundary handling

Fee cap enforcement

Out-of-domain refusal

ROUGE scores (validation):

ROUGE-1: ~0.83

ROUGE-2: ~0.81

ROUGE-L: ~0.83

 Deployment
 Hugging Face Model:
https://huggingface.co/Best-Verie/bestverie-bank-lora

 Live Demo (HF Spaces):
https://huggingface.co/spaces/Best-Verie/bestverie-bank-assistant

The deployed app loads:

Base model from Hugging Face

LoRA adapter from this repository

Demo Video
https://share.vidyard.com/watch/m6kS7CBs8ZyzLcw186tyJF

