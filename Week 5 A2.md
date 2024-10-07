# A2: 


## A2a: About your group  
### I am confident coding in Python:  
>1-Disagree  
### What is your group’s focus area?  
>Built  
### Is you focus area keeping the manager role?  
>Yes  
### Are you an analyst or a manager?  
>Analyst 


## A2b: Identify Claim   
* We are working on building building 2411.  
* We want to identify the total cost of the glass facade.  
* By doing this we want to check quantities of glass facade and then add the cost to it.   
* This script could be useful in both the early and later stages of the design process. Also we believe that with a script like this we could easily reuse it to find for example column and       cost, or change it find columns and total volume, and then again use it for LCA analyses and similar.   

## A2c: Use Case
### How you would check this fact?
   * We will get the scipt to get the total area of facade from the model. We will then give the price as an imput. We will also try to see if we can make the script read the                  report and find the price itself, but this would be useless if we on another project have a model but not a report attached. 
### When would this claim need to be checked?
   * This fact could be checked at an early stage because this is the time when it`s easiest to do changes. For example we check the total pricing of the facade and figure out                 the type chosen is to ecxpensive so it should be changed for another one, or the area with facade should be decreased. It could also be used at any point of the project, depending       on what it should be used for (LCA, process plan etc) .
### What information does this claim rely on?
   * The area of each wall, and then added together to get the total area. And then the chosen facade type, and the unit price (per m2) for this type.
### What phase? planning, design, build or operation.
* The cost would mainly be relevant in the planning and design phase, to make desicions. But also during building phase to track budgets. Quantities in itself is relevant for all                 phases. For example build when making a schedule. 
### What BIM purpose is required? Gather, generate, analyse, communicate or realise
* Gather, because we are quantifying elements. 
### Review use case examples - do any of these help?, What BIM use case is this closest to? If you cannot find one from the examples, you can make a new one.
* 02 Cost Estimation is similar to what we will be doing. 

## A2d:Scope the use case
* In the BPMN diagram is highlighted in red where the script is needed. 

## A2e: Tool Idea 
### Describe in words your idea for your own OpenBIM ifcOpenShell Tool in Python: 
* The idea for this ifcOpenShell Tool is that the user can in a short time get the total price of the chosen facade type for the building. This can be used to compare different options. 
### What is the business and societal value of your tool?
* The business value of this tool is that they can make informed desicion about materials / types for their projects, in this case facade type.
* The societal value can be that clients can get buildings that better alligns with their requirements.
 ![BPMN](https://raw.githubusercontent.com/Odanorland/BIManalyst_g_40_new/refs/heads/main/Diagram.svg)




## A2f: Information requirements
### Identify what information you need to extract from the model
#### Where is this in IFC?
* IfcCurtainWall - TypeName
#### Is it in the model?
* It should be, but requires that the architect/producer of the model has assigned a name to "TypeName" for facade. 
#### Do you know how to get it in ifcOpenShell?
* Yes, we have an idea. 
#### What will you need to learn to do this?
* For now we think we know how to do it, but it is likely that we will come across issues when we get to the actual coding, and then we`ll add it to the excel sheet. 

## A2g: Identify appropriate software licence
* GPL-3.0



