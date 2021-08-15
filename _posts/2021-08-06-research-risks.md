---
title: Managing risks in research
layout: post
---

Research is uncertain.
It's not clear *what* problems you will hit.
It's not clear *how many* problems you will hit.
It's not clear *how long* success will take
or what success will *look like*
or whether you will even *succeed*.
When we talk about research, we often focus on
the ideas, the sudden insight, the stroke of genius,
standing on the shoulders of giants, etc.
We sometimes talk about uncertainty and persistence.
But we very rarely talk about risk and, most importantly,
how to manage it.

And it's not just that risk is an unfortunate side-effect
of tackling hard, unsolved problems; *dealing with risk is our job*.
In 15+ years of industrial research, I've come to believe that

> An essential part of the job of an industrial researcher is
> to keep unacceptable levels/types of risks away from production engineering teams
> so that they can execute as efficiently as possible
> without too many false steps.

Managing risk is also a key part of a company's research strategy:
tracking long-term trends for risks (and opportunities)
for the business; maintaining a balance of high-risk and low-risk projects;
balancing short-term projects with the more risky long-term projects;
etc.
But, for this post, I'll focus on managing risks in individual projects.


### I have a little list

The first part to managing the risks in a research project
is to make a list of all the risks you can think of.

- There's usually a bunch of technical questions: a list of challenges
  you need to solve. These are usually fairly obvious because you
  already know that the existing approach doesn't work.

- Then there's questions about how well your solution will work:
  Will it be 80% effective? 90%? 99%?
  Will it be fast enough? small enough? etc.

- But then we get into the really big risks:
  Are we solving the right problem?
  Did we understand the issue?
  Did the problem really need to be solved?
  As we navigated the twists and turns of finding a solution,
  did we lose track of the problem?
  Has the problem changed during the course of the project?

- Another important risk to consider is whether you need
  to do anything at all? Maybe somebody has already solved
  the problem. In industrial research, this is great news because
  it means that you can solve the problem quickly
  and move onto the next problem. (There is no shortage of hard
  problems in industry.)
  In practice though, this rarely happens because the problems
  we hit in industry always have unsolved corners to them and,
  until you have solved all the problems, it is not ready
  for production engineering teams to implement.
  (Some of my favourite research papers are about all the
  surprising issues that are encountered in solving 
  a problem.)

For [my current project][RVT website], I have a
[list of around 50 risks that I'm worried about](https://project-oak.github.io/rust-verification-tools/2021/08/15/rvt-risks.html).

Once you have a list of risks, you need to estimate the size of each risk:
how much impact it could have and how uncertain you are about
whether it is a real problem.
This is basically impossible to do at the start of a project:
you just don't understand enough to list all the risks and rank
them accurately.
This is an iterative process so just start with a coarse-grained
ranking system like high, medium and low and do the best you can.



### Managing your risk budget

Now the hard part... try to kill your project.[^student-projects]
Pick the largest risk and try to show that it is so big
that your project is bound to fail.
Be creative. Try really hard to kill it.
This is a bit brutal but it's a lot better to find a problem yourself
early in a project than to have somebody else find the problem later.

[^student-projects]:
    From comments on Twitter, I realize that I did not make it clear that
    the approach in this article is mostly for multiperson, multiyear
    projects. For a student project, the PhD supervisor would be thinking
    of some of these issues before suggesting the project to avoid
    the student discovering the fatal flaws for themselves some distance
    into the project.

*[[Laurence Tratt](https://tratt.net/laurie/)
(King's College London)
[wrote about](https://tratt.net/laurie/blog/entries/stick_or_twist.html)
how he has applied a similar approach at
several points in his career.]*


> If it's your job to eat a frog, it's best to do it first thing in the morning.
> And If it's your job to eat two frogs, it's best to eat the biggest one first.
>
> --- Mark Twain

Keep going with any risks that you think could potentially doom your project to failure.

Along the way, you will probably find that you need to change your plans
to avoid some risk.
For example, if you become uncertain that you can automate 100% of a problem: you might change your
plan to allow some small amount of human assistance.
And then you would amend the risk to include questions about whether you are able
to automate enough of the problem to be useful and whether your users can realistically solve
the part that you leave for them.

And, as you work the problem, you will probably realize that you misunderstood
the problem, that you had left out some risks, etc.
This is good: you are building a clearer understanding of the problem;
building a better project plan;
and saving production teams from risk.

As you work on each risk, your goal is not to reduce that risk
to zero. Your goal is just to reduce the size of the biggest risk
by solving part of the problem and/or making your assessment of the risk more accurate.
Especially at the start of a project, you have lots of risks to assess
so it is best to take a brief look at all the big ones early
and revisit them later.
Another way of looking at this is that, in the early stages, you will explore
the topic in a breadth-first manner where you understand the topic and the risks;
and, in later stages, you will shift more to a depth-first approach where you
work more efficiently by diving deep and maintaining focus on each aspect for longer.

You can only manage so much of this per month:
it is psychologically hard to kill your own ideas;
you need to build part of the system before you
have enough to attack;
and you have to make forward progress.
So, give yourself a risk budget: a certain number of
days per month that you will spend trying to reduce risk.

On my [current project][RVT website], I manage the risk budget by doing "risk sprints"
that are limited to a maximum of one week.
In that week, I try to move as quickly as possible.
I take good notes about what I do and what I learn
but I allow myself to ignore every software engineering
rule in the book.
My job during that week is just to learn as much as I can
about the risk so that I can update the risk assessment.
Along the way though, I am hoping to learn something useful
to move the project forward.
So, at the end of the week, 
I switch to software engineering mode: turning any useful
ideas into decent quality code or writing design documents for later.
And, since the project is all open source, sometimes I write blog post
about 
things like [profiling](https://project-oak.github.io/rust-verification-tools/2021/03/12/profiling-rust.html)
or 
fixing [bottlenecks](https://project-oak.github.io/rust-verification-tools/2021/05/19/fixing-bottlenecks.html)
found by profiling.

And every few months, I go back to the list of risks and
update my sense of which risks matter most and think about
the risks I should work on over the next few months,
whether there are any logical order/dependencies between them
and what I need to build to support that.

### Summary

- An essential function of industrial research is to keep unacceptable
  levels and types of risk away from production engineering teams.

- We can manage that risk by

  - making a very long list of all the risks we can think of

  - guessing the size of each risk

  - tackling the biggest risks first

  - updating the list of risks and our guesses about size
    throughout the life of the project.

- With luck, the number of high-rated risks will go down over time.
  If not, you should seriously consider killing your project.

In closing...
the idea here is not to fixate on risk: running around shouting
that the sky is falling down.
Instead, it is like the [Getting Things Done](https://gettingthingsdone.com/)
productivity system:
by writing down all the risks, you can stop worrying about them because
you know that you have that taken care of and you have a plan to handle them.
Which lets you focus on other aspects of the project.
The tweak that I am adding is the idea that you can use the
list of risks to help decide what part of the problem to work on next.


------------


[RVT website]: https://project-oak.github.io/rust-verification-tools/
