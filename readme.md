Course: Introduction to Programming 

Institution: International Balkan University

Student ID: 1008552

Student Name: Muhammed Emin Kalkan


1. Executive Summary

This project is a hybrid game engine that integrates classic "Snake" mechanics with "Maze Solver" logic. Unlike standard snake games, this application features a 4-stage evolutionary environment that adapts based on the player's performance. The project was developed using Python and the Pygame library, following modular and functional programming principles.



2. Technical Architecture & Algorithms

**Head Projection:** The current 'direction' vector is added to the head coordinates ('snake[0]') to calculate the potential next position ('new_head').

**Queue Manipulation:** The new head coordinate is inserted at the beginning of the list ('index 0').   

**Condition-Based Truncation:** - If the snake has not collided with food, the last segment of the tail is removed using 'pop()'.


The stability of the game depends on the precision of the collision detection algorithm. The system executes a three-layered verification process during each frame:

**Self-Collision Logic ($O(n)$):** Scans the remaining elements of the snake list using the 'in' operator to determine if the head has overlapped with its own body.

**Dynamic Maze Collision:** The 'new_head' is cross-referenced with the 'current_maze' coordinate list. This check is dynamic, as the matrix updates automatically when the level changes.


Generating food requires more than simple randomization; the system must ensure that the food does not spawn inside a wall or the snake's body.

**Randomization:** A coordinate pair is generated within the 20x20 grid using 'random.randit'.

**Constraint Verification:** The generated coordinate is checked against both the 'snake'   list and the 'current_maze' list.

**Iterative Retry:** If a conflict is detected, the system repeats the process through a 'while true' loop until a valid coordinate is found.

Phase 1: Architectural Planning & Conceptualization
Prompt: "I want to build a Python-based Snake game using Pygame. However, I want it to be unique. Can we integrate a maze system that changes dynamically as the player scores?"

Outcome: The AI suggested integrating a Level Matrix into the main Game Loop. This allowed the environment to shift based on the score variable.

Phase 2: Data Structures & Modularity
Prompt: "How can I store maze coordinates efficiently so the game can switch between 4 different levels without lag? Should I use nested lists or classes?"

Outcome: We implemented Nested Lists containing tuples for each level. This approach optimized memory usage and allowed for O(1) or O(n) collision lookups, ensuring smooth level transitions.

Phase 3: Algorithmic Logic (Spaced Walls)
Prompt: "I want the maze walls to have gaps so the snake can maneuver through them. Can we use a mathematical operator like modulo to generate these gaps automatically?"

Outcome: We developed the create_spaced_wall function. By using the Modulo (%) operator, we created a "comb-like" effect, providing strategic gaps for the snake to pass through.

Phase 4: Collision Detection & Validation
Prompt: "The maze changes at score 5. How do I ensure the food doesn't spawn inside a wall after the environment shifts? I need a validation loop."


Outcome: A while True loop was added to the get_food function. This validates that the food's random coordinates do not overlap with the snake's body or the newly generated maze walls.




Throughout this project, I treated the AI as a technical engineering partner. I designed the high-level logic—such as the level progression and the mathematical spacing of walls—and then collaborated with the AI to implement that logic into clean Python syntax. This partnership allowed me to focus on complex algorithm design while ensuring the code remained modular, bug-free, and aligned with industry standards.