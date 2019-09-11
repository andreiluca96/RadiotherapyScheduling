# Timetable Scheduler GA

#### Note: this is a WIP

### Table of Contents

1. Purpose
2. Input and output
3. Chromosome representation
4. Mutation and crossover
5. Fitness function
6. Selection

### Purpose

The aim of this project is to implement a GA solution to the university timetable scheduling problem.

### Input and output

### Chromosome

A chromosome represents the timetable for all student classes (and, consequently, all teachers), 
for every day of the week. Each class is represented as an array of days, and each day contains the subjects the students
are taking in that day, in a consecutive manner (no gaps are allowed in their schedules). A subject is represented via the
ID of the teacher that is assigned for it to that specific class. 

### Mutation and crossover

#### Mutation


### Fitness function

The fitness function evaluates the number of collisions teachers have. Given that it is physically impossible for a person
to be in two places at the same time, that is the only constraint we will take into consideration for starters. A collision
can be detected by comparing the same time slot for all classes and checking that no value appears more than once. 
One candidate solution will receive a point for every slot it manages to fill without violating said constraint.

### Selection
