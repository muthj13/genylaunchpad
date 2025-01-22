# hyperliquid-ai-nft-launchpad

A complex, end-to-end AI + NFT Launchpad that demonstrates:
- **AI Image Generation** (using OpenAI or other models).
- **Rust-based NFT contracts** on the fictional [Hyperliquid](https://hyperliquid.example.org/) blockchain.
- **Python** scripts to deploy and interact with these contracts.
- **Docker** for containerized development.
- **Streamlit** for a simplified UI.

## Table of Contents

1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Environment Variables](#environment-variables)
5. [Running Locally](#running-locally)
6. [Docker](#docker)
7. [Usage](#usage)
8. [Tests](#tests)
9. [Project Structure](#project-structure)
10. [License](#license)

---

## Overview

This repository shows a hypothetical scenario where:
- You generate NFT artwork using AI (DALLE-2, Stable Diffusion, etc.).
- You mint those NFTs on the **Hyperliquid** blockchain via a Rust contract.
- You manage the entire flow with Python scripts for deployment, interactions, and user-facing endpoints.

**Disclaimer**: Hyperliquid, Hypurrrscan, and HLQ tokens are *fictional*. This is for demonstration purposes.

## Requirements

- **Python 3.9+**
- **pip** or **conda** for dependency management
- **Rust** (1.60+) if you plan to build/modify the `hyperliquid_nft.rs`
- **Docker** (optional, if using the included docker-compose)
- An **OpenAI API Key** (or any other image-generation service)
- (Optional) A local or test Hyperliquid node/CLI

## Installation

1. **Clone this repository:**

   ```
   bash
   git clone https://github.com/muthj13/hyperliquid-ai-nft-launchpad.git
   cd hyperliquid-ai-nft-launchpad
   ```

2. **Install Python dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Copy .env.example to .env and fill in the required environment variables:**
 ```
 cp .env.example .env 
 ```





