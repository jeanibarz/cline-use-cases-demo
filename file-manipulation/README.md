# File Manipulation Use Case

This use case demonstrates how Cline can be used to manipulate files.

**Goal:** To fill a CSV file with synthetic data, rename files in a directory, zip files, and read the content of a text file.

**User instructions to Cline assistant:**
- Fill the existing data csv file with a synthetic dataset. I want 4 columns: first name, last name, age, sex, profession. All people working in IT and Aeronautics.
- Generate a shell command that renames all files in the "files" directory that contain "old" in their name, replacing it with "new". Execute the command in the terminal and verify that the files are renamed correctly.
- Zip all files within 'files/' under a file named "backup.zip". Tell me which command to use to unzip this file later.
- Read content of long story short text file and tell me what this content is about.
