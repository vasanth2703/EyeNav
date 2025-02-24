# EyeNav

This project aims to empower individuals with motor disabilities to interact with digital devices hands-free using an AI-powered eye-tracking system. Traditional input methods can be challenging or impossible for some, and existing hardware solutions for eye-tracking are often expensive. This project leverages the open-source IBM Granite Vision Transformer and a standard webcam to provide an affordable and accessible alternative.

## Problem Statement

People with motor disabilities often struggle to use digital devices. Voice commands can be slow and inaccurate, while dedicated eye-tracking hardware can be prohibitively expensive. This project seeks to address this challenge by creating a software-based eye-tracking solution.

## Solution

This project implements an AI-powered eye-tracking cursor that enables hands-free control of the browser using only eye movements and blinks. It uses the IBM Granite Vision Transformer to analyse webcam video and translate eye movements into cursor control.

## Key Features

* **Gaze-Based Cursor Movement:** Move the on-screen cursor by simply looking around.
* **Blink twice to Click:** Perform mouse clicks with blinks: a short blink for a left-click and a longer blink for a right-click.
* **Gaze Scrolling:** Scroll pages and reels by looking up or down.
* **Real-Time AI Adaptation:** The model learns and adapts to individual user-specific gaze patterns over time for improved accuracy.
* **No Extra Hardware Needed:** Works with a standard webcam, making it accessible and affordable.

## Development

**Clone the repository:**

```bash
git clone https://github.com/believemanasseh/EyeNav.git
cd EyeNav
```

### Chrome Extension

* Download the source code from the repository.
* Go to chrome://extensions/ in your Chrome browser.
* Enable "Developer mode" in the top right corner.
* Click "Load unpacked" and select the downloaded extension folder.

### FastAPI Server

**Navigate to server directory:**

```bash
cd server
```

**Install dependencies:**

```bash
poetry install
```

**Start development server:**

```bash
fastapi dev src/app.py
```
