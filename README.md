# Cline Demo Preparation

Preparing a demo for showcasing Cline extension to corporate friends.

| Use Case                | Description |
| ----------------------- | ----------- |
| Code Generation         | Generate a FastAPI endpoint with a router named 'items', a prefix of '/items', and two routes: a GET route at '/' named 'read_items' that returns a list of sample items, and a GET route at '/{item_id}' named 'read_item' that returns the item ID. Set up a virtual environment for the project, install the necessary dependencies, and run the FastAPI application. If any errors occur, identify and resolve them, ensuring the application runs successfully. |
| Code Explanation        | Explain implementation of code.py. Generate a new file revised-code.py with similar implementation but with improved formatting. Check that implementation of code.py and revised-code.py are similar. |
| Debugging               | Check example1.py for potential bugs |
| File Manipulation       | Fill the existing data csv file with a synthetic dataset. I want 4 columns: first name, last name, age, sex, profession. All people working in IT and Aeronautics. Generate a shell command that renames all files in the "files" directory that contain "old" in their name, replacing it with "new". Execute the command in the terminal and verify that the files are renamed correctly. Zip all files within 'files/' under a file named "backup.zip". Tell me which command to use to unzip this file later. Read content of long story short text file and tell me what this content is about. |
| Terminal Interaction    | User instructions to Cline assistant: I'm a real novice in linux. Explain to me what are the current permissions in the current folder. |
| Documentation Generation | Revise and complete documentation inside configuration.ts, ensuring documentation is consistent with current implementation. |

## README Template

Here is an example of how the README of a use case should be filled:

```markdown
# Use Case Title

This use case demonstrates how Cline can be used to [do something].

**Goal:** [Describe the goal of the use case in a concise and impactful way].

**User instructions to Cline assistant:** [Describe the instructions of the use case].
```

The README Template is to be filled within each use case folder. This is important because it helps to define the goal and scenario of the use case before any work is done. This ensures that the use case is focused and that the work is aligned with the intended outcome. This should be done before anything else when working on a use case folder.
