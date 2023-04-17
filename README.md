# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Aline Garcia-Sanchez
- Isabel Fernandez

## Lab Question Answers

Question 1: Under what circumstances do you think it will be worthwhile to offload one or both
of the processing tasks to your PC? And conversely, under what circumstances will it not be
worthwhile?

Answer: If the data is very large, it will be better to offload. Transferring the data may take longer than it will take to execute in the RPI itself if the data is small, so if a data set is significantly large, offload it.

Question 2: Why do we need to join the thread here? 

Answer: The threads need to be joined to ensure that they finished executing before the program moves on. Otherwise it would kep executing what comes next and it might cause issues if it needs things that the thread is processing.

Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?

Answer: These processes are concurrent. SInce they are threads, they are running on the same core, but technically not at the exact same time. For it to be parallel, they would need to be running on different cores so they can actually execute at the exact same time.

Question 4: What is the best offloading mode? Why do you think that is?

Answer: Offloading both seems to be the best mode of offloading (since it has the shortest bar on the graph). This is probably because the data was large and the computer (not the RPI) could execute the tasks much faster and make up for the lost time used for transfer.

Question 5: What is the worst offloading mode? Why do you think that is?

Answer: Process 2... it has the tallest bar. I would like to think this is because process 2 requires more calculations and thus takes longer to execute. Offloading the first process takes time due to transfer and then the RPI got stuck with the longer of the tasks, leading to the slowest execution time.

Question 6: The processing functions in the example aren't very likely to be used in a real-world application. 
What kind of processing functions would be more likely to be used in a real-world application?
When would you want to offload these functions to a server?

Answer: ...