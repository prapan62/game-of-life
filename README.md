# Conway's Game of Life

Conway's Game of Life is a well-known mathematical simulation and "zero-player" game developed by British mathematician John Horton Conway in 1970. It takes place on an infinite, two-dimensional grid where "cells" live, die, or reproduce according to four simple principles based on their neighbors.

# The 4 Principles

Conway's Game of Life follows 4 main rules:

 (For populated spaces)
1. Each cell with one of more neighbors dies, as if by loneliness.

 <img width="105" height="92" alt="Screenshot 2026-06-28 at 9 29 46 PM" src="https://github.com/user-attachments/assets/4576b804-3280-41f3-a684-c81deab64d95" /> -> <img width="132" height="92" alt="Screenshot 2026-06-28 at 9 29 55 PM" src="https://github.com/user-attachments/assets/7f031c82-3396-4943-b609-27dd8957a114" />

2. Each cell with four or more neighbors dies, as if by overpopulation.

<img width="61" height="61" alt="Screenshot 2026-06-28 at 9 28 45 PM" src="https://github.com/user-attachments/assets/9a15714a-acf1-4439-b888-fbe53ca64b60" /> -> <img width="78" height="69" alt="Screenshot 2026-06-28 at 9 28 56 PM" src="https://github.com/user-attachments/assets/9a1cbd18-e81c-4eb5-8710-054b38410956" />

3. Each cell with two or three neighbors survives.

<img width="106" height="103" alt="Screenshot 2026-06-28 at 9 30 28 PM" src="https://github.com/user-attachments/assets/78168bec-2364-4e3d-86eb-294ad3ea2b25" /> -> <img width="103" height="82" alt="Screenshot 2026-06-28 at 9 30 39 PM" src="https://github.com/user-attachments/assets/c5758fb4-1fd4-4f85-a8ea-92cead89ce30" />

 (For empty or unpopulated spaces)  
4. Each cell with three neighbors becomes populated.

<img width="81" height="72" alt="Screenshot 2026-06-28 at 9 31 02 PM" src="https://github.com/user-attachments/assets/5b89ac85-f1b9-4a7c-ad12-23db3cdd0d30" /> -> <img width="82" height="68" alt="Screenshot 2026-06-28 at 9 31 13 PM" src="https://github.com/user-attachments/assets/b1ae6de0-9ed0-4c81-8833-858c3253593e" />

# What it Models in the Real World

Conway's Game of Life uses four simple rules to simulate population dynamics: cells die from isolation or overpopulation, live with the appropriate number of neighbors, and reproduce when conditions are ideal, precisely simulating the fundamental problems that real populations face. When these local principles are applied simultaneously to thousands of cells, spiraling cycles of ups and downs and self-organizing patterns emerge, with no central coordination. It demonstrates that the complex behavior of natural populations, ranging from bacterial colonies to animal herds, may be fully explained by a few simple local interactions.
