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


  - The basic attributes we use in any workflow are:

    name — The name of your workflow (optional)

    on — GitHub event that triggers the flow. It can be repository events (push, pull requests, release) or webhooks, branch creation, issues, or members joining the repository.

    jobs — Workflows must have at least one job. Each job must have an identifier, it’s like a name for the task we perform say “build”, “test” etc.

    runs-on — The type of machine needed to run the job. These environments are called Runners. Some of them are windows server 2019, ubuntu 18.04, macOS Catalina 10.15, etc.

    steps — a list of all the commands or actions. Each step runs its process.

    uses — identifies an action to use, defines the location of that action. An action can be uploading and downloading artifacts or checkout or configure any cloud account. You can find various actions at GitHub MarketPlace, with categories including Continuous Integration, Deployment, Project management, Testing, Security, etc. I really suggest you to explore various actions, also we can publish our custom actions on the Marketplace.

    run — runs the command in the virtual environment shell.
    
    name — an optional name identifier for the step.
