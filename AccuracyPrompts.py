from langchain.prompts import PromptTemplate, FewShotPromptTemplate


#Accuracy prompt technqiues = '[IO prompt]X, [Self-Generate Prompt Instructions]X, [Zero/One/Few Shot CoT], [Self-Consistency CoT], [Self-Evaluation]X, Chained Prompting [hierarchical divide-and-conquer]X, [Tree-Of-Thought Prompting]X, [Genetic_Prompting]X'  

 
###Zero Shot prompting 
Zero_Shot_Prompt = PromptTemplate(input_variables=["question"], template= """Question: {question}

Answer: Let's think step by step.""")

###Few-Shot CoT (One-Shot CoT is just a reduced version)
Chain_of_Though_Prompt = PromptTemplate(input_variables=["MainQuestion","Question1", "Answer1", "Question2", "Answer2"], template="""You are a brilliant problem-solver, thinker and task perfectionist. Your job is to answer the following question: {MainQuestion} 
                                        
                                        Here are few Question-and-Answers examples to help you answer the question
                                        
                                        ---
                                        Examples
                                        ---
                                        
                                        Q: {Question1}
                                        A: {Answer1}
                                        
                                        Q:{Question2}
                                        A:{Answer2}
                                        
                                        
                                        Q: {MainQuestion}
                                        A:
                                        
                                                                                
                                        """)



###ToT: Breadth-First Searhc or Depth-First Search
Tree_Of_Thought_Prompt = PromptTemplate(input_variables=["question"], template="""Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realises they're wrong at any point then they leave. The question is...

Simulate three brilliant, logical experts collaboratively answering a question. Each one verbosely explains their thought process in real-time, considering the prior explanations of others and openly acknowledging mistakes. At each step, whenever possible, each expert refines and builds upon the thoughts of others, acknowledging their contributions. They continue until there is a definitive answer to the question. For clarity, your entire response should be in a markdown table. The question is {question}.

Identify and behave as three different experts that are appropriate to answering this question.
All experts will write down the step and their thinking about the step, then share it with the group.
Then, all experts will go on to the next step, etc.
At each step all experts will score their peers response between 1 and 5, 1 meaning it is highly unlikely, and 5 meaning it is highly likely.
If any expert is judged to be wrong at any point then they leave.
After all experts have provided their analysis, you then analyze all 3 analyses and provide either the consensus solution or your best guess solution.
The question is {question}
                                        
                                        
                                        """)


#Self-Evaluation Prompt
Self_Evaluate_Prompt = PromptTemplate(input_variables=["answer"], template= """ Please self-evaluate thoroughly the following {answer} that you gave. Make sure to refine as much as possible.
                                      
                                      Please present your answer in the following format:
                                      
                                      ----
                                      Answer:
                                      ----
                                      
                                      Here is a more complete, refined and update version of your answer!
                                      
                                      """)

#Automaticity Prompt
Self_Generated_Instructions_Prompt=PromptTemplate(input_variables= [], template="""You are a robot for creating prompts. You need to gather information about the user's goals, examples of preferred output, and any other relevant contextual information.

The prompt should contain all the necessary information provided to you. Ask the user more questions until you are sure you can create an optimal prompt.

Your answer should be clearly formatted and optimized for ChatGPT interactions. Be sure to start by asking the user about the goals, the desired outcome, and any additional information you may need.
                                                    
                                                    """)
  
#Task facilitation Prompt
Chained_Prompting = PromptTemplate(input_variables=["task"], template=""" You are a Question-Answering, Task performing chatbot for answering questions as well as performing tasks perfectly and properly. You are provided the following {task} either in the form of a question or an imperative.
                                   Before performing the task, it is favorable to divide-and-conquer the task execution strategy in a hierarchical manner: 1-Architecture/format/outline/scaffold -> 2-Relevant content -> 3-Perform the task, More specifically:
                                   At first, in order to facilitate this task for you, you should first start with providing yourself with the appropriate architecture, outline, scaffold..etc of your answer based on the task given to you, so that you understand the overall format of the answer.
                                   Second, before performing the task, make sure to filter out irrelevant information in the answer ie; make sure to exclusively include relevant, enriching and seemingly satisfactorily content in your already formed architecture format. 
                                   Finally, perform the specific task given to you by exploiting the appropriate format/architecture as well as the content you generated previously in order to increase your efficiency and performance. (Remember, the reason you are told to extract the appropriate answer architecture/format as well as relevant content, is just to facilitate your task performance by minimizing the workload you have to do during task performance)
                                   """ ) 
  
#This one is inspired from ToT (it still can be refined though)  [a little bit similar to Self-Consistency CoT]
Genetic_Prompting = PromptTemplate(input_variables=["Answer1", "Answer2"], template=""" Imagine 3 brilliant experts evaluating these two answers: 
                                   
                                   Answer 1: {Answer1},
                                   Answer 2: {Answer2},
                                   
                                   Simulate three brilliant, logical experts collaboratively evaluating the two answers. Each one verbosely explains their thought process in real-time, considering the prior explanations of others and openly acknowledging mistakes. At each step, whenever possible, each expert refines and builds upon the thoughts of others, acknowledging their contributions. They continue until there is a definitive best answer between the two answers. For clarity, your entire response should be in a markdown table.

Identify and behave as three different experts that are appropriate to evaluating the two answers.
All experts will write down the step and their thinking about the step, then share it with the group.
Then, all experts will go on to the next step, etc.
At each step all experts will score their peers response between 1 and 5, 1 meaning it is highly unlikely, and 5 meaning it is highly likely.
If any expert is judged to be wrong at any point then they leave.
After all experts have provided their analysis, you then analyze all 3 analyses and provide either the consensus answer or your best guess answer
                                   
                                   """)
