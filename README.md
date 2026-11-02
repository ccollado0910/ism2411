# ISM2411 — Python for Business

**Name:** Christian Collado

**Semester:** Fall 2026

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week07/` — Functions: calculate_tax, apply_discount, final_price
- Module 8 — Git: set up this repo with a `.gitignore`, a README, and my first GitHub commits

## How to Run

Each script is standalone. Open a terminal in this folder and run:
```
python3 week07/functions.py
```

## Reflection

**1. What does my commit history say about how I work?**

```
da88023 add README with module listing and run instructions
9edb1a4 add module 7 functions: calculate_tax, apply_discount, final_price
ad88f13 add .gitignore for Python and OS files
1d22ba3 Initial commit
```

If I were hiring someone and saw this history, I would think they work in small, organized steps. Each commit does one thing, and the message says exactly what changed, so you can tell what happened without opening any files. The order also makes sense: the .gitignore came first so junk files never got tracked, then the code, then the documentation. It is a short history so far, but it shows someone who plans before they start adding files.

**2. How does Git change the way I edit a working script?**

Before this module, when I had a working script I was nervous to change it, so in Module 7 I copied my functions into every exercise section instead of building on the same code. With Git, I can commit the working version first and then make changes, because if something breaks I can always go back to the last commit. Now I would commit every time something works, and make smaller changes in between.

**3. What would I add to my .gitignore?**

I would add `Screenshot*.png`. I take screenshots of my lab output to submit on Canvas, and on my Mac they can end up in the same folder I am working in. They are only for my own submissions, they are not code, and they would make the repo bigger and more cluttered for anyone else looking at it.
