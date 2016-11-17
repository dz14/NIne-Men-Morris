
# import student's functions
from solution import *

#Select what to test
test_manhattan = True
test_alternate_heuristic = False
test_weighted_astar = False
test_fval_function = True

if test_manhattan:
    ##############################################################
    # TEST MANHATTAN DISTANCE
    print('Testing Manhattan Distance')

    #Correct Manhattan distances for the initial states of the provided problem set
    correct_man_dist = [8, 6, 2, 4, 8, 2, 3, 1, 3, 4, 11, 8, 7, 4, 11, 8, 10, 8, 
                        12, 12, 12, 13, 13, 12, 10, 13, 13, 12, 10, 6, 35, 45, 28, 
                        32, 41, 29, 43, 35, 36, 32]

    solved = 0; unsolved = []

    for i in range(0,40):
        print("PROBLEM {}".format(i))

        s0 = PROBLEMS[i]

        man_dist = heur_manhattan_distance(s0)
        print('calculated man_dist:', str(man_dist))
        #To see state
        print(s0.state_string())

        if man_dist == correct_man_dist[i]:
            solved += 1
        else:
            unsolved.append(i)    

    print("*************************************")  
    print("In the problem set provided, you calculated the correct Manhattan distance for {} states out of 40.".format(solved))  
    print("States that were incorrect: {}".format(unsolved))      
    print("*************************************\n") 
    ##############################################################

if test_alternate_heuristic:
    ##############################################################
    # TEST ALTERNATE HEURISTIC WITH 1 SECOND TIME BOUND
    print('Testing Alternate Heuristic with 1 second time bound')

    #1 Second Benchmark
    complete_in_1_sec = 23
 
    solved = 0; unsolved = []; timebound = 1; 

    for i in range(0,40):
        print("*************************************") 
        print("PROBLEM {}".format(i))
        s0 = PROBLEMS[i]
        se = SearchEngine('best_first', 'full')
        final = se.search(initState=s0, heur_fn=heur_alternate, timebound=timebound, goal_fn=sokoban_goal_state)

        if final:
            solved += 1
            #If you want to see the path
            # final.print_path()
        else:
            unsolved.append(i)   

    print("\n*************************************")  
    print("In the problem set provided, {} were solved in less than {} seconds by this solver.".format(solved, timebound))  
    print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))   
    print("A benchmark heuristic achieved {} solved problems in 1 sec.".format(complete_in_1_sec))     
    print("*************************************\n") 
    ##############################################################

    ############################################################## 
    # TEST ALTERNATE HEURISTIC WITH 5 SECOND TIME BOUND
    print('Testing Alternate Heuristic with 5 second time bound')

    #5 Second Benchmark
    complete_in_5_secs = 24

    solved = 0; unsolved = []; timebound = 5; #costbound = 12

    for i in range(0,40):
        print("*************************************") 
        print("PROBLEM {}".format(i))
        s0 = PROBLEMS[i]
        se = SearchEngine('best_first', 'full')
        final = se.search(initState=s0, heur_fn=heur_alternate, timebound=timebound, goal_fn=sokoban_goal_state)

        if final:
            solved += 1
            #If you want to see the path
            # final.print_path()
        else:
            unsolved.append(i)   

    print("\n*************************************")  
    print("In the problem set provided, {} were solved in less than {} seconds by this solver.".format(solved, timebound))  
    print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))  
    print("A benchark heuristic achieved {} solved problems in 5 sec.".format(complete_in_5_secs))     
    print("*************************************\n") 
    ##############################################################

if test_weighted_astar:

  len_benchmark = [16, 13, 4, 10, 21, 9, 10, 5, 8, 18, -99, -99, 16, 11, 41, 14, 14, 14, -99, -99, 37, -99, 38, -99, -99, 33, 33, 29, 29, 18, -99, -99, -99, 81, -99, -99, -99, -99, -99, -99]

  ##############################################################
  # TEST ANYTIME WEIGHTED A STAR
  print('Testing Anytime Weighted A Star')

  solved = 0; unsolved = []; benchmark = 0; timebound = 8 #8 second time limit 
  for i in range(0,40):
    print("*************************************")  
    print("PROBLEM {}".format(i))

    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    final = weighted_astar(s0, timebound)

    if final:
      final.print_path()   
      if final.gval <= len_benchmark[i] or len_benchmark[i] == -99:
        benchmark += 1
      solved += 1 
    else:
      unsolved.append(i)  

  print("\n*************************************")  
  print("Of 40 initial problems, {} were solved in less than {} seconds by this solver.".format(solved, timebound))  
  print("Of the {} problems that were solved, the cost of {} matched or outperformed the benchmark.".format(solved, benchmark))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))  
  print("The benchmark implementation solved 24 out of the 40 practice problems given 8 seconds.")  
  print("*************************************\n") 
  ##############################################################


if test_fval_function:

  test_state = SokobanState("START", 6, None, None, None, None, None, None, None)

  correct_fvals = [6, 8, 10]

  ##############################################################
  # TEST fval_function
  print("*************************************") 
  print('Testing fval_function')

  solved = 0
  weights = [0., .5, 1.]
  for i in range(len(weights)):

    test_node = sNode(test_state, hval=10, fval_function=fval_function, weight=weights[i])

    fval = fval_function(test_node, weights[i])
    print ('Test', str(i), 'calculated fval:', str(fval), 'correct:', str(correct_fvals[i]))
    
    if fval == correct_fvals[i]:
      solved +=1  


  print("\n*************************************")  
  print("Your fval_function calculated the correct fval for {} out of {} tests.".format(solved, len(correct_fvals)))  
  print("*************************************\n") 
  ##############################################################


