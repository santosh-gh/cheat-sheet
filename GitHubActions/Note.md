# The Component of GitHub Actions
  - workflows: Workflows are essentially automated processes that contain one or more logically related 
    jobs. For example, you could put the build and run tests jobs into the same workflow, and the deployment job into a different workflow

  - event: Events are literally the events that trigger the execution of a job by GitHub Actions. 
    Recall we mentioned passing jobs to be executed through a config file? In that config file you'd also have to specify when a job should be executed.

    Example: on-PR to main
             on-push to main
             on-merge to main
             schedule a job

  - jobs: Jobs are the tasks you command GitHub Actions to execute through the YAML config file. 
    
    Example: build source code
             run tests 
             deploy the code that has been built to some remote server

  - actions: Actions are the reusable commands that you can reuse in your config file. You can write 
    your custom actions or use existing ones.

  - runner: A runner is the remote computer that GitHub Actions uses to execute the jobs you tell it to.


  - Events (Pull Request, Push to a branch,Create Issue, Close Issue)

  - Workflow 
    - Job1
      - Step1: Action
      - Step2: Shell Command
      - Step3: Action

    - Job2 
      - Step1: Shell Command

  - Runner (Each Job run in a Machine-Runner)
    Runner run the steps of the Job and Log Results
    Two type of runner (GitHub hosted and Self hosted)

  - Steps does not run in parallel, it run in sequential
  - Jobs Run in parallel