'''
book: Dead simple python 
--> There are two options to achieving concurrency in python:
    1)threading "pre-emptive multitasking" :
        * OS manages the multitasking by running eah task in a single flow of execution called thread
        * threads still share the same system process 
        * has its own pitfalls
    2)asynchrony "cooperative-multitasking": 
        * python handles it with your help ->sidestepping some issues that crop up with threading   
        * easiest way to achieve concurrency 
        * the operating system still sees your code running in single process with a single thread
        * it is not parallelism 
        * GIL (global Interpreter lock) mechanism in Python ensures a single process is constrained to a single CPU core.
        * It is possible with two keywords borrowed from C# . (async, await) + special types of coroutine.
        * execution is managed and run by event-loop available in asyncio module 
        * pick up either 
             -> Trio library(recommended): https://trio.readthedocs.io/en/stable/    
             -> curio library:https://curio.readthedocs.io/en/latest/
        * https://docs.python.org/3/library/asyncio.html
        * (outdated but still is used) https://twisted.org/
--> parallelism:
    multiple tasks occur simultaneously 
   
--> concurrency:
    rapidly dividing a program's singular attention between multiple tasks 
    does not actually speed up execution time
    Is not helpful with CPU-bounded tasks 
    Is helpful when dealing with IO-bound tasks(waiting for data or user entry )
    Is useful to performing a task at regular intervals (ex: saving a temp file every 5 mins)
    Is useful for improving perceived responsiveness
    
    
     
    



'''