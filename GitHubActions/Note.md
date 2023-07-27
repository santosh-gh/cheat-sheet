# The Component of GitHub Actions
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