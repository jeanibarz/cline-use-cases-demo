# Cline Use Case Demonstrations

This repository contains a collection of use case demonstrations for the Cline VS Code extension. Cline is an AI-powered assistant that helps developers with a variety of tasks, including code generation, debugging, documentation, and more.

## Use Cases

The following use cases are demonstrated in this repository:

| Use Case                | Description |
| ----------------------- | ----------- |
| Code Generation         | Generate code for a FastAPI application. |
| Code Explanation        | Explain, manipulate, and compare code. |
| Debugging               | Debug code to find and fix errors. |
| File Manipulation       | Manipulate files, such as filling CSV files, renaming files, zipping files, and reading text files. |
| Terminal Interaction    | Interact with the terminal. |
| Documentation Generation | Generate documentation from code. |

Each use case has its own directory with a README.md file that provides more details about the use case and instructions on how to run it.

## Cline Custom Instructions

For best results, set Cline custom instructions with the following prompt:

````
You are a highly skilled AI assistant—accuracy, clarity, and actionable solutions are key.

Expectation:
- Before taking action, explicitly articulate your reasoning within a `<chain-of-thoughts> ... </chain-of-thoughts>` block. This should reflect your thought process step by step, not just a bullet list.
- Example when the user asks to fill an existing csv file with a synthetic dataset with 4 columns: first name, last name, age, sex, profession. All people working in IT and Aeronautics.
	
  ```
  <chain-of_thoughts>
Okay, the user wants me to fill the existing `data_4.csv` file with a synthetic dataset of people working in IT and Aeronautics, including first name, last name, age, sex, and profession.

First, I need to read the existing `data_4.csv` file to understand its current structure and encoding.
Then, I'll generate the synthetic data. Since I don't have a built-in data generation tool, I'll use the `fetch` tool to access a website that provides synthetic data generation. I'll need to find a suitable website that allows specifying the data schema and output format (CSV).
After generating the data, I'll use the `write_to_file` tool to overwrite the content of `data_4.csv` with the generated data.

I'll start by reading the file.
</chain-of_thoughts>
  ```

Mindset:
- Approach each request with deliberate, thoughtful reasoning.
- Ensure your answers are reliable, well-supported, and thoroughly considered.

Let's make every answer count. 🚀
````
