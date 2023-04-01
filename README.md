# Secure Code Game

_A GitHub Security Lab initiative, providing an in-repo learning experience, where learners secure intentionally vulnerable code._

Source: https://github.com/skills/secure-code-game

<details id=1>
<summary><h2>Level 1: Black Friday</h2></summary>

_Welcome to "Secure Code Game"! :wave:_

### 📝 Storyline
A few days before the massive shopping event Black Friday, an electronics shop without an online presence rushed to create a website to reach a broader customer base. As a result, they spent all their budget on development without investing in security. Do you have what it takes to fix the bug and progress to Level 2?

### :keyboard: What's in the repo?
For each level, you will find the same file structure:
- `code` includes the vulnerable code to be reviewed
- `hack` exploits the vulnerabilities in `code`. Running `hack.py` will fail initially, your goal is to get this file to pass.
- `hint` offers a hint if you get stuck.
- `solution` provides one working solution. There are several possible solutions.
- `tests` contains the unit tests that should still pass after you have implemented your fix.

### 🚦 Time to start!
1. Review the code in `code.py`. Can you spot the bug?
1. Try to fix the bug. Ensure that unit tests are still passing.
1. You successfully completed the level when both `hack.py` and `tests.py` pass 🟢.
1. If you get stuck, read the hint in the `hint.js` file.
1. Compare your solution with `solution.py`.

</details>


<details id=2>
<summary><h2>Level 2: Matrix</h2></summary>

_You have completed Level 1: Black Friday! Welcome to Level 2: Matrix. :tada:_

### 📝 Storyline
At the time "The Matrix" was first released in 1999, programming was different. In the movie, a computer programmer named Thomas "Neo" Anderson leads the fight in an underground war against powerful computers who have constructed his entire reality with a system called the Matrix. Do you have what it takes to win that war and progress to Level 3?

### :keyboard: What's in the repo?
For each level, you will find the same file structure:
- `code` includes the vulnerable code to be reviewed
- `hack` exploits the vulnerabilities in `code`. Running `hack.py` will fail initially, your goal is to get this file to pass.
- `hint` offers a hint if you get stuck.
- `solution` provides one working solution. There are several possible solutions.
- `tests` contains the unit tests that should still pass after you have implemented your fix.

### 🚦 Time to start!
1. Keep working inside the same environment as in Level 1
1. If you skipped Level 1, go back and follow the 🚦 **Time to start** guide
1. Review the code in `code.h`. Can you spot the bug?
1. Try to fix the bug. Ensure that unit tests are still passing.
1. The level is completed successfully when both `hack.c` and `tests.c` pass. 🟢
1. If you get stuck, read the hint in the `hint.txt` file.
1. Compare your solution with `solution.c`.

</details>


<details id=3>
<summary><h2>Level 3: Social Network</h2></summary>

_Nice work finishing Level 2: Matrix! It's now time for Level 3: Social Network. :sparkles:_

### 📝 Storyline
The following fictitious story takes place in the mid-2030s. Authorities worldwide have become more digitized. Various governments are adapting social network technology to fight crime. The goal is to establish local communities that foster collaboration by supporting citizens with government-related questions. Other features include profile pictures, hashtags, real-time support in comments, and public tip sharing. Do you have what it takes to secure the social network and progress to Level 4?

### :keyboard: Setup instructions
- For Levels 3-5, we encourage you to enable code scanning with CodeQL. For more information about CodeQL, see "[About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/)." For instructions setting up code scanning, see "[Setting up code scanning using starter workflows](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/setting-up-code-scanning-for-a-repository#setting-up-code-scanning-using-starter-workflows)."

### :keyboard: What's in the repo?
For each level, you will find the same file structure:
- `code` includes the vulnerable code to be reviewed
- `hack` exploits the vulnerabilities in `code`. Running `hack.py` will fail initially, your goal is to get this file to pass.
- `hint` offers a hint if you get stuck.
- `solution` provides one working solution. There are several possible solutions.
- `tests` contains the unit tests that should still pass after you have implemented your fix.

### 🚦 Time to start!
1. The codebase generates several code scanning alerts. Your goal is to resolve these alerts for each level.
1. Review the code in `code.py`. Can you spot the bugs?
1. If you get stuck, read the code scanning alert.
1. Try to fix the bug. Make your changes and open a pull request to `main` or push your fix to a branch.
1. Check the tests and the code scanning results to confirm the alert for this level has now disappeared.

</details>


<details id=4>
<summary><h2>Level 4: Data Bank</h2></summary>

_Nicely done! Level 3: Social Network is complete. It's time for Level 4: Database. :partying_face:_

### 📝 Storyline
Databases are essential for our applications. However, malicious actors only need one entry point to exploit a database, so defenders must continuously protect all entry points. Can you secure them all?

### :keyboard: What's in the repo?
For each level, you will find the same file structure:
- `code` includes the vulnerable code to be reviewed
- `hack` exploits the vulnerabilities in `code`. Running `hack.py` will fail initially, your goal is to get this file to pass.
- `hint` offers a hint if you get stuck.
- `solution` provides one working solution. There are several possible solutions.
- `tests` contains the unit tests that should still pass after you have implemented your fix.

### :keyboard: Setup instructions
For Levels 3-5, we encourage you to enable code scanning with CodeQL. For more information about CodeQL, see "[About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/)." For instructions setting up code scanning, see "[Setting up code scanning using starter workflows](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/setting-up-code-scanning-for-a-repository#setting-up-code-scanning-using-starter-workflows)."

### 🚦 Time to start!
1. The codebase generates several code scanning alerts. Your goal is to resolve these alerts for each level.
1. Review the code in `code.py`. Can you spot the bugs?
1. If you get stuck, read the code scanning alert.
1. Try to fix the bug. Make your changes and open a pull request to `main` or push your fix to a branch.
1. Check the tests and the code scanning results to confirm the alert for this level has now disappeared.

</details>


<details id=5>
<summary><h2>Level 5: Locanda</h2></summary>

_Almost there! One level to go! :heart:_

### 📝 Storyline
It's a common myth that passwords should be complex. In reality, it's more important that passwords are long. Some people choose phrases as their passwords. Users should avoid common expressions from movies, books, or songs to safeguard against dictionary attacks. Your password may be strong, but for this exercise, a website you have registered with has made a fatal but quite common mistake. Can you spot and fix the bug? Good luck!

### :keyboard: What's in the repo?
For each level, you will find the same file structure:
- `code` includes the vulnerable code to be reviewed
- `hack` exploits the vulnerabilities in `code`. Running `hack.py` will fail initially, your goal is to get this file to pass.
- `hint` offers a hint if you get stuck.
- `solution` provides one working solution. There are several possible solutions.
- `tests` contains the unit tests that should still pass after you have implemented your fix.

### :keyboard: Setup instructions
For Levels 3-5, we encourage you to enable code scanning with CodeQL. For more information about CodeQL, see "[About CodeQL](https://codeql.github.com/docs/codeql-overview/about-codeql/)." For instructions setting up code scanning, see "[Setting up code scanning using starter workflows](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/setting-up-code-scanning-for-a-repository#setting-up-code-scanning-using-starter-workflows)."

### 🚦 Time to start!
1. The codebase generates several code scanning alerts. Your goal is to resolve these alerts for each level.
1. Review the code in `code.py`. Can you spot the bugs?
1. If you get stuck, read the code scanning alert.
1. Try to fix the bug. Make your changes and open a pull request to `main` or push your fix to a branch.
1. Check the tests and the code scanning results to confirm the alert for this level has now disappeared.

</details>

---

&copy; 2023 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
