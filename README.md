# ComfyUI-QwenImage-PromptStorage-Node
ComfyUI-Qwen-Image-Prompt-Storage-Node loads and manages prompts from a prompt_storage.json file in ComfyUI workflows. Users can select from predefined prompts or input custom positive and negative prompts manually, with manual input taking priority over selection.

---

This repository contains a custom node for **ComfyUI** that integrates with **Qwen-Image** models. It allows users to load and manage predefined prompts from a `prompt_storage.json` file, or enter custom prompts manually for use in workflows. This node helps automate and streamline prompt selection for image generation.

## Features

- **Load prompts** from a `prompt_storage.json` file.
- **Select prompts** from a predefined library or enter custom **positive** and **negative** prompts manually.
- **Prioritization**: Custom inputs take precedence over selected prompts.
- **Return**: Positive and negative prompts as strings for integration into workflows.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/modula-r/ComfyUI-QwenImage-PromptStorage-Node.git


2. Install the dependencies (if applicable) for your environment. This node is designed to work with ComfyUI and requires Python 3.x.

3. Place the prompt_storage.json file in the same directory as the script, with the following structure: 


```json
{
  "library": [
    {
      "name": "Prompt 1",
      "positive": "positive prompt text",
      "negative": "negative prompt text"
    },
    {
      "name": "Prompt 2",
      "positive": "positive prompt text",
      "negative": "negative prompt text"
    }
  ]
}
```

4. Use the node in your ComfyUI workflow as per the provided documentation.

## Usage

### Input:
The node expects three inputs:

prompt_choice: A selection from the available prompts or "None".

manual_positive: A string for custom positive prompts.

manual_negative: A string for custom negative prompts.

### Output:
The node returns two strings:

positive_prompt: The selected or entered positive prompt.

negative_prompt: The selected or entered negative prompt.


```python
positive, negative = prompt_storage_node.get_prompt("Prompt 1", "", "")
```

---

In this example, the node returns the positive and negative prompts associated with "Prompt 1" if no manual inputs are provided.

## License

This project is licensed under the Apache 2.0 License - see the LICENSE
 file for details.

## Contributing

1.Fork the repository.

2.Create a feature branch (git checkout -b feature-branch).

3.Commit your changes (git commit -am 'Add new feature').

4.Push to the branch (git push origin feature-branch).

5.Create a new Pull Request.

## Acknowledgments

ComfyUI for providing the framework for custom nodes.

Qwen-Image for the inspiration and integration with prompt management.

---

Note: This Custom Node is Part of the following Respo/Audit-Node´s from EU-AI Act2024 Compliance-dev. 

## Related Projects

### [EU-AI-ACT-2024-Praktische-Umsetzung](https://github.com/modula-r/EU-AI-ACT-2024-Praktische-Umsetzung)
This repository contains the practical implementation of the **EU-AI-ACT-2024** project. It explores AI applications in the context of the European Union's regulations and directives. The project includes research, case studies, and hands-on implementations of AI solutions.


