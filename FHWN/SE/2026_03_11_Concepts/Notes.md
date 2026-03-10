> [!NOTE]
> Everything here is light worded. 
> Objective is easy understanding of main concepts, not being precise. 
> Dig deeper is something becomes relevant.


# Software Engineering -- The "Theory"

"Theory" because it is not theory, it is mostly a collection of best practices based on experience in the industry.

> [!Important]
> Don't be a Mandalorian and take anything in this semester as "THE way". 
> Everything here is condensed knowledge, **that works**, IF (huuuuuuge if) applied correctly,  as each situation, circumstance is different. 

## Recap from last class

### Software Engineering vs. Software Development vs. Programming vs. Coding

 - Overlapping concept without clear definitions.
 - Coding & Programming: translating **well specified** behavior to code, that the computer can execute.
 - Software Development: the whole process that also includes other necessary tasks, such as requirement specifications, tests, etc.
 - Software Engineering: the "educated way" of doing it based on best practices, so that the final product can (mostly) be shipped. Includes documentation rules, formal methods, etc.

### Why software development is hard?

 - Communication. Between:
   - developers
   - developer & management
   - us & client
 - Client requirements:
   - Often/May don't really know what they want.
   - Often/May tell something else than what they want.
   - What they want is incompatible with other things they want.
   - What they want changes. 
 - Complexity:
   - Much more components than in a house, car.
   - Interaction between components is much higher.
 - Technology stack:
   - Deprecation, security issues. 
   - Custom solution -> maintenance. Library -> dependency.
   - Not just components, tooling too.
 - Shipping fast vs. "Good code" 
   - Shortcuts => Technical debt
 - No agreement & hot debates / "semi-religious factions"
   - best language for the job
   - best framework for the job
   - best tooling for the job
   - best paradigma / coding style
   - even coding style

## "SE by the book"

> Those who do not know the past are condemned to repeat it.

### Linear models

#### Waterfall

```
Requirements -> Design -> Development -> Testing -> Deploying -> Maintenance 
```

 - Linear path. 
 - Good for "well defined" and regulated product, not ideal for most software.
 - Issues appear late, fixing costs a lot. 

#### V modell

```
Requirement Analysis               ↱ Acceptance Testing
 ↳ System Design                ↱ System testing
    ↳ Architecture Design    ↱ Integration testing
       ↳ Module Design    ↱ Unit testing
          ↳ Cooooooooooooding
```

 - Still linear.
 - But each step on the left has a set of corresponding tests as artifacts.
 - These tests are still executed AFTER coding, but this improves traceability and accountability
 - More about tests later, **Verification vs. Validation**!

#### W modell
 - Variant of V, where preliminary reviews of informal specifications are carried out before coding.
 - Design issues come to light earlier than in V. 
  
### Iterative & Iterative models /concepts / ideas

> [!important]
> **Iterative**: Do more smaller plan->do->test steps instead of 1 big cycle.
> **Incremental**: Intermediate versions are usable, testable.
 
 - Methodologies, concept & philosophies overlap.
 - Widespread for most software projects.

#### Spiral model 


1. Determine objectives
2. Identify and resolve risks
3. Development and test
4. Plan the next iteration
5. Repeat

Oldschool model from 1986, focuses on risks.

#### Agile

[The agile manifesto.](https://agilemanifesto.org/)
Bunch of very clever, and respected guys put down **guidelines**:

> **Individuals and interactions** over processes and tools <br />
> **Working software** over comprehensive documentation<br />
> **Customer collaboration** over contract negotiation<br />
> **Responding to change** over following a plan

 - NOT a methodology.
 - Become the "holy grail", "silver bullet",  "buzzword of managers"
 - Agile is like communism: "But REAL agile was never tried."
 - Often misunderstood, focus on theatrics instead of intentions

#### Scrum

 - IS a methodology, how agile ideas should/could be implemented.
 - Concrete list of roles, schedules, processes, etc. (=Theatrics)
 - MANY haters.
 - Almost everyone uses it. (something that has some resemblance to it.)

> **Uncle Bob**: “The Agile message has gotten so badly twisted and torqued and perverted […] Agile was a small idea for helping small teams do small things. It was not the overarching pattern of software development that was to dominate the world. It was just a way to get six or seven guys to be able to work well together.” <br /><br />
> **ThePrimeagen**: “So what made it fall apart then?” <br /><br />
> **Uncle Bob**: “One of us […] a Scrum advocate, Ken Schwaber , decided that he wanted to teach a course called the Certified Scrum Master course […] and the idea just took off. Everybody wanted to be a Certified Scrum Master; not one programmer wanted to be a Certified Scrum Master. All the project managers wanted it. They wanted that little checkbox on their resume; and the project managers flooded into the field. They flooded into Agile, they took over the message, they took over the conferences, they took over everything and they literally pushed the programmers out. And Agile became a project management idea […]. Where Agile breaks down is when people try to put an overarching envelope around the outside and then demand certain behaviors across the board […]”
>
> [source](https://overbring.com/blog/2024-05-01-uncle-bob-when-agile-fell-apart/?utm_source=chatgpt.com)


Having said that, it is good to know the most important points of scrum:

- **Team Size:** 3–9 people (self-organizing)

- **Roles:**  
  - **Product Owner:** decides what to do  
  - **Scrum Master:** ensures that the developers can do the thing
  - **Development Team:** does the thing

- **Artifacts:**  
  - **Product Backlog:** Ordered list of things to do (features, requirements, bugs)
  - **Sprint Backlog:** Subset chosen on Sprint planning 
  - **Increment:** The incremental version of the product

- **Timeboxes / Schedule:**  
  - **Sprint:** 1–4 weeks, mostly 2 
  - **Daily Scrum / Standup:** ~15 min, progress & blockers  
  - **Sprint Planning:** sprint goals, pick backlog items  
  - **Sprint Review:** Demo increment, feedback  
  - **Sprint Retrospective:** Inspect & adapt process  

- **Other Concepts / Buzzwords:**  
  - **Definition of Done (DoD):** Criteria for completed work  
  - **Velocity:** Measure of team output per sprint  
  - **Burndown Chart:** Tracks remaining work in sprint  
  - **Impediments / Blockers:** Anything slowing the team  
  - **Complexity / Estimation:** Story points, Planning Poker, T-shirt sizing  

- **Key Principles:**  
  - Inspect and adapt every sprint  
  - Deliver **working software frequently**  
  - Team is self-organizing, accountable, and empowered  

But often:

- **Daily Standup → Status Meeting:** Becomes reporting to the manager instead of team coordination.  
- **Sprint Planning → Overload:** Teams pick too much, ignore capacity, velocity drops.  
- **Backlog → Endless Grooming:** Priorities unclear, refinement never finishes.  
- **Sprint Review → Demo Theater:** Focus on presentation, not feedback or learning.  
- **Retrospective → Talking Shop:** Repetitive, superficial, no real changes implemented.  
- **Velocity → Pressure Tool:** Management misuses it to push teams, killing morale.  
- **Scrum Roles → Role Confusion:** Scrum Master becomes project manager; Product Owner gets ignored.  
- **Ceremonies → Rituals:** Rituals followed blindly; Agile principles are lost.  

#### Kanban

A way to organize tasks: 
 - there is a board
 - there are lists/columns on the board (original didn't have this)
 - tasks/cards can be moved between columns

The "typical" columns:  backlog/planned, in progress, testing/review, done.

Mostly for continuous flow, helps to limit work in progress.

"Kanban style" boards sometimes used with columns for:
 - sprints
 - people
 - priorities
 - whatever is useful


#### XP - Extreme programming

Emphasizes new deliveries in VERY short cycles, constant feedback. 
Goes hand in hand with CI/CD techniques.

### Bunch of abbreviations

#### TDD - Test Driven Development
Write the tests first.

#### DRY - Don't repeat yourself / WET - Write Everything Twice
Avoid repeated code (loops, functions, inheritance, delegation, etc.)
But... avoid generalization too early.

#### SOLID
**S**ingle responsibility principle - one thing should only do one thing

(Leave the rest for now until you learn OO)
**O**pen/Closed principle 
**L**iskov substitution principle  
**I**nterface segregation principle  
**D**ependency inversion principle  

#### YAGNI - You Ain't Gonna Need It
Don't do things in advance that you are not absolutely sure you will need. 
(Unnecessary abstractions, speculative generalization with OO are prime examples.)

#### Other common abbreviations / principles

#### KISS - Keep It Simple, Stupid
Do a few things well, rather than doing 100 things, mediocre.

#### PoC — Proof of Concept**  
A small prototype to verify that an idea works.

#### MVP — Minimum Viable Product**  
The smallest useful version of a product.

### Testing... 
Many different types of tests, with again, overlapping concepts...

#### Unit Test
Isolated test of a function/class.
Usually automatically run in CI pipeline.

#### Integration Test
Tests whether these small things work together.
Can still run automated. 

#### System Test
Tests the entire system in a real environment.
Verification = did we do what we planned to do?

#### Acceptance Test
Tests with real client needs.
Validation = what we planned and did is really what the client needs?

#### Regression Test
Testing old things, if they still work.

#### Performance Test
Tests if the thing works under pressure. 
Loadtest, stresstest, scalability test etc.

#### Security Test
Check for vulnerabilities, possible attacks.

#### End-to-End (E2E) Test**  
Tests whole workflows, that may involve external systems/services.