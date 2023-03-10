# Simulation of an N-body problem using Pygame

This is a program written in the Python programming language using the Pygame library.
It simulates the movement of a number of "bodies" on a screen, where the bodies are represented by circles. The positions, velocities, and accelerations of the bodies are updated based on forces that are calculated between the bodies according to Newton's law of gravitation.


https://user-images.githubusercontent.com/116048487/211740455-56093d16-1093-46ed-b829-a21417c40669.mp4




https://user-images.githubusercontent.com/116048487/211741224-da88772e-64c3-4c1c-8460-9d2fb127abf9.mp4






## How to Run

The program requires Python and Pygame to be installed on your computer
(at least Python 3.6) 

```bash
  pip install Python 3.6
  pip install pygame
```
    
## Customization

The user can customize the following parameters:

`G` : Gravitaional constant

`dt` : time step for the simulation

`width` and `height` : of the screen

`method` : two different formulas for the gravitational force can be chosen.

You also can set the initial body that consists of these parameters:

`x` and `y`: The initial position in the x-axis and y-axis

`vx` and `vy` : The initial velocity in the x-axis and y-axis

`mass`: The mass of the body

`color`: The color of the body

note: The size of the body is based on mass but you also can set it by adding the argument name radius.

## Information displayed

- FPS: The number of frames per second that the simulation is running at
- Particles: The number of bodies in the simulation
- G: The Gravitaional constant
- dt: The time step of the simulation
- Method : Which formula is used to calculate gravitational force.

## Note

- Adjusting parameters such as dt and G can change the way the simulation runs and affects the stability of the simulation.

- Lowering dt will increase the precision of the simulation but also increase the running time of the simulation.

- This program only simulated the motion of the body in 2-dimension.

## Time complexity
The time complexity of this simulation is O(n^2) as the force calculation between each body with every other bodies and updating the position and velocity.
As the number of bodies increases, the amount of computation also increases quadratically. This may cause the simulation to become slow with a large number of particles.

## Optimization
We can Optimize the code by using The Barnes-Hut Algorithm to move from O(n^2) to O(NlogN)
- The main idea of The Barnes-Hut is that instead of being calculated in every pair of bodies, We switched to calculating the center of mass instead.
- It recursively divides the set of bodies into groups by storing them in a quad-tree.

Here is more content about Barnes-Hut Algorithm if you are interested.
http://arborjs.org/docs/barnes-hut


![2022-12-24 (117)](https://user-images.githubusercontent.com/116048487/211741568-91ca24f4-954e-4736-88e2-8185f6160a25.png)
![2022-12-24 (126)](https://user-images.githubusercontent.com/116048487/211741590-ab829a01-2151-4ec9-8184-5596766b0001.png)
![2022-12-24 (129)](https://user-images.githubusercontent.com/116048487/211741598-34a29e92-9e33-4c3e-921e-b5f3a93f6b68.png)
![2022-12-24 (131)](https://user-images.githubusercontent.com/116048487/211741612-194c3dec-0283-4a1a-b720-ad93eecc7195.png)
![2022-12-24 (134)](https://user-images.githubusercontent.com/116048487/211741630-80960784-42bf-41c0-afd8-1dc337f7f2cc.png)
![2022-12-24 (135)](https://user-images.githubusercontent.com/116048487/211741643-25678c5d-7ed8-492b-a0f4-7eec6e426bce.png)
