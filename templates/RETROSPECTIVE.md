# Pair Retrospective: test_utils library

Copy this file to the ROOT of your shared repo as `RETROSPECTIVE.md`, fill in EVERY section
(replace each `[WRITE HERE]`), and commit it on your shared branch. Write it together:
one person types, the other dictates, then swap for the last two sections.

- Pair members: [Vennela Preethi, Shaqayeq Salimy]
- Repository / branch / PR link: [https://github.com/Venny12/Exercise4/tree/main]
- Date and total time spent: [Oct 16th, 3 hours]

## 1. Role-swap log

Fill one row per 30-minute block (add rows if you swapped more often).

| Block | Minutes | Driver | Navigator | What we built | Last commit hash (short) |
|---|---|---|---|---|---|
| 1 | 0-30 | [Vennela] | [Shaqayeq] | [startcode, .gitignore, first 3 M1 validators check] | [f8bb998] |
| 2 | 30-60 | [Shaqayeq] | [Vennela] | [6 validators pass] | [ee355e1] |
| 3 | 60-90 | [Vennela] | [Shaqayeq] | [4 generators check pass] | [a3463d2] |
| 4 | 90-120 | [Shaqayeq ] | [Vennela] | [all generators and timer pass] | [85776e9] |
| 5 | 120-150 | [Vennela, Shaqayeq] | [Vennela, Shaqayeq] | [updated demo_report.py, helpers.py, RETROSPECTIVE.md] | [] |

## 2. What went well in how we worked together?
[collaboration went well, we divided the tasks according to the file and requirement and waited for each other to finish up the respective parts and checked on each other, one of us spotted the the folder name isn't correct and we renamed the folder's name that was affecting the result while running the files] 

## 3. What was difficult?
- Technically: [We didn't have major technical issue, however sometimes we were running the file outside of the folder and it was giving the not found file error]
- As a team (communication, pace, disagreement, git hand-offs): [we were sitting side by side, communicating clearly, explaining for each other, we didn't have disagreement along the way of project, and git commands were working good for both sides.]

## 4. What did each of us learn from the other?
- [Vennela] learnedHERE from [Shaqayeq]: [we both together went over errors and discussed and solved it together]
- [Shaqayeq] learned from [Vennela]: [I learned precision and error handling]

## 5. Our code
- The function we are proudest of, and why: [wrapper and timers, because we didn't have the intial knowledge of it, then we learned and build it]
- The function that most needs improvement, and how: [make_test_case, we were getting none typeerror and we were able to improve and fix it]
- One bug we hit and how we found it (error message, what we tried, the fix): [File "C:\Users\chvpr\Documents\Exercise4\test_util\decorators.py", line 18, in wrapper
    result = func(*args, **kwargs), we fixed the error by implementing the correct function in generators.py]

## 6. Git collaboration
- Did every swap follow commit, push, pull? What went wrong when we skipped a step? [we followed every step]
- Did we get a merge conflict? How did we resolve it (or why not)? [we got one, two functions were duplicated and we deleted one]
- Output of `git shortlog -sne` (paste): [WRITE HERE]

## 7. Next time
- Two things we would do differently: [WRITE HERE]
- Self-rating, 1 (poor) to 5 (excellent): communication [WRITE HERE], keeping to the swap timer [WRITE HERE], understanding every line [WRITE HERE]

## 8. Final check
Paste the last lines of `python3 check_exercise.py` (the "x/y checks passed" line): [WRITE HERE]