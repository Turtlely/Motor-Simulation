# Motor Simulation
 
This is a simulation of a coil placed within a magnetic field of strength B teslas.
The parameters of the simulation can be adjusted in ``config.py``.

A crude commutator simulator is built in, that switches the flow of current accordingly to create a smooth rotation. 

This simulator uses the euler method of numerically solving differential equations. this is because thats easy to program.